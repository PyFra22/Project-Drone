import cv2
import datetime
import time 

cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()
    
    cv2.imshow("Camera", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()