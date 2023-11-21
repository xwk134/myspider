import cv2
import numpy as np

img = cv2.imread("test.jpg")
cv2.imshow("test", img)
cv2.waitKey(10000)
