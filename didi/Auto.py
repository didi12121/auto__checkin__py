from selenium.webdriver import ChromeOptions
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_cookie(profile__path):
    opt = ChromeOptions()
    opt.add_argument('--no-sandbox')
    opt.add_argument("--headless")
    opt.add_argument(r'user-data-dir={}'.format(profile__path))
    browser = webdriver.Chrome(options=opt)
    loginurl = "https://weibo.com/newlogin";
    browser.get(loginurl)
    time.sleep(5)
    print(browser.current_url)
    element = browser.find_element(By.LINK_TEXT, '热门微博')
    element.click()
    time.sleep(1)
    element.send_keys(Keys.SPACE)
    time.sleep(2)
    browser.find_element(By.LINK_TEXT, '登录').click()
    time.sleep(2)
    imgelement = browser.find_element(By.CSS_SELECTOR,
                                      '#app > div:nth-child(4) > div.woo-modal-main > div > div.woo-box-flex.woo-box-alignCenter.woo-box-justifyCenter.LoginPop_main_SAOC0 > div > div > div.woo-box-flex.woo-box-alignCenter.woo-box-justifyBetween.LoginPop_crbox_237wO > div.LoginPop_mabox_3Lyr6 > img')
    print('请打开链接扫描二维码')
    print(imgelement.get_attribute("src"))
    while browser.current_url.__contains__('newlogin'):
        time.sleep(3)
        print('等待扫码')
    print(browser.current_url)
    print('扫码成功')
    browser.close()
