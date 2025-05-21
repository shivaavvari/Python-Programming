#image thresholding
#convert greyscale image to binary image.
#parameters
#convert image to grayscale image
#threshold value -> arbitrary value
# maxvalue - applied to image if exceeds thresholding values
#threshold method



import cv2
import numpy as np

image = cv2.imread('gradient.png',0)
ret,thresh = cv2.threshold(image,80,255,cv2.THRESH_BINARY)

cv2.imshow('image',image)
cv2.imshow('image2',thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()