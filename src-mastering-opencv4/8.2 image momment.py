import cv2
import numpy as np
import constant

img = np.zeros(shape=(500,500,3), dtype=np.uint8)
print(img.shape)
cv2.rectangle(img, pt1=(100,100), pt2=(300,300),color=constant.RED, thickness=-1)
cv2.rectangle(img, (150, 150), (250, 250), (70, 70, 70), -1)
print(img.shape)
imggray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
print(imggray.shape)
_,imgthres = cv2.threshold(imggray, thresh=75, maxval=255, type=cv2.THRESH_BINARY)
print(imgthres.shape)


c, h = cv2.findContours(image=imgthres,mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
print(h)
print(len(c))

for i in c:
    cv2.drawContours(img, contours=[i], contourIdx=0, color=constant.WHITE,thickness=3)
    m = cv2.moments(array=i)
    print(m)


cv2.imshow('out', img)
cv2.imshow('out2', imgthres)

cv2.waitKey()