from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from urllib import request
from lxml import etree

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

    def __init__(self):
        self.driver = self.create_chrome_driver()
        self.driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F')
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@class="login-tab login-tab-r"]/a').click()
        self.driver.find_element_by_name('loginname').send_keys('13437061763')
        self.driver.find_element_by_name('nloginpwd').send_keys('xwk970728')
        self.driver.find_element_by_id('loginsubmit').click()
        time.sleep(1)

    def get_images(self):
        info = self.driver.page_source
        #print(info)
        self.root_element = etree.HTML(info)
        link = self.root_element.xpath('//div[@class="JDJRV-img-wrap"]/div[1]/img/@src')[0]
        link1 = self.root_element.xpath('//div[@class="JDJRV-img-wrap"]/div[2]/img/@src')[0]
        request.urlretrieve(link, 'jdhkbj.png')
        request.urlretrieve(link1, 'jdhk.png')
        time.sleep(1)

    def jd_hk(self):
        hk = self.driver.find_element_by_xpath('//div[@class="JDJRV-smallimg"]')
        action = ActionChains(self.driver)
        action.click_and_hold(hk).move_by_offset(100, 0).perform()
        action.release(hk).perform()

jd = JD_login()
jd.get_images()
jd.jd_hk()

