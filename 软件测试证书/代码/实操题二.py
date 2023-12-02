# 研发者：时间遗忘
# 开发时间：2023/11/24 21:37
# 特点说明：
'''

'''
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://116.204.37.186:30018')

time.sleep(30)
driver.find_element(By.ID, 'username').send_keys('hrteachar')

driver.find_element('//input[@id="password"]').send_keys('123456')

driver.find_element(By.CLASS_NAME, 'loginBtn').click()

driver.find_element(By.LINK_TEXT,'个人证书').click()

# 找到下拉选择框元素
dictCerType_element = driver.find_element(By.NAME,'dictCerType')

# 用 Select 类进行实例化
dictCerType = Select(dictCerType_element)

dictCerType.deselect_by_visible_text('学位证')