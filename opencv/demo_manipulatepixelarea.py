import cv2
image = cv2.imread('D:\inligntech\opencv\lena.jpg',1)
a= image[0:100,0:100]
image[100:200,100:200] = a

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()