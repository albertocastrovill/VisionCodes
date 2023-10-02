#import the required libraries 
import numpy as np 
import matplotlib.image as img
import matplotlib.pyplot as plt 
import cv2 

image_colour = img.imread('PistaRC.jpg') 
plt.imshow(image_colour)
plt.xticks([]), plt.yticks([])
print(image_colour.shape)

#converting image to Gray scale 
#gray_image = cv2.cvtColor(image_colour,cv2.COLOR_BGR2GRAY)
#plotting the grayscale image
#plt.imshow(gray_image, cmap='gray') 
#cv2.imwrite("image_lane_g.jpg", gray_image)


plt.show()