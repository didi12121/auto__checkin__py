from tkinter.ttk import Label

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageTk
from tkinter import font as tf
from tkinter import Tk


def get_cookie():
    browser = webdriver.Chrome()
    loginurl = "https://weibo.com/newlogin";
    browser.get(loginurl)
    time.sleep(10)
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
    code_png = "qrCode.png"
    imgelement.screenshot(code_png)
    frame = create_image_frame(code_png)
    flag = True
    print('-----等待扫码----')
    while flag:
        time.sleep(3)
        print('-----等待扫码----')
        print('newlogin' in browser.current_url)
        flag = 'newlogin' in browser.current_url
    print(browser.get_cookies())
    frame.quit()
    browser.close()


def create_image_frame(url) -> Tk:
    root = Tk()
    root.title('扫描二维码')
    image = Image.open(url)
    source_img = ImageTk.PhotoImage(image)
    label = Label(root, text='test', image=source_img)
    label.pack()
    root.mainloop()
    return root
