import numpy as np
import cv2
image = cv2.imread('blue.jpg',1)

#object tracking

new_image= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('image',new_image)


low_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(new_image,low_blue,upper_blue)
cv2.imshow('mask',mask)

res =cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('res',res)

blue = np.uint8([[[255,0,0]]])
hsv_blue= cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
print(hsv_blue)
cv2.waitKey(10000)
cv2.destroyAllWindows()