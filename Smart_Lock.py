import cv2
import numpy as np 
import face_recognition
import os 
from datetime import datetime
from gpiozero import LED
from time import sleep

def map_range(value, from_min, from_max, to_min, to_max):
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

Angle = 90
pulse_width = map_range(Angle, 0, 180, 400, 2400)
delay = pulse_width / 1000000

servo = LED(4)

path = 'Database'
images = []
class_names = []
my_list = os.listdir(path)

targeted_name =["Ahmed_Saber"] # The targeted name.

for cl in my_list:
    curimg =cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    class_names.append(os.path.splitext(cl)[0])

def Encoder(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encode_list_known = Encoder(images)
print(len(encode_list_known))   
cap = cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
    face_current_frame = face_recognition.face_locations(imgs)
    encodes_curr_frame = face_recognition.face_encodings(imgs,face_current_frame)

    for encode_face, face_locin in  zip(encodes_curr_frame, face_current_frame):
        matches = face_recognition.compare_faces(encode_list_known,encode_face)
        face_distance = face_recognition.face_distance(encode_list_known,encode_face)
        print(face_distance)
        match_index = np.argmin(face_distance)
        y1,x2,y2,x1 = face_locin
        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)


# open the door if right targeted image detected
        if matches[match_index]:
            name = class_names[match_index]
            if name in targeted_name:
                
                print(name)
                
                servo.on()
                sleep(delay)
                servo.off()

                y1,x2,y2,x1 = face_locin
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)          
        else:
                servo.on()
                sleep(0.0005)
                servo.off()
                

                
        
    cv2.imshow('ori_image',img)
    cv2.waitKey(1)
