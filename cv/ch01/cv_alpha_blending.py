import os
import cv2
import numpy as np

d_path = os.path.dirname(__file__)
d_path = f'{d_path}/img'
fstr_bg = os.path.join(d_path,'ml.png')
fstr_fg = os.path.join(d_path,'opencv-logo0.png')

def show_imgs(ax, title, img):
    ax.imshow(img[...,::-1])
    ax.set_title(title)
    ax.set_xticks([]); ax.set_yticks([])


bg = cv2.imread(fstr_bg)
fg = cv2.imread(fstr_fg)
print(fg.shape)
bg = cv2.resize(bg, dsize=fg.shape[1::-1], interpolation= cv2.INTER_AREA)

dst = cv2.addWeighted(bg,0.7, fg,0.3,0)

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


