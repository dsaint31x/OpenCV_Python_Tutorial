import cv2
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  

# img_path = '/home/dsaint31/lecture/OpenCV_Python_Tutorial/images/lena.png'
img_path = os.path.join(BASE_DIR,"img/lena.png")

img = cv2.imread(img_path)
cv2.imshow('img', img)
x,y,w,h = cv2.selectROI('img', img, False)

print(cv2.getWindowProperty('img', cv2.WND_PROP_VISIBLE))
if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('roi', roi)
    cv2.moveWindow('roi',0,0)
    cv2.imwrite('roi2.png', roi)

while cv2.getWindowProperty('img', cv2.WND_PROP_VISIBLE) >=1: # check whether x button is clicked.
    key_code = cv2.waitKey(50)&0xff #50msec
    print(key_code)
    if key_code == 27: #check whether ESC key is entered.
        break

cv2.destroyAllWindows()