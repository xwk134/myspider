from threading import Thread
import requests
import json
import time
import mysql.connector
import datetime

infolist = []
infolist1 = []
infolist2 = []
def grabOnePage(url):
    print('获取请求地址：', url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Cookie': 'AUTHOR_PROJECT=yidejia; AUTHOR_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4OTJmNjNmMTIzNTM0M2E4YjJiZjZlMmFkN2Y0ZDNhMyIsInN1YiI6IjIwMTkwODQiLCJpc3MiOiJodHRwczpcL1wvb2EuamluZ3podWFuLmNuIiwiYXVkIjoiIiwiaWF0IjoxNjU5MTAzMjc1LCJleHAiOjE2NjE2OTUyNzUsInVzZXJfaWQiOiIyMDE5MDg0Iiwia2V5IjoiY29sbGVnZSJ9.-Oy0VNfaXTzQgHr1kZjV0wBdbNBQsNtsG_IQfTXMg5c'
    }
    res = requests.get(url=url, headers=headers, timeout=20)
    res.encoding = 'gb2312'
    list = json.loads(res.text)
    print(list)
    list1 = list['data']
    print(list1)

    list2 = []



    for idx in range(len(list1)):
        dict = {
            'id1': list1[idx]['id']  # 一级类目id
        }
        list2.append(dict)
    print(list2)

    list22 = []
    list6 = []
    for x in range(len(list1)):
        list11 = list['data'][x]['child']
        print(list11)


        for i in range(len(list11)):
            dict = {
                'id2': list11[i]['id']  # 二级类目id
            }
            bb = list11[i]['child']
            print(bb)

            for b in range(len(bb)):
                dict = {
                    'id6': bb[b]['id']  # 三级类目id
                }
                list6.append(dict)
            print(list6)

            list22.append(dict)
    print(list22)





    row = len(list2)
    print(f'本次共抓取到{row}条一级类目id')
    for x in range(2, row+2):
        for a, b in list2[x-2].items():
            infolist.append(b)


    row = len(list22)
    print(f'本次共抓取到{row}条二级类目id')
    for x in range(2, row + 2):
        for a, b in list22[x - 2].items():
            infolist1.append(b)

    row = len(list6)
    print(f'本次共抓取到{row}条三级类目id')
    for x in range(2, row + 2):
        for a, b in list6[x - 2].items():
            infolist2.append(b)

theadlist = []
for pageIdx in range(1, 2):
    url = f'https://xyapi.jingzhuan.cn/api/newxy/public/article/category?to_show=1&ts=1659153036.233&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4OTJmNjNmMTIzNTM0M2E4YjJiZjZlMmFkN2Y0ZDNhMyIsInN1YiI6IjIwMTkwODQiLCJpc3MiOiJodHRwczpcL1wvb2EuamluZ3podWFuLmNuIiwiYXVkIjoiIiwiaWF0IjoxNjU5MTAzMjc1LCJleHAiOjE2NjE2OTUyNzUsInVzZXJfaWQiOiIyMDE5MDg0Iiwia2V5IjoiY29sbGVnZSJ9.-Oy0VNfaXTzQgHr1kZjV0wBdbNBQsNtsG_IQfTXMg5c&project=yidejia'
    time.sleep(1)
    thread = Thread(target=grabOnePage,
                    args=(url,)
                    )
    thread.start()
    # 把线程对象都存储到 threadlist中
    theadlist.append(thread)

for thread in theadlist:
    thread.join()
print(theadlist)
print(infolist)
print(infolist1)
print(infolist2)
listdata = infolist+infolist1+infolist2
print(listdata)

for x in range(1, 11):
    for y in range(0, len(listdata)):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Cookie': 'AUTHOR_PROJECT=yidejia; AUTHOR_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4OTJmNjNmMTIzNTM0M2E4YjJiZjZlMmFkN2Y0ZDNhMyIsInN1YiI6IjIwMTkwODQiLCJpc3MiOiJodHRwczpcL1wvb2EuamluZ3podWFuLmNuIiwiYXVkIjoiIiwiaWF0IjoxNjU5MTAzMjc1LCJleHAiOjE2NjE2OTUyNzUsInVzZXJfaWQiOiIyMDE5MDg0Iiwia2V5IjoiY29sbGVnZSJ9.-Oy0VNfaXTzQgHr1kZjV0wBdbNBQsNtsG_IQfTXMg5c'
        }
        url = f'https://xyapi.jingzhuan.cn/api/newxy/public/article/category/id?category_id={listdata[y]}&pageindex={x}&pagesize=10&sort=0&ts=1659173565.736&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4OTJmNjNmMTIzNTM0M2E4YjJiZjZlMmFkN2Y0ZDNhMyIsInN1YiI6IjIwMTkwODQiLCJpc3MiOiJodHRwczpcL1wvb2EuamluZ3podWFuLmNuIiwiYXVkIjoiIiwiaWF0IjoxNjU5MTAzMjc1LCJleHAiOjE2NjE2OTUyNzUsInVzZXJfaWQiOiIyMDE5MDg0Iiwia2V5IjoiY29sbGVnZSJ9.-Oy0VNfaXTzQgHr1kZjV0wBdbNBQsNtsG_IQfTXMg5c&project=yidejia'
        time.sleep(1)
        res = requests.get(url=url, headers=headers, timeout=20)
        res.encoding = 'gb2312'
        list = json.loads(res.text)
        list44 = len(list['data'])
        print(list44)

        if list44 == 0:
            print('获取数据为空')

        else:
            list33 = len(list['data']['data'])
            print(list33)
            if list33 == 0:
                print('获取数据为空')
            else:
                print(list)
                id3 = list['data']['data']  # 视频列表
                print(id3)
                for a in range(0,len(id3)):
                    id4 = list['data']['data'][a]['id']  # 视频id
                    print(id4)
                    url = f'https://xyapi.jingzhuan.cn/api/newxy/public/article/id?id={id4}&ts=1659315039.32&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4OTJmNjNmMTIzNTM0M2E4YjJiZjZlMmFkN2Y0ZDNhMyIsInN1YiI6IjIwMTkwODQiLCJpc3MiOiJodHRwczpcL1wvb2EuamluZ3podWFuLmNuIiwiYXVkIjoiIiwiaWF0IjoxNjU5MTAzMjc1LCJleHAiOjE2NjE2OTUyNzUsInVzZXJfaWQiOiIyMDE5MDg0Iiwia2V5IjoiY29sbGVnZSJ9.-Oy0VNfaXTzQgHr1kZjV0wBdbNBQsNtsG_IQfTXMg5c&project=yidejia'
                    res = requests.get(url=url, headers=headers, timeout=20)
                    res.encoding = 'gb2312'
                    list1 = json.loads(res.text)
                    print(list1)
                    if list1['code'] == 200:
                        title = list1['data']['data']['title']
                        print(title)
                        author = list1['data']['data']['author']
                        print(author)
                        audio = list1['data']['data']['audio_url']
                        print(audio)
                        images = list1['data']['data']['img_url']
                        print(images)
                        ppt = list1['data']['data']['courseware_url']
                        print(ppt)
                        deta1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        print(deta1)
                        videom3u8 = 'https:'+list1['data']['data']['content']
                        print(videom3u8)
                        print(videom3u8[-4:])

                        #开始写入数据
                        mydb = mysql.connector.connect(
                            host="192.168.31.118",
                            user="root",
                            passwd="root",
                            database="bootdo",
                            buffered=True
                        )
                        mycursor = mydb.cursor()
                        if audio==None:
                            print('此视频没有音频')
                            if videom3u8[-4:] == 'm3u8':
                                sql = "INSERT IGNORE INTO jzxy_jzxyname (title, author, image, ppt, deta, videom3u8) VALUES (%s,%s,%s,%s,%s,%s)"
                                val = (title, author, images, ppt, deta1, videom3u8)
                            elif videom3u8[-4:] == '.mp4':
                                sql = "INSERT IGNORE INTO jzxy_jzxyname (title, author, video, image, ppt, deta) VALUES (%s,%s,%s,%s,%s,%s)"
                                val = (title, author, videom3u8, images, ppt, deta1)
                            else:
                                print('该数据为文章类型')
                        else:
                            if videom3u8[-4:] == 'm3u8':
                                sql = "INSERT IGNORE INTO jzxy_jzxyname (title, author, audio, image, ppt, deta, videom3u8) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                                val = (title, author, audio, images, ppt, deta1, videom3u8)
                            elif videom3u8[-4:] == '.mp4':
                                sql = "INSERT IGNORE INTO jzxy_jzxyname (title, author, video, audio, image, ppt, deta) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                                val = (title, author, videom3u8, audio, images, ppt, deta1)
                            else:
                                print('该数据为文章类型')
                        try:
                            mycursor.execute(sql, val)
                            mydb.commit()  # 数据表内容有更新，必须使用到该语句
                        finally:
                            print("数据插入成功")

print('主线程结束')


