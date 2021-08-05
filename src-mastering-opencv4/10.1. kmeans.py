import cv2
import numpy as np

img = cv2.imread('../resources/Photos/lady.jpg')

data = img.astype(np.float32).reshape(-1,3)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
# a = np.array([1,2,3])
ret, label, center = cv2.kmeans(data, K = 3, bestLabels=None, criteria=criteria, attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)
center = center.astype(np.uint8)

print(label.shape)
print(ret)
print(center.shape)
print(center)

print(np.unique(label))

result = center[label.flatten()]
result = result.reshape(img.shape)

cv2.imshow('1', img)
cv2.imshow('2', result)
cv2.waitKey()