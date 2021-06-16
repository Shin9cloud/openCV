import sys
import numpy as np
import cv2


src = cv2.imread('cells.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# _, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
# _, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)

_, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY_INV)
_, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY_INV)
## 반전

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
