from skimage import data
import cv2

# from skimage.color import rgb2gray
# from skimage import img_as_ubyte,img_as_float

cat   = data.chelsea()     # take the test image of cat!
print(f'{cat.shape=}')
cat   = cat[...,::-1]
# ---------------------
# def on_trackbar(val):
#     pass

cv2.namedWindow('test_cat', cv2.WINDOW_NORMAL) # 생략가능.
cv2.imshow('test_cat', cat)

# cv2.createTrackbar("trackbar","test_cat", 0, 100, on_trackbar)
while True:
    k = cv2.waitKey(10)
    if k & 0xFF == 27:  #check ESC
        break
    if cv2.getWindowProperty('test_cat', cv2.WND_PROP_VISIBLE) < 1:
        break
# k =cv2.waitKey(0) # 키 입력 무한 대기.
cv2.destroyAllWindows()