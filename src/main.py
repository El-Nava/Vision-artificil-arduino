import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector=HandDetector(detectionCon=0.8,maxHands=1)

video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    frame=cv2.flip(frame,1)
    hands,img=detector.findHands(frame)
    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)

        print(fingerUp)
        cnt.led(fingerUp)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Dedos Levantados: 0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,'Dedos Levantados: 1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1,cv2.LINE_AA)    
        elif fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'Dedos Levantados: 2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,165,0),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'Dedos Levantados: 3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'Dedos Levantados: 4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(128,255,0),1,cv2.LINE_AA)
        elif fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Dedos Levantados: 5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1,cv2.LINE_AA) 

    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==ord("q"):
        break

video.release()
cv2.destroyAllWindows()
