import cv2
#blurring Averaging
image = cv2.imread('train.jpeg',1)
blur=cv2.blur(image,(5,5),)
cv2.imshow('image',image)
cv2.imshow('image1',blur)
cv2.waitKey(10000)
cv2.destroyAllWindows()