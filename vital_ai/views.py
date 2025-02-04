# views.py
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from channels.generic.websocket import AsyncWebsocketConsumer
import cv2
import numpy as np
import json
import base64
from .PoseModule import poseDetector
from .Activity import activity

# Existing HTTP views
def index(request, aasan='inter_1'):
    context = {'aasan': aasan}
    return render(request, 'index.html', context)

@csrf_exempt
def video_feed(request, aasan='inter_1'):
    if request.method == 'POST':
        try:
            frame_file = request.FILES['frame']
            np_frame = np.frombuffer(frame_file.read(), np.uint8)
            frame = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)
            processed_frame = process_frame(frame, aasan)
            _, buffer = cv2.imencode('.jpg', processed_frame)
            return HttpResponse(buffer.tobytes(), content_type='image/jpeg')
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# WebSocket consumer
class VideoProcessorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.aasan = self.scope['url_route']['kwargs'].get('aasan', 'inter_1')
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            # Process binary frame data
            try:
                frame = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
                processed_frame = process_frame(frame, self.aasan)
                _, buffer = cv2.imencode('.jpg', processed_frame)
                await self.send(bytes_data=buffer.tobytes())
            except Exception as e:
                await self.send(text_data=json.dumps({'error': str(e)}))

# Common processing function
def process_frame(frame, aasan):
    detector = poseDetector()
    count = 0
    dir = 0
    per = 0
    ex = 0

    frame = cv2.flip(frame, 1)
    frame = detector.findPose(frame, False)
    lmList = detector.findPosition(frame, False)

    if len(lmList) != 0:
        # Your existing activity detection logic
        if aasan.startswith('ex_'):
            ex = 1
            exercise_map = {
                'ex_1': activity.lifting_curls_biceps,
                'ex_2': activity.lifting_floor_press,
                'ex_3': activity.lifting_bentover_dumbbell,
                'ex_4': activity.lifting_forearms,
                'ex_5': activity.lifting_dumbell_squats,
                'ex_6': activity.lifting_shoulder_press,
            }
            per = exercise_map.get(aasan, lambda *args: 0)(frame, detector)

        elif aasan.startswith(('beg_', 'inter_', 'adv_')):
            level, num = aasan.split('_')
            activity_func = getattr(activity, f'yoga_{level}_aasana{num}', None)
            if activity_func:
                activity_func(frame, detector)

        # Repetition counting logic
        if ex == 1:
            color = (255, 0, 255)
            if per == 100:
                color = (0, 255, 0)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 255, 0)
                if dir == 1:
                    count += 0.5
                    dir = 0

            cv2.rectangle(frame, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, str(int(count)), (45, 670), 
                       cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 25)

    return frame