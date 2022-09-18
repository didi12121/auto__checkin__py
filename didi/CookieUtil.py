import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium import webdriver


def __get_cookie__by__pro__file(user__data__dir):
    opt = ChromeOptions()
    opt.add_argument("--headless")
    opt.add_argument(user__data__dir)
    browser = webdriver.Chrome(options=opt)
    print("=====打开浏览器====")
    browser.get("https://weibo.com/")
    print(browser.current_url)
    time.sleep(2)
    while not browser.current_url.__eq__("https://weibo.com/"):
        print("等待跳转中")
    data = browser.get_cookies()
    print("=======获取cokie======")
    return data
