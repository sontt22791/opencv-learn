import cv2
import numpy as np

img = cv2.imread('resources/lena.jpg')
imgGray = cv2.cvtColor(img, code= cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, ksize=(7,7), sigmaX=1)

imgEdge = cv2.Canny(imgBlur, threshold1=150, threshold2=200)

kernel = np.ones(shape=(3,3))
imgDilation = cv2.dilate(imgEdge, kernel=kernel)
imgEroded = cv2.erode(imgDilation,kernel=kernel)

cv2.imshow("out", img)
cv2.imshow("out gray", imgGray)
cv2.imshow("out blur", imgBlur)
cv2.imshow("out edge", imgEdge)
cv2.imshow("out dilate", imgDilation)
cv2.imshow("out erode", imgEroded)
# imgStack = np.concatenate([img, imgGray, imgBlur,imgEdge, imgDilation, imgEroded], axis=1)
# cv2.imshow("output", imgStack)
cv2.waitKey(0)