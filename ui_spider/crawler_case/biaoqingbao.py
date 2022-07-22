import requests
from requests_html import HTMLSession
# 文件保存目录
path = 'C:/Users/推广部/Desktop/表情包/'
# 保存为.jpg格式
def save(respone, name):
    with open(path + name + '.jpg', 'wb') as f:
        f.write(respone)
# 保存为.gif格式
def savegif(respone, name):
    with open(path + name + '.gif', 'wb') as f:
        f.write(respone)
def main():
    # 爬取表情包图片
    for i in range(2, 201):
        b = '/lists/page/' + str(i) + '.html'
        url = "https://fabiaoqing.com/biaoqing"+b
        session = HTMLSession()
        r = session.get(url)
        # print(r.html.html)
        # 直接定位到img标签,具体分析，获取相应的数据
        # print(r.html.find('img'))
        result = r.html.xpath('//*[@class="tagbqppdiv"]/a/img')
        # 下载图片
        for idx in range(len(result)):
            try:
                temp_result = result[idx].attrs
                print(temp_result)
                image_name = temp_result['title']
                img_url = temp_result['data-original']
                print('第%d个，url:%s' % (idx + 1, img_url))
                connet = requests.get(img_url, timeout=15)
                # 判断文件格式
                if (img_url[-3:] == 'jpg'):
                    save(connet.content, image_name)
                else:
                    savegif(connet.content, image_name)
            except Exception as e:
                print(e)
        print('第:', i, '页表情包下载完成')

if __name__ == "__main__":
    main()
