import cv2
import numpy as np

img = cv2.imread('../resources/lena.jpg')

# Applying arbitrary kernels
kernel_averaging_5_5 = np.ones((5, 5), np.float32) / 25
dst_img = cv2.filter2D(img, ddepth=-1, kernel=kernel_averaging_5_5)

# avg blur
imgAvgBlur = cv2.blur(img,ksize=(10,10))
imgAvgBlur2 = cv2.boxFilter(img, ddepth=-1, ksize=(10,10), normalize=True)

# gaussian blur
imgGauBlur = cv2.GaussianBlur(img, (9,9), 1)

# median blur
imgMedianBlur = cv2.medianBlur(img, ksize=5)

# Bilateral
imgBilateral = cv2.bilateralFilter(img, d = 5, sigmaColor=10, sigmaSpace=10)

cv2.imshow('original', img)
cv2.imshow('out', dst_img)
cv2.imshow('imgAvgBlur', imgAvgBlur)
cv2.imshow('imgAvgBlur2', imgAvgBlur2)
cv2.imshow('imgGauBlur', imgGauBlur)
cv2.imshow('imgMedianBlur', imgMedianBlur)
cv2.imshow('imgBilateral', imgBilateral)
cv2.waitKey()

