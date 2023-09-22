from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL.ImageEnhance import Sharpness
from PIL import ImageFilter


im = Image.open('E:\\test_image\\2.png')
print(np.max(im))
# 锐化效果
im.filter(ImageFilter.EDGE_ENHANCE)

r, g, b = im.split()  # 分割图像通道为R、G和B
r_old = np.linspace(0, 255, 11)   # 参考点
r_new = [0., 12.75, 25.5, 51., 76.5, 127.5, 178.5, 204., 229.5, 242.25, 255.]  # 参考点的新值

r1 = Image.fromarray((np.reshape(np.interp(np.array(r).ravel(), r_old, r_new),
                                 (im.height, im.width))).astype(np.uint8), mode='L')

plt.figure(figsize=(20,10))
plt.subplot(121)
plt.imshow(im)
plt.title('last image', size=20)
plt.axis('off')
im2 = Sharpness(im).enhance(3.0)
plt.subplot(122)
plt.imshow(im2)
plt.axis('off')
plt.title('with transformation', size=20)
plt.tight_layout()
plt.show()
im2.save('E:\\test_images\\4.png')
