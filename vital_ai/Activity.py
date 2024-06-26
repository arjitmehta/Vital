import numpy as np
# import time
# import PoseModule as pm
# import cv2
# import random

class activity():
    def yoga_beg_aasana0(img,detector):
        angle = detector.findAngle(img, 11, 13, 15, False)
        angle1 = detector.findAngle(img, 27, 25, 23, False)
        if angle <168 or angle >170:            
            angle = detector.findAngle(img, 11, 13, 15)
        if angle1 <75 or angle1 >80:
            angle1 = detector.findAngle(img, 27, 25, 23)
    def yoga_beg_aasana1(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 11, 23, 25, False)
        #feet ka KARNA POSSIBLE NAHI HO RAHAA
        angle4 = detector.findAngle(img, 31, 27, 25, False)
        if angle1 <160 or angle1>184:            
            angle = detector.findAngle(img, 15, 13, 11)
        if angle2 <170 or angle2 >182:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <154 or angle3 >178:
            angle3 = detector.findAngle(img, 11, 23, 25)
        if angle4 <154 or angle4 >178:
            angle4 = detector.findAngle(img, 31, 27, 25)
        
    def yoga_beg_aasana2(img,detector):
        angle1 = detector.findAngle(img, 25, 23, 11, False)
        angle2 = detector.findAngle(img, 15, 13, 11, False)
        angle3 = detector.findAngle(img, 27, 25, 23, False)
        if angle1 <70 or angle1>82:            
            angle1 = detector.findAngle(img, 25, 23, 11)
        if angle2 <162 or angle2>172:            
            angle2 = detector.findAngle(img, 15, 13, 11)
        if angle3 <172 or angle3 >200:
            angle3 = detector.findAngle(img, 27, 25, 23)

    def yoga_beg_aasana3(img,detector):
                
        angle1 = detector.findAngle(img, 11, 23, 25, False)
        angle2 = detector.findAngle(img, 27, 25, 23, False)
        angle3 = detector.findAngle(img, 24, 26, 28, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <65 or angle1 >135:            
            angle1 = detector.findAngle(img, 11, 23, 25)
        if angle2 <15 or angle2 >45:
            angle2 = detector.findAngle(img, 27, 25, 23)
        if angle3 <155 or angle3>185:            
            angle3 = detector.findAngle(img, 24, 26, 28)
        if angle4 <160 or angle4>184:
            angle4 = detector.findAngle(img, 23, 11, 13)
     
        
    def yoga_beg_aasana4(img,detector):
        angle1 = detector.findAngle(img, 16, 14, 12, False)
        angle2 = detector.findAngle(img, 24, 26, 28, False)
        angle3 = detector.findAngle(img, 24, 12, 14, False)
        if angle1 <170 or angle1>180:            
            angle = detector.findAngle(img, 16, 14, 12)
        if angle2 <172 or angle2 >190:
            angle2 = detector.findAngle(img, 24, 26, 28)
        if angle3 <5 or angle3>30:            
            angle3 = detector.findAngle(img, 24, 12, 14)
        pass
    def yoga_beg_aasana5(img,detector):
        #angle1 = detector.findAngle(img, 12, 14, 16, False)
        #angle2 = detector.findAngle(img, 26, 24, 12, False)
        angle3 = detector.findAngle(img, 28, 26, 24, False)
        angle4 = detector.findAngle(img, 27, 25, 23, False)
        angle5 = detector.findAngle(img, 11, 13, 15, False)
        #if angle1 <159 or angle1>163:            
            #angle1 = detector.findAngle(img,  12, 14, 16)
        if angle5 <160 or angle5 >200:
            angle5 = detector.findAngle(img, 11, 13, 15)
        if angle3 <220 or angle3>260:            
            angle3 = detector.findAngle(img, 28, 26, 24)
        if angle4 <180 or angle4>210:
            angle4 = detector.findAngle(img, 27, 25, 23)
        
        
    def yoga_beg_aasana6(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 24, 26, 28, False)
        if angle1 <170 or angle1>190:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        
        if angle2 <160 or angle2>182:            
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <90 or angle3>120:
            angle3 = detector.findAngle(img, 24, 26, 28)
        pass
    def yoga_beg_aasana7(img,detector):
        #9/10/21
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <170 or angle1>180:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <100 or angle2 >120:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <85 or angle3>108:            
            angle3 = detector.findAngle(img, 25, 23, 11)
        if angle4 <140 or angle4>180:
            angle4 = detector.findAngle(img, 23, 11, 13)
            
    def yoga_beg_aasana8(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 11, 23, 25, False)
        if angle1 <155 or angle1>180:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <160 or angle2 >176:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <130 or angle3>150:            
            angle3 = detector.findAngle(img, 11, 23, 25)
        pass
    def yoga_beg_aasana9(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <160 or angle1>180:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <160 or angle2 >180:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <160 or angle3>180:            
            angle3 = detector.findAngle(img, 25, 23, 11)
        if angle4 <40 or angle4>70:
            angle4 = detector.findAngle(img, 23, 11, 13)
        
    def yoga_beg_aasana10(img,detector):
        angle1 = detector.findAngle(img, 11, 13, 15, False)
        angle2 = detector.findAngle(img, 16, 14, 12, False)
        angle3 = detector.findAngle(img, 27, 25, 23, False)
        angle4 = detector.findAngle(img, 24, 26, 28, False)
        angle5 = detector.findAngle(img, 13, 11, 23, False)
        angle6 = detector.findAngle(img, 24, 12, 14, False)
        
        if angle1 <90 or angle1>115:            
            angle1 = detector.findAngle(img,  11, 13, 15)
        if angle2 <90 or angle2 >115:
            angle2 = detector.findAngle(img,  16, 14, 12)
        if angle3 <120 or angle3>150:            
            angle3 = detector.findAngle(img, 27, 25, 23)
        if angle4 <120 or angle4>150:
            angle4 = detector.findAngle(img, 24, 26, 28)
        if angle5 <90 or angle5>115:            
            angle5 = detector.findAngle(img, 13, 11, 23)
        if angle6 <90 or angle6>115:
            angle6 = detector.findAngle(img, 24, 12, 14)
            
            
   #******************************************************************************************************         
    def yoga_inter_aasana1(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11)
        angle2 = detector.findAngle(img, 12, 14, 16)
        if angle1 <35 or angle1>80:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <35 or angle2 >80:
            angle2 = detector.findAngle(img,12, 14, 16)
            
    def yoga_inter_aasana2(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 25, 23, 11, False)
        angle3 = detector.findAngle(img, 23, 25, 27, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <162 or angle1>180:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <82 or angle2 >92:
            angle2 = detector.findAngle(img, 25, 23, 11)
        if angle3 <160 or angle3>175:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <48 or angle4>58:
            angle4 = detector.findAngle(img, 23, 11, 13)
        
    def yoga_inter_aasana3(img,detector):
        angle1 = detector.findAngle(img, 24, 12, 14, False)
        angle2 = detector.findAngle(img, 16, 14, 12, False)
        angle3 = detector.findAngle(img, 27, 25, 23, False)
        angle4 = detector.findAngle(img, 24, 26, 32, False)
        angle5 = detector.findAngle(img, 26, 24, 12, False)
        if angle1 <80 or angle1>110:            
            angle1 = detector.findAngle(img,  24, 12, 14)
        if angle2 <160 or angle2 >191:
            angle2 = detector.findAngle(img,  16, 14, 12)
        if angle3 <160 or angle3>191:            
            angle3 = detector.findAngle(img, 27, 25, 23)
        if angle4 <160 or angle4>191:
            angle4 = detector.findAngle(img, 24, 26, 28)
        if angle5 <35 or angle5>60:            
            angle5 = detector.findAngle(img, 26, 24, 12)
        
        
    def yoga_inter_aasana4(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 25, 23, 11, False)
        angle3 = detector.findAngle(img, 23, 25, 27, False)
        angle4 = detector.findAngle(img, 31, 27, 25, False)
        angle5 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <102 or angle1>106:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <174 or angle2 >178:
            angle2 = detector.findAngle(img, 25, 23, 11)
        if angle3 <169 or angle3>173:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <105 or angle4>109:
            angle4 = detector.findAngle(img, 31, 27, 25)
        if angle5 <5 or angle5>15:            
            angle5 = detector.findAngle(img, 23, 11, 13)
        pass
    def yoga_inter_aasana5(img,detector):
        angle1 = detector.findAngle(img, 16, 14, 12, False)
        angle2 = detector.findAngle(img, 24, 12, 14, False)
        angle3 = detector.findAngle(img, 26, 24, 12, False)
        angle4 = detector.findAngle(img, 24, 26, 28, False)
        
        if angle1 <160 or angle1>181:            
            angle1 = detector.findAngle(img,  16, 14, 12)
        if angle2 <40 or angle2 >70:
            angle2 = detector.findAngle(img,  24, 12, 14)
        if angle3 <160 or angle3>181:            
            angle3 = detector.findAngle(img, 26, 24, 12)
        if angle4 <160 or angle4>181:
            angle4 = detector.findAngle(img, 24, 26, 28)
            
            
    def yoga_inter_aasana6(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 24, 26, 28, False)
        angle4 = detector.findAngle(img, 26, 24, 12, False)
        if angle1 <164 or angle1>168:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <140 or angle2 >160:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <160 or angle3>180:            
            angle3 = detector.findAngle(img, 24, 26, 28)
        if angle4 <70 or angle4>90:
            angle4 = detector.findAngle(img, 26, 24, 12)
            
            
        
    def yoga_inter_aasana7(img,detector):
        angle1 = detector.findAngle(img, 27, 25, 23)
        angle2 = detector.findAngle(img, 24, 26, 28)
        if angle1 <15 or angle1>25:
            angle1 = detector.findAngle(img,  23, 25, 27)
        if angle2 <15 or angle2 >25:
            angle2 = detector.findAngle(img, 28, 26, 24)
        pass
    def yoga_inter_aasana8(img,detector):
        
        angle1 = detector.findAngle(img, 24, 26, 28, False)
        angle2 = detector.findAngle(img, 11, 13, 15, False)
        angle3 = detector.findAngle(img, 13, 11, 23, False)
        angle4 = detector.findAngle(img, 24, 12, 14, False)
        
       
        if angle1 <170 or angle1 >180:
            angle1 = detector.findAngle(img,  24, 26, 28)
        if angle2 <165 or angle2>185:            
            angle2 = detector.findAngle(img, 11, 13, 15)
        if angle3 <100 or angle3>130:            
            angle3 = detector.findAngle(img, 13, 11, 23)
        if angle4 <45 or angle4>75:
            angle4 = detector.findAngle(img, 24, 12, 14)
        
       
    def yoga_inter_aasana9(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 24, 26, 28, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        angle5 = detector.findAngle(img, 25, 23, 11, False)
       
        if angle1 <166 or angle1>170:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <166 or angle2 >170:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <168 or angle3>172:            
            angle3 = detector.findAngle(img, 24, 26, 28)
        if angle4 <166 or angle4>170:
            angle4 = detector.findAngle(img, 23, 11, 13)
        if angle5 <88 or angle5>92:            
            angle5 = detector.findAngle(img, 25, 23, 11)
        
    
    def yoga_inter_aasana10(img,detector):
        angle1 = detector.findAngle(img, 12, 14, 16, False)
        angle2 = detector.findAngle(img, 24, 12, 14, False)
        angle3 = detector.findAngle(img, 26, 24, 12, False)
        angle4 = detector.findAngle(img, 28, 26, 24, False)
        if angle1 <165 or angle1>187:            
            angle1 = detector.findAngle(img, 12, 14, 16)
        if angle2 <22 or angle2 >45:
            angle2 = detector.findAngle(img, 24, 12, 14)
        if angle3 <165 or angle3>187:            
            angle3 = detector.findAngle(img,26, 24, 12)
        if angle4 <60 or angle4>80:
            angle4 = detector.findAngle(img, 28, 26, 24)
            
   #****************************************************************************************************** 
        
    def yoga_adv_aasana1(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 13, 11, 23, False)
        if angle1 <57 or angle1>63:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <145 or angle2 >156:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <142 or angle3>158:            
            angle3 = detector.findAngle(img,25, 23, 11)
        if angle4 <78 or angle4>98:
            angle4 = detector.findAngle(img, 13, 11, 23)
        
    def yoga_adv_aasana2(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 13, 11, 23, False)
        if angle1 <57 or angle1>63:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <145 or angle2 >156:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <142 or angle3>158:            
            angle3 = detector.findAngle(img,25, 23, 11)
        if angle4 <78 or angle4>98:
            angle4 = detector.findAngle(img, 13, 11, 23)
    
    def yoga_adv_aasana3(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <133 or angle1>143:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <162 or angle2 >180:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <7 or angle3>30:            
            angle3 = detector.findAngle(img,25, 23, 11)
        if angle4 <120 or angle4>128:
            angle4 = detector.findAngle(img, 23, 11, 13)
            
    def yoga_adv_aasana4(img,detector):
        angle1 = detector.findAngle(img, 11, 13, 15, False)
        angle2 = detector.findAngle(img, 27, 25, 23, False)
        angle3 = detector.findAngle(img, 12, 24, 26, False)
        angle4 = detector.findAngle(img, 14, 12, 24, False)
        if angle1 <174 or angle1>182:            
            angle1 = detector.findAngle(img, 11, 13, 15)
        if angle2 <118 or angle2 >126:
            angle2 = detector.findAngle(img,  27, 25, 23)
        if angle3 <72 or angle3>92:            
            angle3 = detector.findAngle(img, 12, 24, 26)
        if angle4 <32 or angle4>40:
            angle4 = detector.findAngle(img, 14, 12, 24)
        
    def yoga_adv_aasana5(img,detector):
        angle1 = detector.findAngle(img, 12, 14, 16, False)
        angle2 = detector.findAngle(img, 28, 26, 24, False)
        angle3 = detector.findAngle(img, 26, 24, 12, False)
        angle4 = detector.findAngle(img, 24, 12, 14, False)
        angle5 = detector.findAngle(img, 14, 18, 26, False)
        if angle1 <163 or angle1>171:            
            angle1 = detector.findAngle(img, 16, 14, 12)
        if angle2 <163 or angle2 >171:
            angle2 = detector.findAngle(img, 11, 13, 15)
        if angle3 <155 or angle3>167:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <52 or angle4>72:
            angle4 = detector.findAngle(img, 11, 23, 25)
        if angle5 <95 or angle5>107:
            angle5 = detector.findAngle(img, 13, 11, 23)
        
        
        
        
    def yoga_adv_aasana6(img,detector):
        angle1 = detector.findAngle(img, 16, 14, 12, False)
        angle2 = detector.findAngle(img, 11, 13, 15, False)
        angle3 = detector.findAngle(img, 23, 25, 27, False)
        angle4 = detector.findAngle(img, 11, 23, 25, False)
        angle5 = detector.findAngle(img, 13, 11, 23, False)
        if angle1 <163 or angle1>171:            
            angle1 = detector.findAngle(img, 16, 14, 12)
        if angle2 <163 or angle2 >171:
            angle2 = detector.findAngle(img, 11, 13, 15)
        if angle3 <155 or angle3>167:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <52 or angle4>72:
            angle4 = detector.findAngle(img, 11, 23, 25)
        if angle5 <95 or angle5>107:
            angle5 = detector.findAngle(img, 13, 11, 23)
        
    def yoga_adv_aasana7(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 11, 23, 25, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <113 or angle1>133:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <164 or angle2 >184:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <170 or angle3>190:            
            angle3 = detector.findAngle(img, 11, 23, 25)
        if angle4 <5 or angle4>25:
            angle4 = detector.findAngle(img, 23, 11, 13)
        
        
    def yoga_adv_aasana8(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 11, 23, 25, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <37 or angle1>67:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <166 or angle2 >190:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <162 or angle3>186:            
            angle3 = detector.findAngle(img, 11, 23, 25)
        if angle4 <108 or angle4>132:
            angle4 = detector.findAngle(img, 23, 11, 13)
        
    def yoga_adv_aasana9(img,detector):
        angle1 = detector.findAngle(img, 16, 14, 12, False)
        angle2 = detector.findAngle(img, 28, 26, 24, False)
        angle3 = detector.findAngle(img, 26, 24, 12, False)
        angle4 = detector.findAngle(img, 24, 12, 14, False)
        angle5 = detector.findAngle(img, 27, 25, 23, False)
        if angle1 <142 or angle1>158:            
            angle1 = detector.findAngle(img, 16, 14, 12)
        if angle2 <154 or angle2 >170:
            angle2 = detector.findAngle(img, 28, 26, 24)
        if angle3 <161 or angle3>181:            
            angle3 = detector.findAngle(img, 26, 24, 12)
        if angle4 <56 or angle4>76:
            angle4 = detector.findAngle(img, 24, 12, 14)
        if angle5 <36 or angle5>50:
            angle5 = detector.findAngle(img, 27, 25, 23)
        
        
    def yoga_adv_aasana10(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 24, 26, 28, False)
        angle3 = detector.findAngle(img, 23, 25, 27, False)
        angle4 = detector.findAngle(img, 11, 23, 25, False)
        
        if angle1 <61 or angle1>91:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <133 or angle2 >167:
            angle2 = detector.findAngle(img, 24, 26, 28)
        if angle3 <73 or angle3>113:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <70 or angle4>100:
            angle4 = detector.findAngle(img, 11, 23, 25)
            
         
   #****************************************************************************************************** 

    
    def lifting_curls_biceps(img,detector):
        x,y,z=15,13,11
        #left arm
        angle = detector.findAngle(img, x, y, z)
        #right arm
        #angle = detector.findAngle(img, 12, 14, 16)
        #per = np.interp(angle, (210, 310), (0, 100))
        per = np.interp(angle, (150, 50), (0, 100))
        
        
        return per
    def lifting_curls_biceps(img,detector):
        x,y,z=15,13,11
        #left arm
        angle = detector.findAngle(img, x, y, z)
        #right arm
        #angle = detector.findAngle(img, 12, 14, 16)
        #per = np.interp(angle, (210, 310), (0, 100))
        per = np.interp(angle, (150, 50), (0, 100))
        return per
    def lifting_floor_press(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_bentover_dumbbell(img,detector):
        x,y,z=15,13,11
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (150, 75), (0, 100))
        return per
        
    def lifting_forearms(img,detector):  
        #x,y,z=15,13,11
        #left arm
        #angle = detector.findAngle(img, x, y, z)
        #right arm
        angle = detector.findAngle(img, 22, 16, 14)
        #per = np.interp(angle, (210, 310), (0, 100))
        per = np.interp(angle, (192, 184), (0, 100))
        return per
        
    def lifting_dumbell_squats(img,detector):
        x,y,z=23,25,27
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (182, 300), (0, 100))
        return per
        
    def lifting_shoulder_press(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_tricep_overhead_left(img,detector): 
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_ex8(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_ex9(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_ex10(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
             
   #****************************************************************************************************** 
    
    def calisthenics_pushup(img,detector):
        x,y,z=12,14,16
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (160,100 ), (0, 100))
        return per
    def calisthenics_pullup(img,detector):
        x,y,z=14,12,24
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (150, 60), (0, 100))
        return per
    def calisthenics_squats(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (230, 250), (0, 100))
        return per
    def calisthenics_benchdips(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (30, 90), (0, 100))
        return per
    def calisthenics_crunches(img,detector):
        x,y,z=25,23,11
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (120, 40), (0, 100))
        return per
    
             
   #****************************************************************************************************** 
   