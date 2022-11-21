import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 = cv2.imread('./img/wonyoung.jpg')
img2 = cv2.imread('./img/wonyoung2.png')
img3 = cv2.imread('./img/wonyoung3.jpg')


plt.subplot(1,3,1)  # 1행 3열 중에 1번째
plt.imshow(img1[:,:,(2,1,0)])
plt.xticks([]); plt.yticks([])

plt.subplot(1,3,2)  # 1행 3열 중에 2번째
plt.imshow(img2[:,:,(2,1,0)])
plt.xticks([]); plt.yticks([])

plt.subplot(1,3,3)  # 1행 3열 중에 3번째
plt.imshow(img3[:,:,(2,1,0)])
plt.xticks([]); plt.yticks([])

plt.show()