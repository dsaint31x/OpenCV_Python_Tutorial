import cv2
import numpy as np

img_path = '/home/dsaint31/lecture/OpenCV_Python_Tutorial/images/lena.png'

img = cv2.imread(img_path)
cv2.imshow('img', img)
x,y,w,h = cv2.selectROI('img', img, False)

if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('roi', roi)
    cv2.moveWindow('roi',0,0)
    cv2.imwrite('roi2.png', roi)

while cv2.getWindowProperty('img', cv2.WND_PROP_VISIBLE) >=1:
    key_code = cv2.waitKey(50)
    if key_code == 27:
        break

cv2.destroyAllWindows()
