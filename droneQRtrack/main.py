import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

myKey = "MyKey12345"

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        if myData == myKey:
            x, y, w, h = barcode.rect
            if x + w/2 < 300:
                print("Going Left")
            elif x + w/2 > 340:
                print("Going Right")
            elif y + h/2 < 220:
                print("Moving Forward")
            elif y + h/2 > 260:
                print("Moving Back")
            else:
                print("Stationary")
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,255),5)
            pts2 = barcode.rect
            cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)
    print("Stationary")
    cv2.imshow('Result',img)
    cv2.waitKey(1)