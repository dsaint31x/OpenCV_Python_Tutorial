import sys
import os
dir_path = os.path.dirname(__file__)
sys.path.append(dir_path)

import cv2
import numpy as np
import matplotlib.pyplot as plt
from cv_imread import ds_imread, ds_screen_size


f_str = os.path.join(dir_path,'cat_cv.tif')
# f_str = os.path.join(dir_path,'opencv_logo.png')

# using opencv 
img = ds_imread(f_str, cv2.IMREAD_UNCHANGED)
# from cv2 to matplotlib
if len(img.shape) == 3:
    if img.shape[2] > 3:
        cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    else:
        img = img[...,::-1]

# using matplotlib
# img = plt.imread(f_str)

fig, ax = plt.subplots()
im = ax.imshow(img, alpha=.3, origin='lower')
cbar = fig.colorbar(im, ax=ax)
cbar.set_ticks     (np.arange(0,256,255))
cbar.set_ticklabels(np.arange(0,256,255))
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('alpha channel')

plt.show()
