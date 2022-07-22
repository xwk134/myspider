import requests
from bs4 import BeautifulSoup
#反反爬虫机制：设置请求头消息User-Agent模拟浏览器（火狐浏览器）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
}
#输入想获取的网页
url = 'https://movie.douban.com/chart'
#创建一个名为html的response对象
html = requests.get(url=url, headers=headers)
#防止乱码
html.encoding = 'utf-8'
#判断是否反爬虫
#print(html.status_code)
soup = BeautifulSoup(html.text, 'lxml')
print(soup)
for a in soup.find_all(class_='nbg'):
    print(a['title'], a['href'])
