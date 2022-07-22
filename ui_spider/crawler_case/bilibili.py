#encoding:utf-8
import time
import threadpool
import random
import threading
from threading import Thread
from requests_html import HTMLSession
import re
import os
import json
import requests
import shutil
import subprocess
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon

class Stats():
    def __init__(self):
        qfile_stats = QFile("C:/Users/推广部/PycharmProjects/untitled/jktest/test2.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.pushButton.clicked.connect(self.new_printFunc)
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.buttonGroup.buttonClicked.connect(self.handle)
        self.ui.buttonGroup_2.buttonClicked.connect(self.handle1)


    def handle1(self, item):
        print("选中项的id为：", item.group().checkedId())  # 选中选在 选项组中的id。
        print("选中项的名称为：%s\n" % item.text())  # 选中项的文本内容

    def handle(self, item):
        print("选中项的id为：", item.group().checkedId())  # 选中选在 选项组中的id。
        print("选中项的名称为：%s\n" % item.text())  # 选中项的文本内容

    def clear(self):
        self.ui.textBrowser.clear()

    def sayhello(self, url):  #执行方法

        sleep_seconds = random.randint(1, 3)
        print('线程名称：%s，参数：%s，睡眠时间：%s' % (threading.current_thread().name, url, sleep_seconds))
        time.sleep(sleep_seconds)
        session = HTMLSession()
        login_url = 'https://passport.bilibili.com/x/passport-login/web/login'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }

        data = {
            'username': '13437061763',
            'password': 'EE5aHFc4AFcG6IWGlP1JaqqB8G2ZcZw0%2BALRR0eKtdv3Iv8Bm3AawwfXE3%2FruRjdFM8iAaUYzV0cP9Bfr30H1M7eAoUmruVXV3e%2FOAoRv6iqHdJDSWaqqSgl7xGciCYFeOt6OLqolCouY7nulhFntG5p8n%2FEaiKbEI23dMREQA%3D%3D',
            'keep': '0',
            'source': 'main_mini',
            'token': 'e012eb84a8b2454c9846da555d232254',
            'go_url': 'https%3A%2F%2Fwww.bilibili.com%2F',
            'challenge': '39e5966a24a84660b0e50764d89d1acb',
            'validate': 'bf893d2bdd1434baadf36c5a0992dccd',
            'seccode': 'bf893d2bdd1434baadf36c5a0992dccd%7Cjordan'
        }
        # 使用快代理
        proxies = {
            'http': '202.55.5.209:8090'
        }
        res = session.post(url=login_url, headers=headers, proxies=proxies, data=data)
        print(res.status_code)
        if res.status_code == 200:
            print('登录成功')
        else:
            res = session.post(url=login_url, headers=headers, proxies=proxies, data=data)
            print('登录失败')
        print('正在爬取：', threading.current_thread().name+url)
        self.ui.textBrowser.append(f'正在爬取：{url}')
        info = session.get(url=url, headers=headers, proxies=proxies)
        print(info.status_code)
        if info.status_code == 200:
            print('请求成功')
        else:
            info = session.get(url=url, headers=headers, proxies=proxies)
            print('登录失败')
        with open('info.html', 'w', encoding='utf-8') as fp:
            fp.write(info.html.html)
        text = info.html.html
        #print(text)
        p1 = re.compile(r'<script>window.__playinfo__=(.*?)</script>', re.S)
        video = re.findall(p1, text)[0]
        txt = json.loads(video)
        aa = re.compile(r'<script>window.__INITIAL_STATE__=(.*?);', re.S)
        bb = re.findall(aa, text)[0]
        titlelist = json.loads(bb)
        #print(titlelist)
        num = url.split('=', 1)
        title = titlelist['videoData']['pages'][int(num[1]) - 1]['part']
        print('视频标题：', num[1] + '_' + title)
        title2 = titlelist['videoData']['title']
        print('课程标题：', title2)
        self.ui.textBrowser.append(f'课程标题：{title2}')
        audio_url = txt['data']['dash']['audio'][0]['backupUrl'][0]
        #print(audio_url)
        video_url = txt['data']['dash']['video'][0]['backupUrl'][0]
        #print(video_url)
        video_list = [audio_url, video_url]
        # 保持会话状态，在head中添加键值对:referer，存放上一次的会话的url,所以需要一个新的header
        headers2 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
            'Referer': url
        }
        # 下载保存音频和视频两种文件，MP3格式和MP4格式
        titles = num[1] + '_' + title
        print('开始下载音频', titles)
        self.ui.textBrowser.append(f'开始下载音频：{title}')
        r3 = requests.get(url=video_list[0], headers=headers2)
        audio_data = r3.content
        with open(title + '(audio).mp3', mode='wb') as f:
            f.write(audio_data)
        print('音频下载完成', titles)
        self.ui.textBrowser.append(f'音频下载完成：{title}')
        print('开始下载视频', titles)
        self.ui.textBrowser.append(f'开始下载视频：{title}')
        r4 = requests.get(url=video_list[1], headers=headers2)
        video_data = r4.content
        with open(title + '(video).mp4', mode='wb') as f:
            f.write(video_data)
        print('视频下载完成', titles)
        self.ui.textBrowser.append(f'视频下载成功：{title}')
        r3.close()
        r4.close()
        video = title + "(video).mp4"
        audio = title + "(audio).mp3"
        print('开始合成', titles)
        self.ui.textBrowser.append(f'开始合成：{title}')
        cmd = f'ffmpeg -i {video} -i {audio} -acodec copy -vcodec copy {titles + ".mp4"}'
        aa = subprocess.call(cmd, shell=True)
        if aa == 0:
            print(aa)
            print('视频合成成功', titles)
            self.ui.textBrowser.append(f'视频合成成功：{title}')
            os.remove(video)
            os.remove(audio)
            dir_name = f'D:\\{title2}\\'
            # 判断 D盘下是否存在 video目录，如果不存在该目录，则创建 video目录
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
            try:
                shutil.move(titles + ".mp4", dir_name)
                print('视频移动成功', titles)
                self.ui.textBrowser.append(f'视频移动成功：{title}')
            except:
                os.remove(titles + ".mp4")
                print('视频已存在', titles)
                self.ui.textBrowser.append(f'视频已存在：{title}')
        else:
            os.remove(video)
            os.remove(audio)
            print(aa)
            print('视频合成失败', titles)
            self.ui.textBrowser.append(f'视频合成失败：{title}')

    def task(self):  #主任务
        num = self.ui.textEdit.toPlainText()
        one = self.ui.textEdit_2.toPlainText()
        link = self.ui.textEdit_3.toPlainText()
        # number = self.ui.spinBox.value()
        name_list = []    #总共需要执行线程数
        for pageIdx in range(1, int(num)+1):
            url = link+str(pageIdx)
            name_list.append(url)
        start_time = time.time()    #开始时间
        pool = threadpool.ThreadPool(int(one))     #创建线程数
        #创建请求列表
        requests = threadpool.makeRequests(self.sayhello, name_list)
        for req in requests:
            pool.putRequest(req)    #将每个请求添加到线程池中
        pool.wait()  #等待线程执行完后再执行主线程
        print('总共运行时间：%d second' % (time.time()-start_time))
        self.ui.textBrowser.append('总共运行时间：%d second' % (time.time()-start_time))
        self.ui.textBrowser.append(f'共采集视频数：{int(num)}  视频保存在D盘')

    def new_printFunc(self):  # 新线程入口函数
        thread = Thread(target=self.task)
        thread.start()

# pyinstaller bilibili.py -p C:\Users\推广部\PycharmProjects\pythonProject\venv\Lib\site-packages --add-data="test2.ui;." --noconsole --hidden-import PySide2.QtXml --icon="logo.ico"

# https://www.bilibili.com/video/BV1Yh411o7Sz?p=
app = QApplication([])
# 加载 icon
app.setWindowIcon(QIcon('logo.ico'))
stats = Stats()
stats.ui.show()
app.exec_()
