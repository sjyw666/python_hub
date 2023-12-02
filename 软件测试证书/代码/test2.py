from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 等待页面加载完成，增加了更长的等待时间
time.sleep(5)  # 在这里等待了 5 秒，你可以根据需要调整时间

# 找到搜索框和搜索按钮并进行操作
input_tag = driver.find_element(By.ID, 'kw')
input_tag.send_keys('selenium')

btn = driver.find_element(By.ID, 'su')
btn.click()

# 关闭浏览器
driver.quit()

