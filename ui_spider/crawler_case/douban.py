from requests_html import HTMLSession

# 定义会话Session
session = HTMLSession()

url = "https://movie.douban.com/"
# 发送GET请求
r = session.get(url)

# 通过CSS Selector定义li元素，".title"代表class属性
# first=True代表获取第一个元素
print(r.html.find('li.title', first=True).text)
# 输出当前标签的属性值
print(r.html.find('li.title', first=True).attrs)

print("________分割线________")
# 查找特定文本元素
# 如果元素所在的HTML里含有containing的属性值即可提取
for name in r.html.find('li.title', containing="多力特的奇幻"):
    # 输出电影名
    print(name.text)
print("________分割线________")

# 查找全部电影名
for name in r.html.find("li.title"):
    # 输出电影名
    print(name.text)
    # 输出电影名所在标签的属性值
    print(name.attrs)
print("________分割线________")

# 通过Xpath Selector定位ul标签
x = r.html.xpath('//*[@id="screening"]/div[2]/ul/li[6]/ul')
for name in x:
    print(name.text)
print("________分割线________")
# search()通过关键字查找内容
# 一个{}代表一个内容，内容可为中文或英文等
print(r.html.search("多力特的奇幻..."))
print("________分割线________")
# search_all()通过关键字查询整个网页符合的内容
print(r.html.search_all("大话西游{}{}"))



