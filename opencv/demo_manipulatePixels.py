import cv2
#manipulating pixels
image = cv2.imread("lena.jpg",1)
image[100,100] =(255,255,255)
print(image[100,100])
cv2.imshow('image',image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#size of the image
print(image.shape)

