import cv2
import numpy as np
url = 'https://raw.githubusercontent.com/dsaint31x/OpenCV_Python_Tutorial/master/images/opencv_logo.png'


img = cv2.imread(url, cv2.IMREAD_UNCHANGED)
if not img is None:
    print(f'{img.shape=}')

    cv2.imshow('test0', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import requests

t0 = requests.get(url)# requests.models.Response 
print(f'{type(t0)=}')
t1 = t0.content       # byte (immutable) 
print(f'{type(t1)=}') 
t2 = bytearray(t1)    # bytearray (mutable)
print(f'{type(t2)=}')

t3 = np.asarray(t2, dtype=np.uint8)
print(f'{type(t3)=}') # ndarray
img = cv2.imdecode(t3, cv2.IMREAD_UNCHANGED)
print(f'{img.shape=}')
cv2.imshow('test1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('opencv_logo.png', img)