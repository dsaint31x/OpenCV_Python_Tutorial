import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

dir_path = os.path.dirname(__file__)
f_str = os.path.join(dir_path,'cat_cv1.tif')
# f_str = os.path.join(dir_path,'opencv_logo.png')

# using opencv 
img = cv2.imread(
    f_str, 
    cv2.IMREAD_UNCHANGED,
    )

if img is None:
    sys.exit(f'There is not a file: {f_str}')

# from cv2 to matplotlib
if img.ndim == 3:
    if img.shape[2] > 3:
        cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    else:
        img = img[...,::-1]

# using matplotlib
# img = plt.imread(f_str)
fig, ax = plt.subplots()
im = ax.imshow(
    img, 
    # alpha=.3,       # 투명도
    # origin='lower', # left bottom을 origin으로
    )
cbar = fig.colorbar(im, ax=ax)
cbar.set_ticks     (np.arange(0,256,255))
cbar.set_ticklabels(np.arange(0,256,255))
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('matplotlib test')

plt.show()
