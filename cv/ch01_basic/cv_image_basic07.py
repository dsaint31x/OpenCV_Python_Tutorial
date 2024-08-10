import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./opencv_logo.png', cv2.IMREAD_UNCHANGED)
print(f'{img.shape=}')

fig, ax = plt.subplots()
im = ax.imshow(img[...,3], cmap='gray')

cbar = fig.colorbar(im, ax=ax)
cbar.set_ticks(np.arange(0,256,255))
cbar.set_ticklabels(np.arange(0,256,255))
ax.set_title('alpha channel')
plt.show()
