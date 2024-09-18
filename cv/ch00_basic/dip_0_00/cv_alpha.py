import sys
import os
dir_path = os.path.dirname(__file__)
sys.path.append(dir_path)

import cv2
import numpy as np
import matplotlib.pyplot as plt

from cv_imread import ds_imread


f_str = os.path.join(dir_path,'opencv_logo.png')
img = ds_imread(f_str, cv2.IMREAD_UNCHANGED)

fig, ax = plt.subplots()
im = ax.imshow(img[...,3], 
               cmap='gray',
               )
cbar = fig.colorbar(im, ax=ax)
cbar.set_ticks     (np.arange(0,256,255))
cbar.set_ticklabels(np.arange(0,256,255))
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('alpha channel')
plt.show()
