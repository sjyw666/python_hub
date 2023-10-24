#研发者：时间遗忘
#开发时间：2023/9/13 14:56
import socket

def is_network_cable_connected():
    try:
        # 尝试创建一个socket连接到一个已知的IP地址和端口，如果成功，说明连接了网线
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return "已连接网线"
    except OSError:
        return "未连接网线"

# 调用函数进行检测
network_status = is_network_cable_connected()
print(network_status)
