import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import cv2

#COLOR
image  = cv2.imread('carretera.jpeg')
cv2.imshow('Carretera', image)

#GRAY
#gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray', gray_img)

heigth, width = image.shape[:2]
print(heigth, width)

#Rotations
#cv2.getRotationMatrix2D(center_of_rotation, angle, scale)
M_rotation = cv2.getRotationMatrix2D((width/2, heigth/2), 30, 0.6)

#cv2.warpAffine(imagen, M_rotation, size)
rotated_image = cv2.warpAffine(image, M_rotation, (width,heigth))
cv2.imshow('Rotated Image',rotated_image)

#Final
cv2.waitKey(0)
cv2.destroyAllWindows()