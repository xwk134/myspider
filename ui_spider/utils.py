from selenium import webdriver
import time
import requests
from lxml import etree
import os

def create_chrome_driver(*, headless=False):
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

driver = create_chrome_driver()
driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F')
driver.implicitly_wait(50)
driver.maximize_window()
driver.find_element_by_xpath('//*[@class="login-tab login-tab-r"]/a').click()
driver.find_element_by_name('loginname').send_keys('13437061763')
driver.find_element_by_name('nloginpwd').send_keys('xwk970728')
driver.find_element_by_id('loginsubmit').click()
time.sleep(2)
info = driver.page_source
print(info)
root_element = etree.HTML(info)
link = root_element.xpath('//div[@class="JDJRV-img-wrap"]/div/img/@src')[0]
print(link)
conet = requests.get(link)
dir_name = 'D:\\验证码\\'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
with open(dir_name + '京东滑块.png', mode='wb') as f:
    f.write(conet.content)
time.sleep(1)


