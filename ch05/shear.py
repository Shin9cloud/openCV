import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]
# dst = cv2.warpAffine(src, aff, (0,0)) ## 화면 잘림
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h)) ## 화면창 늘어난 만큼 늘리기

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
