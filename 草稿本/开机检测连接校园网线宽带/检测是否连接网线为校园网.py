#研发者：时间遗忘
#开发时间：2023/9/13 15:02
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

if is_network_cable_connected():
    if is_campus_network():
        print("已连接网线并且连接到校园网络")
    else:
        print("已连接网线但未连接到校园网络")
else:
    print("未连接网线")
