import cv2
import numpy as np

img = cv2.imread('../resources/Photos/lady.jpg')

# print(img[:10])
img2 = img + 60
# print(img[:10])
img2_ = img2 % 256
img2 = np.where(img2 > 255, img2_, img2)
img2 = np.where(img2 < 0, 0, img2)
print(img2)

img3 = cv2.add(img, np.ones(img.shape, dtype=np.uint8) * 110)
cv2.imshow('out2', img2)
cv2.imshow('out3', img3)

img4 = cv2.imread('../resources/Photos/park.jpg')
img5 = cv2.subtract(img, cv2.resize(img4//2, dsize=(img.shape[1], img.shape[0])))

cv2.imshow('out5', img5)
cv2.waitKey()
