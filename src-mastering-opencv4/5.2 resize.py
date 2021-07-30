import cv2
import numpy as np

img = cv2.imread('../resources/lena.jpg')

w,h = img.shape[1], img.shape[0]
img1 = cv2.resize(img, dsize=(w*2, h*2), interpolation=cv2.INTER_LINEAR)
cv2.imshow('dsize linear',img1)

img2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('fx-fy cubic',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()