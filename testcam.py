import cv2
import datetime
import time 

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fulbody.xml")

# recording = True 

while True:
    
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    _, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facePart = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # for(x, y, width, height) in facePart:
    #     cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 0), 3)
    
    for (x, y, w, h) in facePart:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        text = f'x={x}, y={y}' 
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)
        cv2.putText(frame, current_time, (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

    
    cv2.imshow("Camera", frame)
    
    if cv2.waitKey(1) == ord('q') or cv2.waitKey(2) == ord('Q'):
        break
    
cap.release()
cv2.destroyAllWindows()