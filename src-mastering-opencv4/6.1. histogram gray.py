import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../resources/lena.jpg')
imgGray = cv2.cvtColor(img, code = cv2.COLOR_BGR2GRAY)
print(imgGray.shape)

imgEqua = cv2.equalizeHist(imgGray)

imgEqua2 = []
for i in range(3):
    imgEqua2.append(cv2.equalizeHist(img[...,i]))
imgEqua2 = cv2.merge(imgEqua2)

b,g,r = cv2.split(cv2.cvtColor(img, code=cv2.COLOR_BGR2HSV))
r = cv2.equalizeHist(r)
imgEqua3 = cv2.cvtColor(cv2.merge((b,g,r)), code= cv2.COLOR_HSV2BGR)

cv2.imshow('out', img)
cv2.imshow('imgGray', imgGray)
cv2.imshow('imgEqua', imgEqua)
cv2.imshow('imgEqua2', imgEqua2)
cv2.imshow('imgEqua3', imgEqua3)

for i in range(3):
    hist = cv2.calcHist([img], channels=[i], mask=None, histSize=[256], ranges=[0,256])
    print(hist.shape)
    plt.plot(hist)
plt.show()

histGray = cv2.calcHist([imgGray], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.plot(histGray)
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()
