from threading import Thread
from requests_html import HTMLSession
import requests
import os

infolist = []
def grabOnePage(url):
    print('获取请求地址：', url)
    session = HTMLSession()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
    }
    res = session.get(url=url, headers=headers, timeout=10)
    res.encoding = 'gb2312'
    #print(res.html.html)
    titles = res.html.xpath("//a[@class='p-title']/text()")
    links = res.html.xpath("//a[@class='p-title']/@href")
    for x in range(0, len(titles)):
        print('PPT下载地址：', titles[x], 'https://www.ypppt.com'+links[x])

        res1 = session.get(url='https://www.ypppt.com'+links[x], headers=headers, timeout=10)
        res1.encoding = 'gb2312'
        titles1 = res1.html.xpath("//a[@class='down-button']/text()")
        links1 = res1.html.xpath("//a[@class='down-button']/@href")
        print('下载链接地址：', titles1[0], 'https://www.ypppt.com' + links1[0])

        res2 = session.get(url='https://www.ypppt.com' + links1[0], headers=headers, timeout=10)
        res2.encoding = 'gb2312'
        titles2 = res2.html.xpath("//ul[@class='down clear']/li[1]/a/text()")
        links2 = res2.html.xpath("//ul[@class='down clear']/li[1]/a/@href")
        print('下载链接：', titles2[0], links2[0])

        conet = requests.get(links2[0], headers)
        dir_name = 'D:\\优品PPT\\'
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        with open(dir_name+titles[x] + '.rar', mode='wb') as f:
            f.write(conet.content)

theadlist = []
for pageIdx in range(2, 10):
    url = f'https://www.ypppt.com/moban/zongjie/list-{pageIdx}.html'
    thread = Thread(target=grabOnePage,
                    args=(url,)
                    )
    thread.start()
    # 把线程对象都存储到 threadlist中
    theadlist.append(thread)
for thread in theadlist:
    thread.join()
print('线程数：', len(theadlist))
