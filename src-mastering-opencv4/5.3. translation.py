import cv2
import numpy as np

def translate(img, x, y):
    M = np.array([[1,0,x],[0,1,y]], dtype=np.float32)
    dst = cv2.warpAffine(img, M, dsize=(img.shape[1], img.shape[0]))
    return  dst

img = cv2.imread('../resources/lena.jpg')
cv2.imshow('original', img)
imgTranslate = translate(img, 50,50)
cv2.imshow('out', imgTranslate)
cv2.waitKey(0)