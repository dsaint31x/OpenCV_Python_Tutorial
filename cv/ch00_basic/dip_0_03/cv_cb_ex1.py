import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode    = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw(event,x,y,flags,param):
    global ix, iy, drawing, mode
    
    tmp = None
        
    if event == cv2.EVENT_LBUTTONDOWN: # left button down event
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE: # mouse move event
        if drawing == True:
            tmp = img.copy()
            if mode == True:                
                cv2.rectangle(tmp,(ix,iy),(x,y),(0,255,0),-1)
                
            else:
                w = x-ix
                h = y-iy                                                
                cv2.ellipse(tmp, (ix+w//2,iy+h//2), 
                            (np.abs(w)//2,np.abs(h)//2),0,0,360, (0,0,255),-1)
                cv2.rectangle(tmp,(ix,iy),(x,y),(0,255,0),1)
                
            cv2.imshow("image",tmp)
            cv2.waitKey(1)
                
                # cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP: # left button up event
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)            
        else:
            # if not (tmp is None):
            #     img = tmp.copy()
            w = x-ix
            h = y-iy
            # cv2.ellipse(img, ( (ix+w//2,iy+h//2), (w,h),0), (0,0,255),-1)
            cv2.ellipse(img, (ix+w//2,iy+h//2), (np.abs(w)//2,np.abs(h)//2),0,0,360, (0,0,255),-1)
            # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
            # cv2.circle(img,(x,y),5,(0,0,255),-1)
            cv2.imshow("image",img)
            
            
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)

cv2.imshow('image',img)
while(True):
    k = cv2.waitKey(100) & 0xFF
    if k == ord('m'):   # enter m
        mode = not mode
    elif k == 27:       # enter ESC
        break
    
    if cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE ) <1:
        break

cv2.destroyAllWindows()