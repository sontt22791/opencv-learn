import cv2
import numpy as np

img = cv2.imread('../resources/sudoku.png')
imggray = cv2.cvtColor(img, code= cv2.COLOR_BGR2GRAY)
imgbilate = cv2.bilateralFilter(imggray,d=15,sigmaColor=25,sigmaSpace=25)

imgthresh = cv2.adaptiveThreshold(imggray, maxValue=100, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                                  thresholdType=cv2.THRESH_BINARY, blockSize=11, C= 5)

imgthreshbilate = cv2.adaptiveThreshold(imgbilate, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                                  thresholdType=cv2.THRESH_BINARY, blockSize=11, C= 5)

print(imggray.shape)
cv2.imshow('1', img)
cv2.imshow('2',imggray)
cv2.imshow('imgbilate',imgbilate)
cv2.imshow('imgthresh',imgthresh)
cv2.imshow('imgthreshbilate',imgthreshbilate)

cv2.waitKey()