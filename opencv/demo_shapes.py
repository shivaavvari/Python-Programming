import cv2
#how to draw shapes on images

image = cv2.imread('lena.jpg',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(0,0),(400,400),(0,255,0),5)
cv2.circle(image,(250,250),100,(0,0,255),-1)
cv2.putText(image,"Hello  Mountains",(100,100),
            cv2.FONT_ITALIC,2,(255,255,255),cv2.LINE_AA)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()



