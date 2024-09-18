import cv2
import os
import numpy as np

d_path = os.path.dirname(__file__)
d_path = f'{d_path}/img'
fstr_0 = os.path.join(d_path,'messi5.jpg')
fstr_1 = os.path.join(d_path,'opencv_logo.png')

img_0 = cv2.imread(fstr_0)
img_1 = cv2.imread(fstr_1,cv2.IMREAD_UNCHANGED)

alpha = img_1[:,:,3]
bgr   = img_1[...,:3]

# -----------------
# general alpha processing
mask = alpha[...,np.newaxis]/255.
rows, cols = img_1.shape[:2]
roi = img_0[:rows, :cols]

ret0 = img_0.copy()
ret0[0:rows, 0:cols] = img_0[0:rows, 0:cols, :] * (1.-mask) + bgr * mask
ret0 = cv2.convertScaleAbs(ret0)


# -----------------
# bitwise op based processing : worse result
ret1 = img_0.copy()
_, bmask = cv2.threshold(alpha, 1, 255, cv2.THRESH_BINARY)
print(bgr.dtype)
masked_fg = cv2.bitwise_and(bgr, bgr, mask=bmask)
masked_bg = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(bmask))
added_roi = cv2.convertScaleAbs(masked_fg+masked_bg)
ret1[:rows,:cols] = added_roi

cv2.imshow('img0', ret0)
cv2.imshow('img1', ret1)
cv2.waitKey(0)
cv2.destroyAllWindows()
