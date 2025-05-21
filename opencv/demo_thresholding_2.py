#adaptive thresholding
import cv2
import numpy as np
#Simple thresholding 1 value for entire image
#adaptive mean , adaptive gaussian , global thresholding
#cv2.adaptivethreshold-> blocksize
#method  mean, threshold
#block size = neighborhood area
#constant - to be subtracted from mean
#mutiple thresholding values for different sections of an image

image = cv2.imread('sample.jpg',0)
ret,thresh = cv2.threshold(image,80,255,cv2.THRESH_BINARY)

cv2.imshow('image1',image)
cv2.imshow('image2',thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()

image = cv2.imread('sample.jpg',0)
thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,10)

cv2.imshow('image3',image)
cv2.imshow('image4',thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()

image = cv2.imread('sample.jpg',0)
thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)

cv2.imshow('image5',image)
cv2.imshow('image6',thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()