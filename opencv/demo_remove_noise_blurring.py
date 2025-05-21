#filter image to remove noise and blurring
#images filtered by lowpass filter(remove noise) , high passfilter (find edges)
#cv2.filter2D ->image , ddepth=1-:same depth  , kernel
#blurring
import cv2
import numpy as np


image = cv2.imread('train.jpeg',1)
matrix = np.ones((5,5),dtype=np.float32)/25
new_image = cv2.filter2D(image,-1,matrix)

cv2.imshow('image',image)

cv2.imshow('image1',new_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()


