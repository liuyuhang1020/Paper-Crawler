from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from func_timeout import func_set_timeout
from threading import Thread
import random


def process(start, end):

    def login():
        driver.get(url)
        driver.find_element(By.XPATH, '//*[@id="searchVal"]').send_keys('中央财经大学')
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/input').click()
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('**********')
        driver.find_element(By.XPATH, '//*[@id = "password"]').send_keys('**********')
        driver.find_element(By.XPATH, '//*[@id="casLoginForm"]/p[2]/button').click()

    @func_set_timeout(180)
    def crawler():
        page = 'https://d.wanfangdata.com.cn/periodical/'+id
        driver.get(page)
        title = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[1]/div[1]/div[1]/span').text
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[1]/div[2]/div/a[1]').click()
        sleep(1)
        f_title_id = open(title_id_path, "a")
        f_title_id.write(title+','+id+'\n')
        f_title_id.close()
        handles = driver.window_handles
        driver.close()
        driver.switch_to.window(handles[1])

    options = webdriver.ChromeOptions()
    p = random.randint(0, len(ip_pool)-1)
    options.add_argument("--proxy-server=http://"+ip_pool[p])
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    login()
    t = 0
    for i in range(start, end):
        id = id_list[i]
        print(i)
        try:
            crawler()
            t = t+1
            if t >= 3:
                sleep(3)
                options = webdriver.ChromeOptions()
                p = random.randint(1, len(ip_pool)-1)
                options.add_argument("--proxy-server=http://"+ip_pool[p])
                driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
                login()
                t = 0
        except:
            options = webdriver.ChromeOptions()
            p = random.randint(1, len(ip_pool)-1)
            options.add_argument("--proxy-server=http://"+ip_pool[p])
            driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
            login()


driver_path = "D:\\chromedriver.exe"
id_path = "C:\\Users\\86191\\Desktop\\wf18年文件缺少2W.txt"
title_id_path = "C:\\Users\\86191\\Desktop\\wanfang_title_id.txt"
url = 'https://fsso.wanfangdata.com.cn/'
ip_path = "C:\\Users\\86191\\Desktop\\ip_pool.txt"
f_ip = open(ip_path, "r")
ip_pool = [i.replace('\n', '') for i in f_ip.readlines()]
f_ip.close()
f_id = open(id_path, "r")
id_list = [i.replace('\n', '') for i in f_id.readlines()]
f_id.close()
l = len(id_list)

thead_list = []
for i in range(16):
    t = Thread(target=process, args=(int(i/16), int((l + 1)/16)))
    t.start()
    thead_list.append(t)

for t in thead_list:
    t.join()
