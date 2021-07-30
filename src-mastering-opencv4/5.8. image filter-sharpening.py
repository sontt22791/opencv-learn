import cv2
import numpy as np

img = cv2.imread('../resources/Photos/lady.jpg')

# avg blur
blur = cv2.GaussianBlur(img, ksize=(9, 9), sigmaX=0)
img2 = cv2.addWeighted(img, alpha=1.5, src2=blur, beta=-0.5, gamma=0)

cv2.imshow('original', img)
cv2.imshow('imgAvgBlur', img2)
cv2.waitKey()
