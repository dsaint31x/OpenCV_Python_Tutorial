import cv2
import numpy as np
url = 'https://raw.githubusercontent.com/dsaint31x/OpenCV_Python_Tutorial/master/images/opencv_logo.png'

import requests

t0 = requests.get(url)# requests.models.Response 
t1 = t0.content       # bytes (immutable) 
t2 = bytearray(t1)    # bytearray (mutable)
t3 = np.asarray(t2, dtype=np.uint8) #ndarray
img = cv2.imdecode(t3, cv2.IMREAD_UNCHANGED)

cv2.imwrite('opencv_logo.png', img)

print(f'{img.shape=}')
# cv2에서는 투명 배경을 검은색으로 표시하는데, 이 경우 검정색 글자가 안보임.
# 때문에 alpha 채널을 읽어서 투명 배경을 흰색으로 변환.
if len(img) > 3 and img.shape[2] == 4:
    bgr = img[:,:,:3]
    alpha = img[:,:,3]
    
    w_bg = np.ones_like(bgr, dtype=np.uint8) * 255
    mask = alpha[:,:,np.newaxis] / 255.
    img0 = bgr*mask + w_bg*(1.-mask)
    img1 = cv2.convertScaleAbs(bgr*mask + w_bg*(1-mask))
else:
    img1 = img
    
cv2.imshow('test1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

