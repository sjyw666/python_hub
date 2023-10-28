# 研发者：时间遗忘
# 开发时间：2023/10/26 19:52
# 特点说明：无
import requests
from bs4 import BeautifulSoup

# 伪装成浏览器的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# 目标网页的URL
url = 'https://www.tipdm.org/u/cms/www/202206/27143450a8sn.pdf'  # 请替换成您想要爬取的网页URL

# 发送HTTP请求
response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有的链接
    links = soup.find_all('a')

    for link in links:
        # 检查链接是否以.pdf结尾
        if link['href'].endswith('.pdf'):
            pdf_url = link['href']
            # 构建完整的PDF链接
            if not pdf_url.startswith('http'):
                pdf_url = url + pdf_url

            # 发送请求下载PDF文件
            pdf_response = requests.get(pdf_url, headers=headers)

            # 检查响应状态码
            if pdf_response.status_code == 200:
                # 保存PDF文件
                with open(pdf_url.split('/')[-1], 'wb') as pdf_file:
                    pdf_file.write(pdf_response.content)
                    print(f"已下载PDF文件：{pdf_url.split('/')[-1]}")
            else:
                print(f"无法下载PDF文件：{pdf_url}")
else:
    print(f"无法访问网页：{url}")
