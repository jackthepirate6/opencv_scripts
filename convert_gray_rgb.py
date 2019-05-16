import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
while(cap.isOpened()):

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    cv2.imshow('test', gray)

    if cv2.waitKey(1) & 0xFF == ord('p') :
        break

cap.release()
cv2.destroyAllWindows()
