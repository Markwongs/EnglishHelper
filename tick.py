# coding=UTF-8

from selenium import webdriver
import time
import datetime

# opt = Options()
# opt.add_experimental_option('excludeSwitches', ['enable-automation'])
# opt.add_argument('--headless')

today = str(datetime.date.today())
url = r"http://dailyreport.hhu.edu.cn/pdc/form/list"
user_file = r"C:\Users\xwsev\Desktop\user.txt"
vertification_file = r'C:\Users\xwsev\Desktop\vertify.txt'
with open(user_file, 'r') as f:
    users = f.readlines()


def tick(pair):

    # driver = webdriver.Chrome(executable_path='', options=opt)
    driver = webdriver.Edge(executable_path=r'C:\Users\xwsev\scoop\apps\edgedriver\93.0.946.0\msedgedriver.exe', options=opt)
    driver.get(url)

    # input username and password
    driver.find_element_by_id("username").send_keys(pair[0])
    time.sleep(0.1)
    driver.find_element_by_id("password").send_keys(pair[1])

    submit_button = driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button')
    submit_button.click()

    driver.implicitly_wait(40)
    enter_in = driver.find_element_by_partial_link_text('进入')
    enter_in.click()

    driver.implicitly_wait(30)
    driver.find_element_by_id('saveBtn').click()

    driver.implicitly_wait(40)
    h3 = driver.find_element_by_css_selector('#successSubmit > div.panel-heading > h3')
    if h3.text == "提交成功！":
        ticked = today
    else:
        print('failed')
        ticked = 'failed'

    time.sleep(1)
    driver.quit()
    return ticked


for user in users:
    index = user.index(':')
    username = user[:index]
    password = user[index+1:]
    suffix = "NoneSuffix"

    try:
        with open(vertification_file, 'r+') as f2:
            ver_text = f2.read()
            if username+today not in ver_text:
                suffix = tick([username, password])
                print('-'*50)

                f2.write(username + suffix)
            else:
                print(username, "had ticked")
    except:
        print(username+" Failed")
        time.sleep(120)
    finally:
        print(username, suffix)
        time.sleep(5)


