import cv2

img = cv2.imread("20220715130039_68cc4.png", 0)  # 图像读取
#cv2.imshow('image', img)  # 图像显示
ret1, img1 = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
cv2.imshow('THRESH_BINARY', img1)
cv2.waitKey(0)  # 等待键入，参数为 0 表示无限等待。这里是为了方便查看效果，不使用的话，窗口会一闪而逝。
cv2.destroyAllWindows()  # 销毁所有显示窗口

