import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 3)
dst_int = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)
src_f = src.astype(np.float32)

blr2 = cv2.GaussianBlur(src_f, (0, 0), 3.0)
dst_float = np.clip(2. * src_f - blr2, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst_int', dst_int)
cv2.imshow('dst_float', dst_float)
cv2.waitKey()

cv2.destroyAllWindows()