import sys
import cv2
import numpy as np
from skimage import data

cat   = data.chelsea()
astro = data.astronaut()

cat_cv   = cv2.cvtColor(cat, cv2.COLOR_RGB2BGR)
astro_cv = cv2.cvtColor(astro, cv2.COLOR_RGB2BGR)

cv2.imwrite("cat_cv.tif"  , cat_cv)
cv2.imwrite("astro_cv.bmp", astro_cv)

img = cv2.imread("cat_cv.tif", cv2.IMREAD_GRAYSCALE)
if img is None:
    print('Error : the image path may be wrong!')
    sys.exit(0)
    
new_cat_cv = cv2.imread("cat_cv.tif")
new_ast_cv = cv2.imread("astro_cv.bmp")
print(f"{img.shape=}")
print(f"{new_cat_cv.shape=}")
print(f"{new_ast_cv.shape=}")
cv2.imshow('01', img)
cv2.imshow('02', new_cat_cv)
cv2.imshow('03', new_ast_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

    