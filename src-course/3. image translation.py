# translation, rotation, crop, resize, flip

import cv2
import numpy as np
import stackimages

img = cv2.imread('../resources/Photos/park.jpg')
(h,w) = img.shape[:2]

# translation
x = 100
y = 100
tranMat = np.array([[1,0,x], [0,1,y]], dtype=np.float32) # chú ý fai set np.float32
img_translation = cv2.warpAffine(img,M = tranMat, dsize=(w,h))

# rotation
rotMat = cv2.getRotationMatrix2D(center=(w//2, h//2), angle=45, scale=1)
img_rotated = cv2.warpAffine(img, M = rotMat, dsize=(w,h))

imgstack = stackimages.ManyImgs(scale=1, imgarray=[[img, img_translation, img_rotated]])
cv2.imshow('out', imgstack)
cv2.waitKey()