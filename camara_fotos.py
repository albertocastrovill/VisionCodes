import cv2
import matplotlib.pyplot as plt 

i = 1
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Web Cam Video', frame)
    
    if cv2.waitKey(1) == 13: #13 Enter key
        cv2.imwrite("Foto" + i + ".jpg", frame)
        i = i+1

    if cv2.waitKey(1) == 32: #12 spacebar key
        break

cap.release()
cv2.destroyAllWindows()

