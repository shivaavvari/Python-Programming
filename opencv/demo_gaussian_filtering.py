import cv2
#Gaussian filtering
image = cv2.imread('train.jpeg',1)
gaussian_blur=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('image',image)
cv2.imshow('blur',gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()