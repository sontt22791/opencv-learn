import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../resources/lena.jpg')
# height, width = img.shape[:2]

pts_1 = np.float32([[38, 26], [161, 24], [32, 172],[175,183]])
pts_2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
print(pts_1.shape)
print(pts_2.shape)
M = cv2.getPerspectiveTransform(pts_1, pts_2)
dst_image = cv2.warpPerspective(img, M, (300, 300))

# cv2.imshow('out',dst_image)
# cv2.waitKey(0)
cv2.imshow('origin', img)
cv2.imshow('out',dst_image)
# plt.show()

cv2.waitKey(0)