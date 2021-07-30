import cv2
import numpy as np
import constant

img = cv2.imread('../resources/Photos/lady.jpg')

rectangle = np.zeros(shape = img.shape, dtype="uint8")
rectangle = cv2.rectangle(rectangle, (25, 25), (275, 275), constant.WHITE, -1)

merge = cv2.bitwise_and(img, rectangle)

# # draw a rectangle
# rectangle = np.zeros((300, 300), dtype="uint8")
# cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
# cv2.imshow("Rectangle", rectangle)
# # draw a circle
# circle = np.zeros((300, 300), dtype = "uint8")
# cv2.circle(circle, (150, 150), 150, 255, -1)
# cv2.imshow("Circle", circle)
#
# bitwiseAnd = cv2.bitwise_and(rectangle, circle)
# cv2.imshow("AND", bitwiseAnd)

cv2.imshow('0',img)
cv2.imshow('1',rectangle)
cv2.imshow('2',merge)
cv2.waitKey()