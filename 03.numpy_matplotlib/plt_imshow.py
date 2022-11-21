import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./img/wonyoung.jpg')

plt.imshow(img) # 이미지 표시
plt.show()