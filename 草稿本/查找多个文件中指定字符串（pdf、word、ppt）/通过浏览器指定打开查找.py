#研发者：时间遗忘
#开发时间：2023/9/3 22:37
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time

def search_pdf_with_edge_browser(file_path, target_string):
    # 设置 Edge WebDriver 的路径
    edge_driver_path = "E:\edgedriver\msedgedriver.exe"  # 替换为您的 Edge WebDriver 的路径

    # 创建 Edge WebDriver 的服务对象
    edge_service = Service(edge_driver_path)

    # 创建 Edge WebDriver
    driver = webdriver.Edge(service=edge_service)

    try:
        # 遍历指定路径下的所有文件和子文件夹
        for root, dirs, files in os.walk(file_path):
            for file in files:
                # 检查文件扩展名是否为PDF
                if file.endswith(".pdf"):
                    pdf_path = os.path.join(root, file)

                    # 打开 PDF 文件
                    driver.get(pdf_path)

                    # 等待页面加载完成
                    time.sleep(2)

                    # 在页面中执行搜索操作
                    search_box = driver.find_element("tag name", "input")
                    search_box.send_keys(target_string)
                    search_box.send_keys(Keys.RETURN)

                    # 等待搜索结果加载完成
                    time.sleep(2)

                    # 检查是否存在搜索结果
                    no_results = driver.find_elements("css selector", ".no-results")
                    if no_results:
                        # 关闭当前页面
                        driver.close()
                    else:
                        # 等待用户手动关闭浏览器
                        input("搜索结果已展示，请手动关闭浏览器后按 Enter 键继续...")

    finally:
        # 关闭浏览器驱动
        driver.quit()

if __name__ == "__main__":
    file_path = input("指定要遍历的文件夹路径:")  # 指定要遍历的文件夹路径
    target_string = input("指定要搜索的目标字符串:")  # 指定要搜索的目标字符串

    search_pdf_with_edge_browser(file_path, target_string)
