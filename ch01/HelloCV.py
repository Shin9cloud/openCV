import sys
import cv2

print('Hello OpenCV', cv2. version)

img = cv2.imread('cat.bmp')
# img = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

# cv2.namedWindow('image')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)

cv2.resizeWindow('image', width=1, height=5)

cv2.imshow('image', img)
while True:
    if cv2.waitKey() == 13 or cv2.waitKey() == 9:
        break

# cv2.imwrite('catzz.png',img)
# cv2.waitKey()

cv2.destroyAllWindows()