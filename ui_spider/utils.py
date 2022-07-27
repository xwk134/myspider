from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from urllib import request
from lxml import etree
import cv2
import random
import json

class JD_login():
    def create_chrome_driver(self, *, headless=False):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        browser = webdriver.Chrome(options=options)
        browser.execute_cdp_cmd(
            'Page.addScriptToEvaluateOnNewDocument',
            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
        )
        return browser

    def add_cookies(self, browser, cookie_file):
        with open(cookie_file, 'r') as file:
            cookies_list = json.load(file)
            for cookie_dict in cookies_list:
                browser.add_cookie(cookie_dict)

    def __init__(self):
        self.driver = self.create_chrome_driver()
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()

        self.driver.get('https://passport.jd.com')
        self.add_cookies(self.driver, 'jd_login.json')
        self.driver.get('https://order.jd.com/center/list.action')

        # self.driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F')
        #
        #
        # self.driver.find_element_by_xpath('//*[@class="login-tab login-tab-r"]/a').click()
        # self.driver.find_element_by_name('loginname').send_keys('13437061763')
        # self.driver.find_element_by_name('nloginpwd').send_keys('xwk970728')
        # self.driver.find_element_by_id('loginsubmit').click()
        time.sleep(15)
        # 获取cookie数据写入文件
        with open('jd_login.json', 'w') as file:
            json.dump(self.driver.get_cookies(), file)

    def get_images(self):
        info = self.driver.page_source
        #print(info)
        root_element = etree.HTML(info)
        link = root_element.xpath('//div[@class="JDJRV-img-wrap"]/div[1]/img/@src')[0]
        link1 = root_element.xpath('//div[@class="JDJRV-img-wrap"]/div[2]/img/@src')[0]
        request.urlretrieve(link, 'jdhkbj.png')
        request.urlretrieve(link1, 'jdhk.png')
        time.sleep(1)

    def juli(self):
        bj_rgb = cv2.imread('jdhkbj.png')
        bj_gray = cv2.cvtColor(bj_rgb, cv2.COLOR_BGR2GRAY)
        hk_rgb = cv2.imread('jdhk.png')
        res = cv2.matchTemplate(bj_rgb, hk_rgb, cv2.TM_CCOEFF_NORMED)
        lo = cv2.minMaxLoc(res)
        # print(lo[2][0])
        return lo[2][0]  # 识别返回滑动距离

    def get_tracks(self, distance):
        '''
        拿到移动轨迹，模仿人的滑动行为，先匀加速后减速
        匀加速运动
        :param distance: 需要移动的距离
        :return: 每0.3秒移动的距离
        '''
        # 初速度
        v0 = 0
        # 单位时间为0.3s来统计轨迹，轨迹即0.3s的位移
        t = 0.3
        # 位移/轨迹列表，列表内的一个元素代表0.3s的位移
        tracks = []
        # 当前的位移
        current = 0
        # 到达mid值开始减速
        mid = distance*4/5
        while current < distance:
            if current < mid:
                # 加速度越小，单位时间的位移越小，模拟的轨迹就越多越详细
                a = 2
            else:
                a = -3
            # 初速度
            v = v0
            # 0.3s时间内的位移
            s = v * t + 0.5 * a * (t ** 2)
            # 当前的位置
            current += s
            # 添加到轨迹列表
            tracks.append(round(s))
            # 速度已到达v,该速度作为下次的初速度
            v0 = v + a * t
        print(tracks)
        return tracks

    def get_track7(self, distance):
        """
        根据偏移量和手动操作模拟计算移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        tracks = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 时间间隔
        t = 0.2
        # 初始速度
        v = 0

        while current < distance:
            if current < mid:
                a = random.uniform(2, 5)
            else:
                a = -(random.uniform(12.5, 13.5))
            v0 = v
            v = v0 + a * t
            x = v0 * t + 1 / 2 * a * t * t
            current += x

            if 0.6 < current - distance < 1:
                x = x - 0.53
                tracks.append(round(x, 2))

            elif 1 < current - distance < 1.5:
                x = x - 1.4
                tracks.append(round(x, 2))
            elif 1.5 < current - distance < 3:
                x = x - 1.8
                tracks.append(round(x, 2))

            else:
                tracks.append(round(x, 2))

        print(tracks, sum(tracks))
        return tracks


    def jd_hk(self):
        x = self.juli()
        # 278:网页原图像素
        # 360:下载后尺寸
        x = int(x * 278 / 360)
        print(x)
        hk = self.driver.find_element_by_xpath('//div[@class="JDJRV-smallimg"]')
        action = ActionChains(self.driver)
        action.click_and_hold(hk).perform()
        tracks = self.get_track7(x)
        for track in tracks:
            action.move_by_offset(track, 0).perform()
        #action.move_by_offset(x, 0).perform()
        time.sleep(3)
        action.release(hk).perform()

jd = JD_login()
# jd.get_images()
# jd.juli()
# jd.jd_hk()

