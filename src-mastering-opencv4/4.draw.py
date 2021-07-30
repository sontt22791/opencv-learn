import cv2
import matplotlib.pyplot as plt
import numpy as np
import constant

img = np.zeros(shape=(500, 500, 3), dtype=np.uint8)
# cv2.imshow('out', img)
# imgRed = img.copy()
# print(imgRed.shape)
# print(imgRed[:].shape)
img[:] = constant.GRAY
# cv2.imshow('out gray', img)


img = cv2.line(img, pt1=(0, 0), pt2=(img.shape[1], img.shape[0]), color=constant.GREEN, thickness=3)
# cv2.imshow("out line", img)

img = cv2.rectangle(img, pt1=(0, 0), pt2=(200, 200), color=constant.RED, thickness=3)

img = cv2.putText(img,"hello opencv",org=(300,300), fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1, color=constant.GREEN, thickness=3)
cv2.imshow('output', img)
cv2.waitKey(0)
