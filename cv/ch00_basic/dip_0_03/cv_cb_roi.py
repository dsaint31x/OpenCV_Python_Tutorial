import cv2
import numpy as np
# import pyautogui

is_dragging = False

x0,y0 = -1,-1
w0,h0 = -1,-1
red = (0,0,255)
exit_roi = False

import os
d_path = os.path.dirname(__file__)
f_path = os.path.join(d_path,"lena.png")

def onMouse(event, x, y, flags, param):

    global is_dragging
    global x0,y0,w0,h0
    global exit_roi
    
    if event == cv2.EVENT_LBUTTONDOWN:
        is_dragging = True
        x0 = x
        y0 = y
        print(x0,y0)

    elif event == cv2.EVENT_MOUSEMOVE:
        if is_dragging:
            tmp = img.copy()
            cv2.rectangle(tmp, (x0,y0), (x,y), red, 2)
            cv2.imshow('roied_img', tmp)

    elif event == cv2.EVENT_LBUTTONUP:
        if is_dragging:
            is_dragging = False
            w = x-x0
            h = y-y0

            if w>0 and h > 0:
                tmp = img.copy()

                cv2.rectangle(tmp, (x0,y0), (x,y), red, 3)
                cv2.imshow('roied_img', tmp)
                exit_roi = True
                roi = img[y0:y0+h, x0:x0+w]
                #roi = img[x0:x0+w, y0:y0+h]
                cv2.imshow('roi', roi)
                cv2.moveWindow('roi',0,0)
                cv2.imwrite(f'{d_path}/roi.png',roi)
                print('roi is cropped and saved!')
            else:
                cv2.imshow('roied_img', img)
                print('unvalid roi!. select roi carefully')

    # pyautogui.press('e') # main thread로 돌아가기 위한 key event 발생.
    return
img = cv2.imread(f_path)
cv2.imshow('roied_img', img)
cv2.setMouseCallback('roied_img',onMouse)

while cv2.getWindowProperty('roied_img', cv2.WND_PROP_VISIBLE) >= 1:
    key_code = cv2.waitKey(50) & 0xff # millisecond
    if key_code != 255:
        print(key_code, ord('x'),exit_roi)

    if key_code == 27:
        # print('ESC')
        break;
    elif exit_roi and key_code == 120:
        print('closed button')
        exit_roi = False
        cv2.destroyWindow('roi')
    elif cv2.getWindowProperty('roied_img', cv2.WND_PROP_VISIBLE) < 1:
        # print('closed button')
        break;
    elif exit_roi and cv2.getWindowProperty('roi', cv2.WND_PROP_VISIBLE) < 1:
        # print('closed button')
        exit_roi = False
        cv2.destroyWindow('roi')

cv2.destroyAllWindows()