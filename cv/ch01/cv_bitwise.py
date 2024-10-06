import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_heatmap(ax,title,img):
  ax.set_title(title)
  sns.heatmap(img,annot=True,fmt='.2f',cmap=plt.cm.gray, ax =ax, 
              cbar=False, linewidth=0, linecolor='blue')
  for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor('blue')
    spine.set_linewidth(2)

img_0 = np.zeros(shape=(2,2), dtype=np.uint8)
img_0[:,:1]= 255 
img_1 = np.zeros_like(img_0)
img_1[:1,:]= 255

d_and = cv2.bitwise_and(img_0,img_1)
d_or  = cv2.bitwise_or (img_0,img_1)
d_not = cv2.bitwise_not(img_0)
d_xor = cv2.bitwise_xor(img_0,img_1)

fig, axs = plt.subplots(1,6, figsize=(12,2))
show_heatmap(axs[0], 'img_0', img_0)
show_heatmap(axs[1], 'img_1', img_1)
show_heatmap(axs[2], 'd_and', d_and)
show_heatmap(axs[3], 'd_or' , d_or)
show_heatmap(axs[4], 'd_not(img_0)', d_not)
show_heatmap(axs[5], 'd_xor', d_xor)
plt.tight_layout()
plt.show()