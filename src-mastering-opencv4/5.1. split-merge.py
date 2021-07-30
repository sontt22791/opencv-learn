import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../resources/lena.jpg')
print(img.shape)
cv2.imshow('out', img)

b, g, r = cv2.split(img)
print(b.shape, g.shape, r.shape)
img2 = cv2.merge(mv=(r, g, b))
cv2.imshow('out2', img2)

img3 = np.swapaxes(img, axis1=0, axis2=2)
print(img3.shape)

img4 = img.copy()
# img4[..., 2], img4[..., 0] = img4[..., 0], img4[..., 2] # sai
# img4[..., [0,1,2]] = img4[..., [2,1,0]]
img4[..., 2], img4[..., 0] = img[..., 0], img[..., 2] # fai la img[..], neu nhu line 18 thi no se update truc tiep vao array img4 va se sai

print(img4.shape)

print(img[...,2].shape)

cv2.imshow('out4', img4)
# plt.imshow(img)
# plt.imshow(img2)
plt.show()

cv2.waitKey(0)
