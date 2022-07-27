from selenium import webdriver
import json
import time

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

def add_cookies(browser, cookie_file):
    with open(cookie_file, 'r') as file:
        cookies_list = json.load(file)
        for cookie_dict in cookies_list:
            browser.add_cookie(cookie_dict)

def login():
    driver = create_chrome_driver()
    driver.implicitly_wait(50)
    driver.maximize_window()

    # driver.get('https://passport.jd.com')
    # add_cookies(driver, 'jd_login.json')
    # driver.get('https://order.jd.com/center/list.action')

    driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F')
    driver.find_element_by_xpath('//*[@class="login-tab login-tab-r"]/a').click()
    driver.find_element_by_name('loginname').send_keys('13437061763')
    driver.find_element_by_name('nloginpwd').send_keys('xwk970728')
    driver.find_element_by_id('loginsubmit').click()

    time.sleep(15)
    # 获取cookie数据写入文件
    with open('jd_login.json', 'w') as file:
        json.dump(driver.get_cookies(), file)

# login()
