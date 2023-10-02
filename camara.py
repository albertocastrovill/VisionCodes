import cv2
import matplotlib.pyplot as plt 


cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv2.imshow('Web Cam Video', frame)
    
    if cv2.waitKey(1) == 13: #13 Enter key
        break

cap.release()
cv2.destroyAllWindows()