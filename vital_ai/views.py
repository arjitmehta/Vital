
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
from .PoseModule import poseDetector
from .Activity import activity

def index(request, aasan='inter_1'):
    print(aasan)
    context = {
        'aasan': aasan
    }
    return render(request, 'index.html', context)

def video_stream(frame, aasan='inter_1'):
    # Flip the frame and process it via OpenCV and computer vision methods.
    processed_frame = cv2.flip(frame, 1)
    detector = poseDetector()
    processed_frame = detector.findPose(processed_frame, False)
    lmList = detector.findPosition(processed_frame, False)
    
    if lmList:
        if aasan == 'ex_1':
            per = activity.lifting_curls_biceps(processed_frame, detector)
        elif aasan == 'ex_2':
            per = activity.lifting_floor_press(processed_frame, detector)
        elif aasan == 'ex_3':
            per = activity.lifting_bentover_dumbbell(processed_frame, detector)
        elif aasan == 'ex_4':
            per = activity.lifting_forearms(processed_frame, detector)
        elif aasan == 'ex_5':
            per = activity.lifting_dumbell_squats(processed_frame, detector)
        elif aasan == 'ex_6':
            per = activity.lifting_shoulder_press(processed_frame, detector)
        elif aasan == 'beg_1':
            activity.yoga_beg_aasana1(processed_frame, detector)
        elif aasan == 'beg_2':
            activity.yoga_beg_aasana2(processed_frame, detector)
        elif aasan == 'beg_3':
            activity.yoga_beg_aasana3(processed_frame, detector)
        elif aasan == 'beg_4':
            activity.yoga_beg_aasana4(processed_frame, detector)
        elif aasan == 'beg_5':
            activity.yoga_beg_aasana5(processed_frame, detector)
        elif aasan == 'beg_6':
            activity.yoga_beg_aasana6(processed_frame, detector)
        elif aasan == 'beg_7':
            activity.yoga_beg_aasana7(processed_frame, detector)
        elif aasan == 'beg_8':
            activity.yoga_beg_aasana8(processed_frame, detector)
        elif aasan == 'beg_9':
            activity.yoga_beg_aasana9(processed_frame, detector)
        elif aasan == 'beg_10':
            activity.yoga_beg_aasana10(processed_frame, detector)
        elif aasan == 'inter_1':
            activity.yoga_inter_aasana1(processed_frame, detector)
        elif aasan == 'inter_2':
            activity.yoga_inter_aasana2(processed_frame, detector)
        elif aasan == 'inter_3':
            activity.yoga_inter_aasana3(processed_frame, detector)
        elif aasan == 'inter_4':
            activity.yoga_inter_aasana4(processed_frame, detector)
        elif aasan == 'inter_5':
            activity.yoga_inter_aasana5(processed_frame, detector)
        elif aasan == 'inter_6':
            activity.yoga_inter_aasana6(processed_frame, detector)
        elif aasan == 'inter_7':
            activity.yoga_inter_aasana7(processed_frame, detector)
        elif aasan == 'inter_8':
            activity.yoga_inter_aasana8(processed_frame, detector)
        elif aasan == 'inter_9':
            activity.yoga_inter_aasana9(processed_frame, detector)
        elif aasan == 'inter_10':
            activity.yoga_inter_aasana10(processed_frame, detector)
        elif aasan == 'adv_1':
            activity.yoga_adv_aasana1(processed_frame, detector)
        elif aasan == 'adv_2':
            activity.yoga_adv_aasana2(processed_frame, detector)
        elif aasan == 'adv_3':
            activity.yoga_adv_aasana3(processed_frame, detector)
        elif aasan == 'adv_4':
            activity.yoga_adv_aasana4(processed_frame, detector)
        elif aasan == 'adv_5':
            activity.yoga_adv_aasana5(processed_frame, detector)
        elif aasan == 'adv_6':
            activity.yoga_adv_aasana6(processed_frame, detector)
        elif aasan == 'adv_7':
            activity.yoga_adv_aasana7(processed_frame, detector)
        elif aasan == 'adv_8':
            activity.yoga_adv_aasana8(processed_frame, detector)
        elif aasan == 'adv_9':
            activity.yoga_adv_aasana9(processed_frame, detector)
        elif aasan == 'adv_10':
            activity.yoga_adv_aasana10(processed_frame, detector)
    
    return processed_frame

@csrf_exempt
def video_feed(request, aasan='inter_1'):
    if request.method == 'POST':
        # Read the uploaded frame.
        frame_file = request.FILES['frame']
        np_frame = np.frombuffer(frame_file.read(), np.uint8)
        frame = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)
        
        # Process the frame via your video_stream function.
        processed_frame = video_stream(frame, aasan)
        
        # Encode the processed frame as JPEG.
        success, buffer = cv2.imencode('.jpg', processed_frame)
        if success:
            return HttpResponse(buffer.tobytes(), content_type='image/jpeg')
        else:
            return HttpResponse(status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})