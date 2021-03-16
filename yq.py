# coding=UTF-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib
from email.mime.text import MIMEText

from selenium.webdriver.chrome.options import Options


def fill_in(xh, mm):
    options = Options()
    options.binary_location = '/usr/bin/google-chrome'
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='/root/driver/chromedriver', chrome_options=options)

    driver.get("http://form.hhu.edu.cn/pdc/formDesignApi/S/gUTwwojq")
    assert "河海大学统一身份认证平台" in driver.title

    def Login():
        # input Username and Password
        eleUserMessage = driver.find_element_by_id("IDToken1")
        eleUserMessage.clear()
        eleUserMessage.send_keys(xh)

        elepassMessage = driver.find_element_by_id("IDToken2")
        # print(elepassMessage)
        elepassMessage.clear()
        elepassMessage.send_keys(mm)
        # driver.find_element_by_xpath("//td[@onclick='defaultSubmit()']").click()
        driver.find_element_by_xpath("//img[@onclick=\"defaultSubmit()\"]").click()
        # print('Login_yes')

    def Select_benke(xh):
        if len(xh) == 10:
            continue_link = driver.find_element_by_partial_link_text('本科生')
        else:
            continue_link = driver.find_element_by_partial_link_text('研究生')
        continue_link.click()

    def Submit():

        sumbit_fin = driver.find_element_by_id('saveBtn')
        sumbit_fin.click()

    def is_succeed():

        h3 = driver.find_element_by_class_name('panel-title')
        # print(h3.text)
        if h3.text == "提交成功！":
            return True
        else:
            return False

    Login()
    time.sleep(2)
    Select_benke(xh)
    time.sleep(2)
    Submit()
    time.sleep(2)
    a = is_succeed()
    time.sleep(2)
    driver.close()
    return a


def main():
    # is_ok = False
    try:
        stus = {'1702040307': '090024', '1702040329': '228574', '1702040102': '173826', '1702040305': 'miniso5039', '201310020001': '085512', '191310060006': '051329', '201310010032': '202020', '181310060017': '093715', '201610010007':'095434', '20021006003':'080041', }
        for xh, mm in stus.items():
            if fill_in(xh, mm) == True:
                is_ok = True
            time.sleep(10)
            print(xh, mm)
    except:
        is_ok = False
    finally:
        print("after first trying:is_ok == {is_ok}", is_ok)


if __name__ == '__main__':
    main()
