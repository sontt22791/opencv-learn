import cv2
import numpy as np
import stackimages

img1 = cv2.imread('../resources/morpho_test_imgs/test1.png')
img2 = cv2.imread('../resources/morpho_test_imgs/test2.png')
img3 = cv2.imread('../resources/morpho_test_imgs/test3.png')

# img1 = cv2.resize(img1, None, fx=0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)
# img2 = cv2.resize(img2, None, fx=0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)
# img3 = cv2.resize(img3, None, fx=0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)

k = cv2.getStructuringElement(shape= cv2.MORPH_ELLIPSE, ksize=(3,3))
dilation1 = cv2.dilate(img1, kernel=k, iterations=1)
dilation2 = cv2.dilate(img2, kernel=k, iterations=1)
dilation3 = cv2.dilate(img3, kernel=k, iterations=1)

eroded1 = cv2.erode(dilation1, kernel=k, iterations=1)
eroded2 = cv2.erode(dilation2, kernel=k, iterations=1)
eroded3 = cv2.erode(dilation3, kernel=k, iterations=1)

opening1 = cv2.morphologyEx(img1, op= cv2.MORPH_OPEN, kernel=k)
opening2 = cv2.morphologyEx(img2, op= cv2.MORPH_OPEN, kernel=k)
opening3 = cv2.morphologyEx(img3, op= cv2.MORPH_OPEN, kernel=k)

close1 = cv2.morphologyEx(img1, op= cv2.MORPH_CLOSE, kernel=k)
close2 = cv2.morphologyEx(img2, op= cv2.MORPH_CLOSE, kernel=k)
close3 = cv2.morphologyEx(img3, op= cv2.MORPH_CLOSE, kernel=k)

imgStack = stackimages.ManyImgs(scale=0.75,imgarray=[[img1, dilation1, eroded1,close1,opening1],
                                                  [img2, dilation2, eroded2,close2,opening2],
                                                  [img3, dilation3, eroded3,close3,opening3]])
cv2.imshow('out', imgStack)
cv2.waitKey()