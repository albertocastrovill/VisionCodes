import cv2


cap = cv2.VideoCapture(0)


ret, frame = cap.read()
cv2.imwrite("Foto1.jpg", frame)
    

cap.release()
cv2.destroyAllWindows()