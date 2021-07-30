import cv2


def rotation(image):
    h, w = image.shape[:2]
    m = cv2.getRotationMatrix2D((w // 2, h // 2), angle=90, scale=1)
    dst = cv2.warpAffine(image, m, dsize=(w, h))
    return dst


img = cv2.imread('../resources/lena.jpg')
cv2.imshow('original', img)
imgTranslate = rotation(img)
cv2.imshow('out', imgTranslate)
cv2.waitKey(0)
