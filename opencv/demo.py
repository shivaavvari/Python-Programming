import cv2
#1 color
#0 blackwhite

image = cv2.imread('lena.jpg',0)
cv2.imshow('image',image)
cv2.waitKey(10000)
cv2.imwrite('lena.png',image)
cv2.destroyAllWindows()

