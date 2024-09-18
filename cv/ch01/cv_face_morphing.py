import cv2
import os

def f(x):
  alpha = x/100
  ret = cv2.addWeighted(img_0, alpha, img_1, 1-alpha,0)
  cv2.imshow('img',ret)

d_path = os.path.dirname(__file__)
d_path = f'{d_path}/img'
fstr_0 = os.path.join(d_path,'face02.PNG')
fstr_1 = os.path.join(d_path,'man_face.jpg')

img_0 = cv2.imread(fstr_0)
img_1 = cv2.imread(fstr_1)
img_0 = cv2.resize(img_0, dsize=(img_1.shape[1],img_1.shape[0]), interpolation= cv2.INTER_AREA)

init_ap = 50
alpha = init_ap/100
cv2.namedWindow('img')
cv2.createTrackbar('p', 'img', init_ap, 100, f)
ret = cv2.addWeighted(img_0, alpha, img_1, 1-alpha,0)
cv2.imshow('img',ret)
while(True):
    k = cv2.waitKey(10) & 0xFF
    if k == 27: # esc
        break
    if cv2.getWindowProperty('img', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()