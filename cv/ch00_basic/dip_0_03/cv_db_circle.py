#!/usr/bin/env python
import cv2
import time, os
import numpy as np

# mouse callback function
def create_dblclk_cb(dblclk_threshold=0.3):
    
    # mouse callback function
    def db_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK: # double click event!
            cv2.circle(img,(x,y),100,(255,0,0),-1)
    
    
    last_click_time = 0
    
    def db_click_mac(event, x, y, flags, params):
        nonlocal last_click_time
        if event == cv2.EVENT_LBUTTONDOWN:
            current_time = time.time() # seconds
            if current_time - last_click_time < dblclk_threshold:
                cv2.circle(img,(x,y),100,(255,0,0),-1)
            last_click_time = current_time
    
    os_str = os.uname().sysname
    if os_str == "Darwin":
        return db_click_mac
    else:
        return db_click
            
    return db_click
            

if __name__ == "__main__":
    # Create a black image, a window and bind the function to window
    img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',create_dblclk_cb())

    while True:
        cv2.imshow('image',img)
        if cv2.waitKey(20) & 0xFF == 27: # enter ESC
            break
        if cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE ) <1:
            break
    cv2.destroyAllWindows()
