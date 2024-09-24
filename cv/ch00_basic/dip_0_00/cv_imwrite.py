from skimage import data
import cv2

# from skimage.color import rgb2gray
# from skimage import img_as_ubyte,img_as_float

cat_cv   = data.chelsea()     # take the test image of cat!
astro_cv   = data.astronaut()     # take the test image of cat!

cat_cv   = cv2.cvtColor(cat_cv, cv2.COLOR_RGB2BGR)
astro_cv = cv2.cvtColor(astro_cv, cv2.COLOR_RGB2BGR)

cv2.imwrite('cat_cv.tif', cat_cv)
cv2.imwrite('astro_cv.bmp', astro_cv)