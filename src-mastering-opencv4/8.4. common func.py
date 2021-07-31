import cv2
import numpy as np

import constant

img = cv2.imread('../resources/shape_features.png')
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
_,thres = cv2.threshold(gray,thresh=50, maxval=255, type=cv2.THRESH_BINARY)

cts, hie = cv2.findContours(thres, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)

x,y,w,h = cv2.boundingRect(cts[0])
cv2.rectangle(img, pt1=(x,y), pt2=(x+w, y+h), color=(0,0,255), thickness=3)

rotated_rect = cv2.minAreaRect(cts[0])
print(f'rotated_rect : {rotated_rect}')
box = cv2.boxPoints(box = rotated_rect)
print(f'box : {box}')
box = np.int0(box)
cv2.polylines(img, pts=[box], isClosed=True,color=constant.GREEN, thickness=3 ) # vẽ hình khi biết 4 góc (giá trị 4 góc fai là int)


print(cv2.minEnclosingCircle(points=cts[0]))
(x,y), radius = cv2.minEnclosingCircle(points=cts[0])
cv2.circle(img, center=(int(x),int(y)), radius=int(radius), color=constant.WHITE, thickness=3)

ellipse = cv2.fitEllipse(cts[0])
cv2.ellipse(img, ellipse, constant.YELLOW, 5)

print(cv2.minEnclosingTriangle(cts[0]))

cv2.imshow('out', img)
cv2.waitKey()