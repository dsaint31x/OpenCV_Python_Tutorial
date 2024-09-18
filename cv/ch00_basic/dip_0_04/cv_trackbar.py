import cv2
import numpy as np

def nothing(x):
    pass

def on_brightness_change(val):
    global brightness 
    brightness = val-100 # trackbar의 값을 [-100,100] 으로

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0:OFF / 1:ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)
 
# create brightness for testing callback func
brightness = 0
cv2.createTrackbar('Brightness+100', 'image', brightness+100, 200, on_brightness_change)


while(1):

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
        img = cv2.convertScaleAbs(img, alpha=1., beta=brightness)
        cv2.putText(img, f'Brightness: {brightness}', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow('image',img)
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
    if cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE ) <1:
        break

cv2.destroyAllWindows()