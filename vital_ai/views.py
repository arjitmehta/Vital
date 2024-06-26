from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
import cv2
import numpy as np
import os
import random
from .PoseModule import poseDetector
from .Activity import activity



def index(request,aasan='none'):
    print(aasan)
    context = {
        'aasan': aasan
    }
    return render(request, 'index.html',context)

def video_stream(aasan='none'):
    # a="inter_1"
    # a="inter_"+str(random.randrange(1,11))
    a=aasan
    # print('this---',act,a)
    b=0
    ex=0
    cap = cv2.VideoCapture(0)
    

    # VITAL = activity()
    detector = poseDetector()
    count = 0
    dir = 0
    per=0
    pTime = 0
    while True:
        success, processed_frame = cap.read()
        if not success:
            break

        #processed_frame = cv2.imread("Yoga_test_images/Beginner/beg_6.png")
        #processed_frame = cv2.resize(processed_frame, (720, 720))
        processed_frame = cv2.flip(processed_frame, 1)
        processed_frame = detector.findPose(processed_frame,False)
        lmList = detector.findPosition(processed_frame, False)
        # print(lmList)
        if len(lmList) != 0:
            
            if a== 'ex_1' :
                per = activity.lifting_curls_biceps(processed_frame,detector)
                ex=1
            if a== 'ex_2' :
                per = activity.lifting_floor_press(processed_frame,detector) #make new conditions for respective functions
                ex=1
            if a== 'ex_3' :
                per = activity.lifting_bentover_dumbbell(processed_frame,detector)
                ex=1
            if a== 'ex_4' :
                per = activity.lifting_forearms(processed_frame,detector)
                ex=1
            if a== 'ex_5' :
                per = activity.lifting_dumbell_squats(processed_frame,detector)
                ex=1
            if a== 'ex_6' :
                per = activity.lifting_shoulder_press(processed_frame,detector)
                ex=1
            if a =='beg_1':
                activity.yoga_beg_aasana1(processed_frame,detector)
            if a =='beg_2':
                activity.yoga_beg_aasana2(processed_frame,detector)
            if a =='beg_3':
                activity.yoga_beg_aasana3(processed_frame,detector)
            if a =='beg_4':
                activity.yoga_beg_aasana4(processed_frame,detector)
            if a =='beg_5':
                activity.yoga_beg_aasana5(processed_frame,detector)
            if a =='beg_6':
                activity.yoga_beg_aasana6(processed_frame,detector)
            if a =='beg_7':
                activity.yoga_beg_aasana7(processed_frame,detector)
            if a =='beg_8':
                activity.yoga_beg_aasana8(processed_frame,detector)
            if a =='beg_9':
                activity.yoga_beg_aasana9(processed_frame,detector)
            if a =='beg_10':
                activity.yoga_beg_aasana10(processed_frame,detector)
            if a =='inter_1':
                activity.yoga_inter_aasana1(processed_frame,detector)
            if a =='inter_2':
                activity.yoga_inter_aasana2 (processed_frame,detector)
            if a =='inter_3':
                activity.yoga_inter_aasana3(processed_frame,detector)
            if a =='inter_4':
                activity.yoga_inter_aasana4(processed_frame,detector)
            if a =='inter_5':
                activity.yoga_inter_aasana5(processed_frame,detector)
            if a =='inter_6':
                activity.yoga_inter_aasana6(processed_frame,detector)
            if a =='inter_7':
                activity.yoga_inter_aasana7(processed_frame,detector)
            if a =='inter_8':
                activity.yoga_inter_aasana8(processed_frame,detector)
            if a =='inter_9':
                activity.yoga_inter_aasana9(processed_frame,detector)
            if a =='inter_10':
                activity.yoga_inter_aasana10(processed_frame,detector)
            if a =='adv_1':
                activity.yoga_adv_aasana1(processed_frame,detector)
            if a =='adv_2':
                activity.yoga_adv_aasana2(processed_frame,detector)
            if a =='adv_3':
                activity.yoga_adv_aasana3(processed_frame,detector)
            if a =='adv_4':
                activity.yoga_adv_aasana4(processed_frame,detector)
            if a =='adv_5':
                activity.yoga_adv_aasana5(processed_frame,detector)
            if a =='adv_6':
                activity.yoga_adv_aasana6(processed_frame,detector)
            if a =='adv_7':
                activity.yoga_adv_aasana7(processed_frame,detector)
            if a =='adv_8':
                activity.yoga_adv_aasana8(processed_frame,detector)
            if a =='adv_9':
                activity.yoga_adv_aasana9(processed_frame,detector)
            if a =='adv_10':
                activity.yoga_adv_aasana10(processed_frame,detector)
            
                
                #print(angle, per)
                #Counting Reps
            if ex==1:
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
                #cv2.putText(processed_frame, "maintain", (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,(0, 0, 255), 5)
                #print(count)
                # Draw Rep Count
                    cv2.rectangle(processed_frame, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
                    cv2.putText(processed_frame, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                                (255, 0, 0), 25)    
        success,buffer=cv2.imencode('.jpg',processed_frame)
        frame=buffer.tobytes()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()
    

@csrf_exempt
def video_feed(request,aasan='none'):
    return StreamingHttpResponse(video_stream(aasan), content_type='multipart/x-mixed-replace; boundary=frame')

# Create your views here.
