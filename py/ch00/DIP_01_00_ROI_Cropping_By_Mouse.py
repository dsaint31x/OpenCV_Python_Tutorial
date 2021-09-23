import cv2
import numpy as np
import matplotlib.pyplot as plt

fstr = '../../images/messi5.jpg'

isDragging = False
x0,y0,w,h = -1,-1,-1,-1

ing_clr = (255,0,0)
end_clr = (0,0,255)

def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, w, h, img
    
    if event == cv2.EVENT_LBUTTONDOWN: # 드래그 시작을 위한 왼버튼 누르는 이벤트
        isDragging = True
        x0=x
        y0=y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0,y0), (x,y),ing_clr,2)
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            w = x-x0
            h = y-y0
            print(f'x:{x: 3d},y:{y: 3d},w:{w: 3d},h:{h: 3d}')
            if w > 0 and h > 0:
                img_draw = img.copy()
                cv2.rectangle(img_draw, (x0,y0), (x,y),end_clr,2 )
                cv2.imshow('img', img_draw)
                roi = img[y0:y0+h,x0:x0+w]
                cv2.imshow('roi', roi)
                cv2.moveWindow('roi',0,0)
                cv2.imwrite('./roi.jpg',roi)
                print('roi saved!')
            else:
                cv2.imshow('img', img)
                print('roi를 저장하려면 좌측상단에서 우측하단으로 드래그하세요.!')

img = cv2.imread(fstr)
cv2.imshow('img', img)
cv2.setMouseCallback('img',onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()