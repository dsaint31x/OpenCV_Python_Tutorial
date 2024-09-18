import os
import cv2
import numpy as np

d_path = os.path.dirname(__file__)
d_path = f'{d_path}/img'

fstr_bg = os.path.join(d_path,'ml.png')
fstr_fg = os.path.join(d_path,'opencv-logo.png')
bg = cv2.imread(fstr_bg)
fg = cv2.imread(fstr_fg,cv2.IMREAD_UNCHANGED)
bg = cv2.resize(bg, dsize=fg.shape[1::-1], interpolation=cv2.INTER_AREA)

transparency = 0.7
bgr   = fg[...,:3]
alpha = fg[...,3]/255.
alpha = alpha[..., np.newaxis] * (1-transparency)

ret = bgr * alpha + bg * (1.-alpha)
ret = cv2.convertScaleAbs(ret)

cv2.imshow('img', ret)
cv2.waitKey(0)
cv2.destroyAllWindows()