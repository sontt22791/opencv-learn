import cv2
import numpy as np

img = cv2.imread('resources/Photos/cat.jpg', flags=cv2.IMREAD_GRAYSCALE)
print(img.shape)

cv2.imshow('out', img)

cv2.waitKey(0)