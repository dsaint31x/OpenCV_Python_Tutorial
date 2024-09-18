import cv2
import sys
import os

d_str = os.path.dirname(__file__)
fstr = os.path.join(d_str,'img/messi5.jpg')

img_ori = cv2.imread(fstr)
if img_ori is None:
    sys.exit(f'There is not a file:{fstr}')
cv2.imshow('original image',img_ori) #expects true color
img = img_ori.copy()

ball = img[280:340,330:390] # numpy is based on matrix. Note that x is width and column, y is height and row.
print(ball.shape)
img[273:333,100:160] = ball

cv2.imshow('modified image',img)

# # ------------------------
# # for simplicity! In this case, never use x button on window to close it.
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ---------------------------
# In this code, x button is supported
while cv2.getWindowProperty('modified image', cv2.WND_PROP_VISIBLE) >= 1:
    k = cv2.waitKey(10)
    if k&0xff == 27:
        break
    if cv2.getWindowProperty('original image', cv2.WND_PROP_VISIBLE) < 1:
        break
cv2.destroyAllWindows()