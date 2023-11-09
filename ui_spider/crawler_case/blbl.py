import datetime

from selenium import webdriver
import os
import ddddocr
import time
import requests
from lxml import etree
import mysql.connector
from selenium.webdriver.common.by import By

cat = input("请输入喵星人下分类名称：")
# 获取当前年份
current_datetime = datetime.datetime.now()
current_year = current_datetime.year

for x in range(1):
    driver = webdriver.Edge()
    driver.implicitly_wait(100)
    driver.maximize_window()
    url = 'https://www.bilibili.com/v/animal/cat/?spm_id_from=333.1007.0.0'
    driver.get(url)
    if cat == "踩奶":

        # 踩奶
        time.sleep(1)
        driver.find_element(By.XPATH, value="/html/body/div[2]/div/main/div/div[1]/button[3]").click()
    elif cat == "萌萌哒":
        # 萌萌哒
        time.sleep(1)
        driver.find_element(By.XPATH, value="/html/body/div[2]/div/main/div/div[1]/button[4]").click()
    elif cat == "小奶猫":
        # 小奶猫
        time.sleep(1)
        driver.find_element(By.XPATH, value="/html/body/div[2]/div/main/div/div[1]/button[6]").click()
    elif cat == "治愈系":
        # 治愈系
        time.sleep(1)
        driver.find_element(By.XPATH, value="/html/body/div[2]/div/main/div/div[1]/button[7]").click()
        time.sleep(1)
    else:
        print("输入分类名称不存在")
        break
    time.sleep(1)
    print("开始爬取")
    info = driver.page_source
    # print(info)
    with open('info.html', 'w', encoding='utf-8') as fp:
        fp.write(info)
    root_element = etree.parse('info.html', etree.HTMLParser())
    links = root_element.xpath('//div[@class="bili-video-card"]/div[2]/a/@href')
    texts = root_element.xpath('//div[@class="bili-video-card"]/div[2]/div/div/h3/@title')
    usernames = root_element.xpath('//div[@class="bili-video-card"]/div[2]/div/div/div/a/span[1]/@title')
    times = root_element.xpath('//div[@class="bili-video-card"]/div[2]/div/div/div/a/span[2]/text()')
    print(texts)
    print(links)
    print(times)
    for link in range(0, len(links) - 1):
        text = texts[link]
        username = usernames[link]

        time = str(current_year) + times[link]
        link = 'https:' + links[link]
        content = '视频名称：' + text, '视频地址：' + link, '发布人：' + username, '发布时间：' + time
        print('视频名称：' + text, '视频地址：' + link, '发布人：' + username, '发布时间：' + time)
        with open(cat + '.txt', 'a', encoding='utf-8') as fp:
            fp.write(str(content)+'\n')
