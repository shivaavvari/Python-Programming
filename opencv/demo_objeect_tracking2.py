import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _,frame= cap.read()

    # object tracking

    new_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('image', new_image)

    low_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(new_image, low_blue, upper_blue)
    #cv2.imshow('mask', mask)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('res', res)
    k= cv2.waitKey(5) & 0xff
    if k==27:
        break
cv2.waitKey(10000)
cv2.destroyAllWindows()
