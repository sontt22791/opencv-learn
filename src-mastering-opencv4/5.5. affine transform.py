import cv2
import matplotlib.pyplot as plt
import numpy as np



img = cv2.imread('../resources/lena.jpg')
height, width = img.shape[:2]

pts_1 = np.float32([[135, 45], [385, 45], [135, 230]])
pts_2 = np.float32([[135, 45], [385, 45], [200, 230]])
print(pts_1.shape)
print(pts_2.shape)
M = cv2.getAffineTransform(pts_1, pts_2)
dst_image = cv2.warpAffine(img, M, (width, height))

# cv2.imshow('out',dst_image)
# cv2.waitKey(0)
plt.imshow(dst_image)
plt.show()