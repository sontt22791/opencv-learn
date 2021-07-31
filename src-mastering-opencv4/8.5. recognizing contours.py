import cv2
import constant

img = cv2.imread('../resources/shapes.png')
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
_,thres = cv2.threshold(gray, thresh=75, maxval=255, type=cv2.THRESH_BINARY)

cts, hie = cv2.findContours(thres, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)

for c in cts:
    cv2.drawContours(img, contours=[c], contourIdx=0, color=constant.WHITE, thickness=3)

    # Calculate perimeter of the contour:
    perimeter = cv2.arcLength(c, True)

    contour_approx = cv2.approxPolyDP(c, 0.03* perimeter, closed=True)
    print(len(contour_approx))
    M = cv2.moments(c)
    Cx = int(M["m10"] / M["m00"])
    Cy = int(M["m01"] / M["m00"])

    cv2.putText(img, text=str(len(contour_approx)), org=(Cx,Cy), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=constant.WHITE)

cv2.imshow('1', img)
cv2.imshow('2', thres)
cv2.waitKey()