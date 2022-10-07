import time
from didi import RedisUtil
from selenium.webdriver import Chrome, ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By


def __get_cookie__by__pro__file(user__data__dir):
    opt = ChromeOptions()
    opt.add_argument('--no-sandbox')
    opt.add_argument("--headless")
    opt.add_argument(user__data__dir)
    browser = webdriver.Chrome(options=opt)
    print("=====打开浏览器====")
    browser.get("https://weibo.com/")
    print(browser.current_url)
    while not browser.current_url.__eq__("https://weibo.com/"):
        time.sleep(3)
        print("等待跳转中")
    data = browser.get_cookies()
    print("=======获取cokie======")
    uid = browser.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/a[5]').get_attribute('href').replace('https://weibo.com/u/', '')
    print("=======获取uid为 {}======".format(uid))
    RedisUtil.cache_cookie(uid, data)
    browser.close()
    return RedisUtil.get_cookie(uid)

