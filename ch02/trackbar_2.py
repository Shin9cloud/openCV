import numpy as np
import cv2


def on_level_change_B(pos):
    value = pos * 32
    if value >= 255:
        value = 255

    img[[0],:] = value
    cv2.imshow('image', img)
    
def on_level_change_G(pos):
    value = pos * 32
    if value >= 255:
        value = 255

    img[1] = value
    cv2.imshow('image', img)

def on_level_change_R(pos):
    value = pos * 32
    if value >= 255:
        value = 255

    img[2] = value
    cv2.imshow('image', img)


img = np.full((480, 640, 3),(0,0,0), np.uint8)

cv2.namedWindow('image')
cv2.createTrackbar('level_B', 'image', 0, 8, on_level_change_B)
cv2.createTrackbar('level_G', 'image', 0, 8, on_level_change_G)
cv2.createTrackbar('level_R', 'image', 0, 8, on_level_change_R)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
