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

#Sharpening Kernel
sharp_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharpered_image = cv2.filter2D(gray_img, -1, sharp_kernel)
cv2.imshow('Sharpered Image', sharpered_image)

#Blurring Kernel Normalized
blurr_kernel = np.ones((6,6))*1/36
blurred_image = cv2.filter2D(gray_img, -1, blurr_kernel)
cv2. imshow('Blurred Image', blurred_image)

#Final
cv2.waitKey(0)
cv2.destroyAllWindows()