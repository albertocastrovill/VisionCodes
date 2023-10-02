import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import cv2

def LiveCamEdgeDetection_Canny(image_color):
    th1 = 100
    th2 = 150
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(image_gray, th1, th2)

    return canny

def LiveCamEdgeDetection_Laplace(image_color):
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(image_gray, cv2.CV_64F)

    return laplacian

def LiveCamEdgeDetection_Sobel(image_color):
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    x_sobel = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=7)
    cv2.imshow('Sobel - X direction', x_sobel)
    y_sobel = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=7)
    cv2.imshow('Sobel - Y direction', y_sobel)

    return x_sobel, y_sobel


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Live Edge Detection', LiveCamEdgeDetection_Canny(frame))
    cv2.imshow('Web Cam Video', frame)
    if cv2.waitKey(1) == 13: #13 Enter key
        break

cap.release()
cv2.destroyAllWindows()