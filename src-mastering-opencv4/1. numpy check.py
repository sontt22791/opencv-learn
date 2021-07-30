import cv2
import numpy as np

img = cv2.imread('../resources/Photos/cat.jpg')

print(img.shape)
print(img[6, 40].shape)
print(img[6, 40])
print(img[6, 40, 0])
print(img[:].shape)

img[:] = 0, 0, 0
# cv2.imshow("out", img)
# cv2.waitKey(0)

arr = np.ones(shape=(2, 4), dtype=np.uint8)
print(arr[:].shape)
arr[:] = 1, 1, 1, 1
print(arr)

arr2 = np.arange(24)
arr2 = arr2.reshape((2, 4, 3))
print(arr2)

print(arr2[..., 2])
print(arr2[..., 0])
arr2[..., 2], arr2[..., 0] = arr2[..., 0], arr2[..., 2]
print(arr2)

arr2 = np.arange(24).reshape((2, 4, 3))
x1, x2, x3 = arr2[:, :, 0], arr2[:, :, 1], arr2[:, :, 2]

arr2[:,:, 0] = x3
arr2[:,:, 2] = x1
print(arr2)
