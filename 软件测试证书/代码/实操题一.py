# 研发者：时间遗忘
# 开发时间：2023/11/24 20:11
# 特点说明：
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By as BY
driver = webdriver.Chrome()
driver.get('http://116.204.37.186:30018')
username = driver.find_element_by_xpath('//input[@id =  "username"]')
username.send_keys('hrteachar')
password = driver.find_element(BY.ID, 'password')
password.send_keys('123456')
loginBtn = driver.find_element(BY.CSS_SELECTOR, 'loginBtn')
loginBtn.click()
