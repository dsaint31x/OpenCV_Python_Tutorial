import cv2
import numpy as np
import os

d_path = os.path.dirname(__file__)
img_path = f'{d_path}/lena.png'

img = cv2.imread(img_path)
cv2.imshow('img', img)
x,y,w,h = cv2.selectROI('img', img, False)

print(cv2.getWindowProperty('img', cv2.WND_PROP_VISIBLE))
if w and h: #선택시 0이 아닌 수로 w,h가 설정됨.
    roi = img[y:y+h, x:x+w]
    cv2.imshow('roi', roi)
    cv2.moveWindow('roi',0,0)
    cv2.imwrite(f'{d_path}/roi2.png', roi)
    print('Enter ESC to quit!')

while cv2.getWindowProperty('img', cv2.WND_PROP_VISIBLE) >=1: # check whether x button is clicked.
    # c = input('Quit? (enter q)')
    # if c == 'q':
    #     break
    key_code = cv2.waitKey(500)&0xff #50msec
    if key_code == 27: #check whether ESC key is entered.
        break
    

cv2.destroyAllWindows()