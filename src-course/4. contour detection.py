import cv2
import numpy as np
import stackimages

img = cv2.imread('../resources/Photos/cats 2.jpg')
img2 = img.copy()
(h,w) = img.shape[:2]


# su dung edge detector
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, ksize=(7,7), sigmaX=1)
canny = cv2.Canny(blur, threshold1=125, threshold2=175)

cts, hierachy = cv2.findContours(canny, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

for c in cts:
    cv2.drawContours(img, contours=[c], contourIdx=0, color=(255,255,255))

# su dung threshold
ret, thresh = cv2.threshold(gray,thresh=125, maxval=255, type=cv2.THRESH_BINARY)
cts, hierachy = cv2.findContours(thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
blank = np.zeros(shape=img.shape, dtype=np.uint8)
cv2.drawContours(img2,contours=cts, contourIdx=-1, color=(255,255,255))

imgstack = stackimages.ManyImgs(scale=1, imgarray=[[img,canny],
                                                   [img2, thresh]])
cv2.imshow('out', imgstack)
cv2.waitKey()