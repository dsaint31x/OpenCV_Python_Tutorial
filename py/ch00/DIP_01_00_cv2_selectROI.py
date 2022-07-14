 
import os
#print(os.getcwd())
#os.chdir('~/dip/py/ch00')


import cv2

fstr = '/mnt/d/gachon/lecture/OpenCV_Python_Tutorial/images/messi5.jpg'
img = cv2.imread(fstr)
print(f'01: img.shape={img.shape}')



x, y, w, h = cv2.selectROI('img1', img,
             True, #showCrossHair
             True #fromCenter
)
                        
if w and h:
    print(f'x:{x: 3d},y:{y: 3d},w:{w: 3d},h:{h: 3d}')
    roi = img[y:y+h, x:x+w].copy()
    cv2.imshow('roi', roi)
    cv2.moveWindow('roi', 0,0)
    cv2.imwrite('roi.jpg',roi)
    print(f'03: img.shape={img.shape}')


print(f'02: img.shape={img.shape}')


cv2.imshow('img2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

