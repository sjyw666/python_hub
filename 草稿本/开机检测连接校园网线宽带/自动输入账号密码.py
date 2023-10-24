#研发者：时间遗忘
#开发时间：2023/9/13 15:06
import socket
import requests

def is_network_cable_connected():
    try:
        # 尝试创建一个socket连接到一个已知的IP地址和端口，如果成功，说明连接了网线
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

def is_campus_network():
    try:
        response = requests.get("http://www.example.com")
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def enter_credentials():
    account = "2022133256"  # 替换为实际的账号
    password = "200418"  # 替换为实际的密码
    return account, password

def select_carrier():
    carrier = "中国电信"  # 替换为实际的运营商
    return carrier

if is_network_cable_connected():
    if is_campus_network():
        print("已连接网线并且连接到校园网络")
        account, password = enter_credentials()
        carrier = select_carrier()
        print("校园网账号:", account)
        print("校园网密码:", password)
        print("选择的运营商:", carrier)
    else:
        print("已连接网线但未连接到校园网络")
else:
    print("未连接网线")
