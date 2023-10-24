#研发者：时间遗忘
#开发时间：2023/9/13 15:10
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 配置Microsoft Edge浏览器驱动的路径，替换为实际路径
edge_driver_path = '/path/to/msedgedriver'

# 创建Microsoft Edge浏览器实例
driver = webdriver.Edge(executable_path=edge_driver_path)

# 打开校园网登录页面
driver.get("校园网登录页面的URL")

# 自动填写账号和密码
account, password = enter_credentials()
account_field = driver.find_element_by_id("2022133256")  # 替换为实际的字段ID
password_field = driver.find_element_by_id("200418")  # 替换为实际的字段ID
account_field.send_keys(account)
password_field.send_keys(password)

# 自动选择运营商（如果有选择项的话）
carrier = select_carrier()
if carrier:
    carrier_dropdown = driver.find_element_by_id("运营商下拉菜单的ID")  # 替换为实际的下拉菜单ID
    carrier_dropdown.click()
    carrier_option = driver.find_element_by_xpath("//option[text()='{}']".format(carrier))
    carrier_option.click()

# 提交表单以连接校园网
login_button = driver.find_element_by_id("登录按钮的ID")  # 替换为实际的按钮ID
login_button.click()

# 等待一段时间以确保连接成功，您可以根据实际情况调整等待时间
time.sleep(10)

# 关闭浏览器
driver.quit()
