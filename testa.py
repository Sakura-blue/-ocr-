import cv2
import random

# # 读取图片
img = cv2.imread('cheem.png')
# print(img)
# 获取图片尺寸
height, width = img.shape[:2]

# 计算旋转中心点
center = (width // 2, height // 2)

# 设置旋转角度
angle = random.randint(-30, 30)
# angle = 30

# 计算旋转矩阵
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# 执行旋转操作
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

# 保存旋转后的图片
# cv2.imwrite('rotated_img.jpg', rotated_img)

# 显示旋转后的图片（可选）
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
