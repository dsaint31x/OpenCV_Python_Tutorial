from skimage import data

#from skimage.color import rgb2gray
#from skimage import img_as_ubyte,img_as_float

cat = data.chelsea()     # take the test image of cat!
astro = data.astronaut() # take the test image of astronaut!

print(f'{cat.shape=}')

# ---------------------
import cv2

# def on_trackbar(val):
#     pass


cv2.imshow('test_cat', cat)
# cv2.createTrackbar("trackbar","test_cat", 0, 100, on_trackbar)
while True:
    k = cv2.waitKey(10)
    if k & 0xFF == 27:
        break
    if cv2.getWindowProperty('test_cat', cv2.WND_PROP_VISIBLE) < 1:
        break
cv2.destroyAllWindows()

# ---------------------
# matplotlib 00
import matplotlib.pyplot as plt

figure, ax = plt.subplots(1,1)
ax.imshow(cat)
ax.set_xticks([]); ax.set_yticks([])
plt.show()

# ---------------------
# cv2.cvtColor 
# cv2.imshow
cat_cv   = cv2.cvtColor(cat  ,cv2.COLOR_RGB2BGR)  #RGB -> BGR
astro_cv = cv2.cvtColor(astro,cv2.COLOR_RGB2BGR)  #RGB -> BGR
cat_gray = cv2.cvtColor(cat  ,cv2.COLOR_RGB2GRAY) #RGB -> Gray-scale

cv2.imshow('cat_cv'  ,cat_cv  )
cv2.imshow('astro_cv',astro_cv)
cv2.imshow('gray_cat',cat_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# for google colab
# cv2_imshow(cat_cv)
# cv2_imshow(astro_cv)
# cv2_imshow(gray_cat)

