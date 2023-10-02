import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np
import cv2

#COLOR
image  = cv2.imread('carretera.jpeg')
cv2.imshow('Carretera', image)

#GRAY
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray_img)

# Sobel Caluculations
x_sobel = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=7)
cv2.imshow('Sobel - X direction', x_sobel)
y_sobel = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=7)
cv2.imshow('Sobel - Y direction', y_sobel)

# Lapacian
laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)

#Canny
#threshold1 - first threshold for the hysteresis preocedure
#threshold2 - second threshold for the hysteresis preocedure
threshold_1 = 200
threshold_2 = 500

canny = cv2.Canny(gray_img, threshold_1, threshold_2)
cv2.imshow('Canny' , canny)

#Final
cv2.waitKey(0)
cv2.destroyAllWindows()