# pip install seleniuim
# pip webdriver_manager

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(options=options)

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://www.naver.com")
time.sleep(2)

# 뉴스
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(3)
newstitle = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text
print(newstitle)

driver.find_element(By.XPATH, "/html/body/section/header/div[1]/div/div/div[1]/span/a").click()
time.sleep(1)

# 부동산
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[4]/a").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/div").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[2]/div/div[1]/div/div/a/span[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[2]/div/div[1]/div/div/div/div[2]/ul/li[18]/label").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[2]/div/div[1]/div/div/div/div[2]/ul/li[4]/label").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[2]/div/div[1]/div/div/div/div[4]/a").click()
time.sleep(5)

# 부동산 2
driver.get("https://m.land.naver.com/search")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("우성꿈동산")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]").click()
time.sleep(1)
rentprice = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text
print(rentprice)

# 증권
driver.get("https://www.naver.com")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[3]/a").click()
time.sleep(1)
# 1
subject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th").text
print(subject)
subject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th").text
print(subject)
subject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th").text
print(subject)
subject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[4]/th").text
print(subject)

# 2
lst = []
for i in range(10): 
    subject = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th").text
    lst.append(subject)

print(lst)


topsubject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table").text
print(topsubject)