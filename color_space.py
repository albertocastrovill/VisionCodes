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

#HSV
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv_img)

#Split Image
B,G,R = cv2.split(image)
print(B.shape)
#cv2.imshow('Blue Channel', B)  #La imagen sale en escala de grises porque OpenCV intepreta que esta en grises por ser solo un canal

#3D image out of the blue channel
zeros = np.zeros(image.shape[:2], dtype = 'uint8')
cv2.imshow("Blue Channel", cv2.merge([B, zeros, zeros]))

#Re-merged image
image_merge = cv2.merge([B, G, R])
cv2.imshow("Image Merge",image_merge)

#COLOR PLT
plt.imshow(image)
plt.show()

#Final
cv2.waitKey(0)
cv2.destroyAllWindows()