from selenium import webdriver
from selenium.webdriver.common.by import By
from func_timeout import func_set_timeout
from threading import Thread
from time import sleep


def process(start, end):

    def login():
        driver.get(url)
        driver.find_element(By.XPATH, '//*[@id="o"]').send_keys('中央财经大学')
        driver.find_element(By.XPATH, '//*[@id="form1"]/div[4]/div[1]/div[2]/div[2]').click()
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('2020311334')
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('20021020Liu')
        driver.find_element(By.XPATH, '//*[@id="casLoginForm"]/p[2]/button').click()

    @func_set_timeout(20)
    def crawler():
        page = 'https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CAPJ&dbname=CAPJDAY&filename=' + id +'&uniplatform=NZKPT&v=K5bYKqTXuu6D-va82qWqKFN9f91gBIt-mQ-X3EKwDnquf89kKyZIknprkZO-J_CH'
        driver.get(page)
        title = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div[3]/div/h1').text
        f_title_id = open(title_id_path, "a")
        f_title_id.write(title+'\t'+id+'\n')
        f_title_id.close()
        driver.find_element(By.XPATH, '//*[@id="pdfDown"]').click()

    driver = webdriver.Chrome(driverpath)
    login()
    t = 0
    for i in range(start, end):
        print(i)
        id = id_list[i]
        try:
            crawler()
            t = t+1
            if t >= 30:
                driver = webdriver.Chrome(driverpath)
                login()
                t = 0
        except:
            driver = webdriver.Chrome(driverpath)
            login()


driverpath = "D:\\chromedriver.exe"
title_id_path = "C:\\Users\\86191\\Desktop\\cnki_title_id.txt"
url = 'https://fsso.cnki.net/'
id_path = "C:\\Users\\86191\\Desktop\\cnki_left.txt"
f = open(id_path, "r")
id_list = [i.replace('\n', '') for i in f.readlines()]
f.close()
l = len(id_list)

thead_list = []
for i in range(16):
    t = Thread(target=process, args=(int(i/16), int((l + 1)/16)))
    t.start()
    thead_list.append(t)

for t in thead_list:
    t.join()
