import cv2
import numpy as np



if __name__ == "__main__":
    # img_path = '/home/dsaint31/lecture/OpenCV_Python_Tutorial/images/lena.png'
    img_path = '/mnt/d/lecture/OpenCV_Python_Tutorial/images/lena.png'

    img = cv2.imread(img_path)
    cv2.imshow('img', img)

    # while True:
    #     x,y,w,h = cv2.selectROI('img', img, False)
    #     print(x,y,w,h)
        
    #     if w and h:
    #         roi = img[y:y+h, x:x+w]
    #         cv2.imshow('roi', roi)
    #         cv2.moveWindow('roi',0,0)
    #         cv2.imwrite('roi2.png', roi)
    #         break

    # while cv2.getWindowProperty('img', cv2.WND_PROP_VISIBLE) >=1: # check whether x button is clicked.
    while True:
        key_code = cv2.waitKey(50) #50msec
        # print(key_code)
        if key_code & 0xFF == 27: #check whether ESC key is entened.
            break
        elif key_code  & 0xFF == ord('x'):
            cv2.destroyWindow('roi')

    #cv2.destroyAllWindows('img')        
    cv2.destroyWindow('img')
