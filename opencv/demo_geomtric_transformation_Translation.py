#geometric transformation of images
#scaling - make bigger or smaller cv.reize
#def resize(src: Mat | ndarray[Any, dtype],
#           dsize: Sequence[int] | None,
#           dst: Mat | ndarray[Any, dtype] | None = ...,
#           fx: float = ...,
#           fy: float = ...,
#           interpolation: int = ...) -> Mat | ndarray[Any, dtype]
# interpolation - cv2.linear
#Translation - shifting the image
#def warpAffine(src: Mat | ndarray[Any, dtype],
#               M: Mat | ndarray[Any, dtype],
#               dsize: Sequence[int],
#               dst: Mat | ndarray[Any, dtype] | None = ...,
#               flags: int = ...,
#               borderMode: int = ...,
#               borderValue: Sequence[float] = ...) -> Mat | ndarray[Any, dtype]

#Rotation - at a specific angle
#scaled rotation with adjustable center
# rotating image with center as reference point

import cv2
import numpy as np
matrix = np.float32([[1,0,100],[0,1,100]])
image = cv2.imread('lena.jpg',0)
rows,cols = image.shape
new_image = cv2.warpAffine(image,matrix,(rows,cols))
cv2.imshow('image',image)
cv2.imshow('image1',new_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()