import sys
import numpy as np
import cv2


# 히스토그램 평활화
src = cv2.imread('field.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

b_plane, g_plane, r_plane = cv2.split(src)
b_plane = cv2.equalizeHist(b_plane)
g_plane = cv2.equalizeHist(g_plane)
r_plane = cv2.equalizeHist(r_plane)
dst_rgb = cv2.merge((b_plane, g_plane, r_plane))
cv2.imshow('src', src)
cv2.moveWindow('src', 20, 50) 
cv2.imshow('dst', dst_rgb)
cv2.moveWindow('dst', 700, 50)

cv2.waitKey()

cv2.destroyAllWindows()
