import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 이미지 읽기
imgL = cv.imread('tsukuba_l.png', cv.IMREAD_GRAYSCALE)
imgR = cv.imread('tsukuba_r.png', cv.IMREAD_GRAYSCALE)

# SGBM 파라미터 설정
minDisparity = 0
numDisparities = 16 * 2  # 16의 배수여야 함
blockSize = 5
P1 = 8 * 3 * blockSize ** 2  # 매개변수 1
P2 = 32 * 3 * blockSize ** 2  # 매개변수 2
disp12MaxDiff = 1
uniquenessRatio = 10
speckleWindowSize = 100
speckleRange = 32
preFilterCap = 63

# SGBM 객체 생성 및 설정
stereo = cv.StereoSGBM_create(
    minDisparity=minDisparity,
    numDisparities=numDisparities,
    blockSize=blockSize,
    P1=P1,
    P2=P2,
    disp12MaxDiff=disp12MaxDiff,
    uniquenessRatio=uniquenessRatio,
    speckleWindowSize=speckleWindowSize,
    speckleRange=speckleRange,
    preFilterCap=preFilterCap,
    mode=cv.STEREO_SGBM_MODE_SGBM_3WAY
)

# 시차 맵 계산
disparity = stereo.compute(imgL, imgR)

# 시차 맵 시각화
plt.imshow(disparity, 'gray')
plt.show()

