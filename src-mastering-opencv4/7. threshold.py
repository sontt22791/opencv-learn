import cv2

img = cv2.imread('../resources/lena.jpg')
imggray = cv2.cvtColor(img, code= cv2.COLOR_BGR2GRAY)

retval, dst = cv2.threshold(img, thresh=150, maxval=255, type=cv2.THRESH_BINARY)
retval2, dst2 = cv2.threshold(imggray, thresh=150, maxval=255, type=cv2.THRESH_BINARY)
print(retval)

cv2.imshow('out', imggray)
cv2.imshow('imgthres', dst)
cv2.imshow('imgthres2', dst2)

cv2.waitKey(0)