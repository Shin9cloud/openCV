import sys
import numpy as np
import cv2


src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

#made_functions
# gmin= np.min(src)
# gmax= np.max(src)
# dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8) #numpy사용 동일 결과

## 히스토그램 표현 함수
def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))#100보다 적은 값을 가지기 위한 식
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

hist_src = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg_src = getGrayHistImage(hist_src)

hist_dst = cv2.calcHist([dst], [0], None, [256], [0, 256])
histImg_dst = getGrayHistImage(hist_dst)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('histImg_src', histImg_src)
cv2.imshow('histImg_dst', histImg_dst)

cv2.waitKey()

cv2.destroyAllWindows()


# 교수님 답안
'''
import sys
import numpy as np
import cv2
def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)
    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))#100보자 적은 값을 가지기 위한 식
        cv2.line(imgHist, pt1, pt2, 0)
    return imgHist
src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed!')
    sys.exit()
gmin, gmax, _, _ = cv2.minMaxLoc(src)
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
#dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8) #numpy사용 동일 결과
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)
hist2 = cv2.calcHist([dst], [0], None, [256], [0, 256])
histImg2 = getGrayHistImage(hist2)
cv2.imshow('histImg', histImg)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('histImg', histImg)
cv2.imshow('histImg2', histImg2)
cv2.waitKey()
cv2.destroyAllWindows()
'''