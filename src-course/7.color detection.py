import cv2
import numpy as np
import stackimages

img = cv2.imread('resources/lambo.jpg')
imgHSV = cv2.cvtColor(img, code=cv2.COLOR_BGR2HSV)


def empty(a):
    pass

cv2.namedWindow(winname="trackbars")
cv2.resizeWindow(winname="trackbars", width=640, height=240)

cv2.createTrackbar("hue min", "trackbars", 0, 179, empty)
cv2.createTrackbar("hue max", "trackbars", 26, 179, empty)
cv2.createTrackbar("sat min", "trackbars", 92, 255, empty)
cv2.createTrackbar("sat max", "trackbars", 255, 255, empty)
cv2.createTrackbar("val min", "trackbars", 60, 255, empty)
cv2.createTrackbar("val max", "trackbars", 255, 255, empty)

while True:
    h_min = cv2.getTrackbarPos(trackbarname="hue min",winname="trackbars")
    h_max = cv2.getTrackbarPos(trackbarname="hue max", winname="trackbars")
    s_min = cv2.getTrackbarPos(trackbarname="sat min", winname="trackbars")
    s_max = cv2.getTrackbarPos(trackbarname="sat max", winname="trackbars")
    v_min = cv2.getTrackbarPos(trackbarname="val min", winname="trackbars")
    v_max = cv2.getTrackbarPos(trackbarname="val max", winname="trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    mask = cv2.inRange(imgHSV, lowerb=np.array([h_min,s_min, v_min]), upperb=np.array([h_max, s_max, v_max]))

    imgResult = cv2.bitwise_and(img, img, mask=mask)

    imgstack = stackimages.ManyImgs(1,[[img, imgHSV,mask, imgResult]])
    cv2.imshow('out', imgstack)
    cv2.waitKey(1)