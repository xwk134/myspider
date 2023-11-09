from selenium import webdriver
import os
import ddddocr
import time
import requests
from lxml import etree
import mysql.connector
for x in range(1):
    driver = webdriver.Edge()
    driver.implicitly_wait(100)
    driver.maximize_window()
    url = 'https://weibo.com/login.php'
    driver.get(url)
    driver.find_element_by_id('loginname').click()
    driver.find_element_by_id('loginname').clear()
    time.sleep(1)
    driver.find_element_by_id('loginname').send_keys('13437061763')
    driver.find_element_by_name('password').send_keys('xwk1343706')
    try:
        driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
        time.sleep(2)
        info = driver.page_source
        #print(info)
        root_element = etree.HTML(info)
        link = root_element.xpath('//div[@class="info_list verify clearfix"]/a/img/@src')[0]
        print(link)
        conet = requests.get(link)
        dir_name = 'D:\\验证码\\'
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        with open(dir_name + 'weibo.png', mode='wb') as f:
            f.write(conet.content)
        time.sleep(1)
        ocr = ddddocr.DdddOcr()
        with open(dir_name + 'weibo.png', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        print('识别出的验证码为：' + res)
        driver.find_element_by_name('verifycode').send_keys(res)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    finally:
        time.sleep(1)
        currentWin = driver.current_window_handle
        handles = driver.window_handles
        print(handles)
        for i in handles:
            if currentWin == i:
                continue
            else:
                # 将driver与新的页面绑定起来
                driver = driver.switch_to.window(i)
        #driver.find_element_by_link_text('最新微博').click()
        driver.find_element_by_xpath('//a[@class="ALink_default_2ibt1"]/button').click()
        time.sleep(3)
        for z in range(1, 5):
            a = 5-z
            js = f"window.scrollTo(0,document.body.scrollHeight/{a})"
            driver.execute_script(js)
            time.sleep(1)
            info = driver.page_source
            #print(info)
            with open('info.html', 'w', encoding='utf-8') as fp:
                fp.write(info)
            root_element = etree.HTML(info)
            txts = root_element.xpath('//div[@class="woo-box-item-flex"]/div[1]/div[2]')
            for txt in range(0, len(txts)-1):

                # 开始写入数据
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="admin",
                    database="test",
                    buffered=True
                )
                mycursor = mydb.cursor()

                # 创建数据表，设置唯一索引去重
                # mycursor.execute("CREATE TABLE weibo"
                #                  " (id INT AUTO_INCREMENT PRIMARY KEY comment '主键',"
                #                  "title VARCHAR(255) comment '文章标题',"
                #                  "link VARCHAR(255) comment '文章地址',"
                #                  "UNIQUE (title, link)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8")

                title = txts[txt].text
                print(title)
                link = 'https:' + root_element.xpath('//a[@class="ALink_none_1w6rm"]/@href')[txt]
                print(link)
                try:
                    sql = "INSERT IGNORE INTO weibo (title, link) VALUES (%s,%s)"
                    val = (title, link)
                    mycursor.execute(sql, val)
                    mydb.commit()  # 数据表内容有更新，必须使用到该语句
                finally:
                    print('当前数据插入成功')
            print(f"第{z}页数据插入成功")
            time.sleep(1)

        #driver.quit()

