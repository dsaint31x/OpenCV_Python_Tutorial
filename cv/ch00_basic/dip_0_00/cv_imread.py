#!/bin/env python
import sys
import cv2
import os

def ds_imread(f_str, mode=cv2.COLOR_RGB2BGR):
    img = cv2.imread(f_str, mode)
    if img is None:
        sys.exit(f'Error: There is not a file: {f_str}')
    return img

def ds_screen_size():
    import tkinter as tk
    root = tk.Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    return w,h

if __name__ == "__main__": 
      
    dir_str = os.path.dirname(__file__)
    f_str = os.path.join(dir_str, "cat_cv.tif")
    
    #img = ds_imread(f_str, cv2.IMREAD_GRAYSCALE)
    #img = ds_imread(f_str, 0)
    #img = ds_imread(f_str, cv2.IMREAD_COLOR)
    #img = ds_imread(f_str, 1)
    #img = ds_imread(f_str, cv2.IMREAD_UNCHANGED)
    #img = ds_imread(f_str, -1)
    img = ds_imread(f_str)
    print(f"{img.shape=}")
    print(f"{img.dtype=}")
    
    ih,iw = img.shape[:2]
    sw,sh = ds_screen_size()
    
    cv2.namedWindow('01', cv2.WINDOW_NORMAL)
    cv2.moveWindow('01', (sw-iw)//2, (sh-ih)//2 )
    cv2.imshow('01', img)
    while True:
        key = cv2.waitKey(100)
        if key & 0xFF == 27: # enter ESC
            break
        if cv2.getWindowProperty('01', cv2.WND_PROP_VISIBLE ) <1:
            break;
    cv2.destroyAllWindows()

    