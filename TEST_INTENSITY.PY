import cv2
import numpy as np
from skimage.draw import polygon2mask

filename = 'your_image_file.png'
img = cv2.imread(filename)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_r = img[:, :, 2]
img_g = img[:, :, 1]
img_b = img[:, :, 0]

# 使用者需提供 ROI 區域的座標
xy = [...]  # 這應該是一個包含多個（x，y）元組的列表

binary_image = polygon2mask(img_gray.shape, np.array(xy))

roi = img_g.copy()
roi[~binary_image] = 0

green = np.where(roi > 0)
total_intensity = np.sum(roi) / 255 / len(green[0])
g = len(green[0])

roi = img_g.copy()
roi[binary_image] = 0
bgreen = np.where(roi >= 0)
b_total_intensity = np.sum(roi) / 255 / len(bgreen[0])
bg = len(bgreen[0])

print(total_intensity)
print(b_total_intensity)
ri = (total_intensity - b_total_intensity) / b_total_intensity
print(ri)
