import sys
import numpy as np
import cv2

src = cv2.imread('tekapo.bmp')
if src is None:
    print('Image load failed!')
    sys.exit()

for f in(1,0,-1): ## 좌우 대칭, 상하 대칭, 좌우 & 상하 대칭
    dst = cv2.flip(src, f , dst=None)
    cv2.imshow('src',src)
    cv2.moveWindow('src', 20, 50)
    cv2.imshow('dst',dst)
    cv2.moveWindow('dst', 700, 50)
    cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()
