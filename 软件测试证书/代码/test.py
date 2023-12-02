from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

inputtag = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'kw'))
)
inputtag.send_keys('selenium')

btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'su'))
)
btn.click()

driver.quit()
