import ddddocr

# ocr = ddddocr.DdddOcr(old=True)
# with open('weibo.png', 'rb') as f:
#     img_bytes = f.read()
# res = ocr.classification(img_bytes)
# print('识别出的验证码为：' + res)

det = ddddocr.DdddOcr(det=False, ocr=False)
with open('jdhk.png', 'rb') as f:
    target_bytes = f.read()
with open('jdhkbj.png', 'rb') as f:
    background_bytes = f.read()
res = det.slide_match(target_bytes, background_bytes, simple_target=True)
print(res)

