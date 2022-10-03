import cv2
import numpy as np
import pyautogui

is_dragging = False

x0,y0 = -1,-1
w0,h0 = -1,-1
red = (0,0,255)

def onMouse(event, x, y, flags, param):

    global is_dragging
    global x0,y0,w0,h0
    
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
                roi = img[y0:y0+h, x0:x0+w]
                #roi = img[x0:x0+w, y0:y0+h]
                cv2.imshow('roi', roi)
                cv2.moveWindow('roi',0,0)
                cv2.imwrite('./roi.png',roi)
                print('roi is cropped and saved!')
            else:
                cv2.imshow('roied_img', img)
                print('unvalid roi!. select roi carefully')

    pyautogui.press('e') # main thread로 돌아가기 위한 key event 발생.
    return

img = cv2.imread('/home/dsaint31/lecture/OpenCV_Python_Tutorial/images/lena.png')
cv2.imshow('roied_img', img)
cv2.setMouseCallback('roied_img',onMouse)

while cv2.getWindowProperty('roied_img', cv2.WND_PROP_VISIBLE) >= 1:
    key_code = cv2.waitKey(50) # millisecond
    if key_code == 27:
        # print('ESC')
        break;
    elif cv2.getWindowProperty('roied_img', cv2.WND_PROP_VISIBLE) < 1:
        # print('closed button')
        break;
    elif cv2.getWindowProperty('roi', cv2.WND_PROP_VISIBLE) < 1:
        # print('closed button')
        cv2.destroyWindow('roi')

cv2.destroyAllWindows()
