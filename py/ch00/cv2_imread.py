import cv2

img = cv2.imread('../../images/lena.jpg')
print(type(img))
cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
