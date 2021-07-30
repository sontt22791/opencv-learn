import cv2
import numpy as np
import constant
import stackimages

img = np.ones(shape=(500,500,3), dtype=np.uint8)
cv2.rectangle(img, (100,100), (300,300), color=constant.RED, thickness=-1)
cv2.rectangle(img, (150, 150), (250, 250), (70, 70, 70), -1)
cv2.circle(img, (400,400), radius=100, color=constant.CYAN, thickness=-1)
cv2.circle(img, (400, 400), 50, (70, 70, 70), -1)

imgGray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
_, imgThres75 = cv2.threshold(imgGray, thresh=75, maxval=255, type=cv2.THRESH_BINARY)
_, imgThres100 = cv2.threshold(imgGray, thresh=100, maxval=255, type=cv2.THRESH_BINARY) # thresh 100 ko detect dc binary hinh vuong

contours, hierarchy = cv2.findContours(image=imgThres75, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(image=img, contours=contours, contourIdx=0, color=constant.WHITE, thickness=3)
for c in contours:
    print('contour shape', c.shape)
    cv2.drawContours(image=img, contours=[c], contourIdx=0, color=constant.WHITE, thickness=3)


print(len(contours))
print(hierarchy)
print(hierarchy.shape)

imgStack = stackimages.ManyImgs(scale=0.75, imgarray=[[imgGray, imgThres75, img, imgThres100]])
cv2.imshow('out', imgStack)
cv2.waitKey()
