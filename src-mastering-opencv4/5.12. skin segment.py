import cv2
import numpy as np

img = cv2.imread('../resources/skin_test_imgs/test3.jpg')

imgHSV = cv2.cvtColor(img, code=cv2.COLOR_BGR2HSV)

# range nay copy trong file https://github.com/PacktPublishing/Mastering-OpenCV-4-with-Python/blob/master/Chapter05/01-chapter-content/skin_segmentation.py
# lower_hsv_2 = np.array([0, 50, 0], dtype="uint8")
# upper_hsv_2 = np.array([120, 150, 255], dtype="uint8")

lower_hsv = np.array([0, 48, 80], dtype="uint8")
upper_hsv = np.array([20, 255, 255], dtype="uint8")

skin_region = cv2.inRange(imgHSV,lowerb=lower_hsv, upperb=upper_hsv)
print(skin_region.shape)

split = cv2.bitwise_and(img, img, mask=skin_region)

cv2.imshow('org', img)
cv2.imshow('out', imgHSV)
cv2.imshow('out2', skin_region)
cv2.imshow('split', split)
cv2.waitKey(0)