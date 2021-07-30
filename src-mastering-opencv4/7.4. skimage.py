import cv2
from skimage.filters import threshold_otsu, threshold_triangle, threshold_sauvola, threshold_niblack
from skimage import img_as_ubyte

img = cv2.imread('../resources/sudoku.png')
imgGray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

print(imgGray.shape)
thresh = threshold_otsu(imgGray)
binary = imgGray > thresh
binary = img_as_ubyte(binary)

def threshold_func(func, image):
    thresh = func(image)
    binary = image > thresh
    binary = img_as_ubyte(binary)
    return  binary

cv2.imshow('threshold_otsu', binary)
cv2.imshow('threshold_triangle', threshold_func(threshold_triangle, imgGray))
cv2.imshow('threshold_sauvola', threshold_func(threshold_sauvola, imgGray))
cv2.imshow('threshold_niblack', threshold_func(threshold_niblack, imgGray))

cv2.waitKey()