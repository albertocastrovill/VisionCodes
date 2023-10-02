import numpy as np 
import matplotlib.image as img
import matplotlib.pyplot as plt 
import cv2 

image_colour = img.imread('carretera.jpeg')
print(image_colour.shape)

image_copy = np.copy(image_colour)
print(image_copy.shape)

image_copy[ (image_copy[:,:,0]<200) | (image_copy[:,:,1]<200) | (image_copy[:,:,2]<200)] = 0

plt.imshow(image_copy, cmap='gray')
plt.xticks([]), plt.yticks([])

cv2.imwrite("white_image.jpg", image_copy)

plt.show()