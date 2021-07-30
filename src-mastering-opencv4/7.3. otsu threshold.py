import cv2

img = cv2.imread('../resources/leaf-noise.png')

imggray = cv2.cvtColor(img, code= cv2.COLOR_BGR2GRAY)

imgblur = cv2.GaussianBlur(imggray, ksize=(11,11), sigmaX=0)

ret, imgResult = cv2.threshold(imgblur,thresh=0, maxval=255, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(imgResult.shape)
cv2.imshow('out', img)
cv2.imshow('imggray', imggray)
cv2.imshow('imgblur', imgblur)
cv2.imshow('imgResult', imgResult)
# cv2.imshow('out', img)q


cv2.waitKey()