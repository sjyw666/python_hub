#研发者：时间遗忘
#开发时间：2023/9/12 23:25
import time
import requests

specified_webpage = "http://192.168.40.2/a79.htm?wlanuserip=10.5.131.225&wlanacname="  # 指定的联网网页
specified_account = "2022133256"  # 指定的账号
specified_password = "200418"  # 指定的密码
specified_carrier = "中国电信"  # 指定的运营商

def is_network_cable_connected():
    # 检测是否连接了网线，根据实际情况编写相应的代码
    # 这里假设通过检测网络接口来判断是否连接网线
    # 可根据不同系统和网络配置自行调整
    # Windows系统示例：
    import socket
    try:
        socket.create_connection(("www.example.com", 80))
        return True
    except OSError:
        return False

def is_campus_network():
    # 检测是否为校园网，根据实际情况编写相应的代码
    # 这里使用了简单的方式，根据指定的网址是否可访问来判断是否为校园网
    try:
        response = requests.get(specified_webpage)
        if response.status_code == 200:
            return True
        else:
            print("Campus network check failed with status code:", response.status_code)
            return False
    except Exception as e:
        print("Campus network check failed with error:", e)
        return False

def is_campus_broadband_page():
    # 检测是否为校园网宽带连接程序，根据实际情况编写相应的代码
    # 这里使用了简单的方式，根据指定的关键词判断是否为校园网宽带连接页面
    try:
        response = requests.get(specified_webpage)
        if "校园网宽带连接页面" in response.text:
            return True
        else:
            print("Not on campus broadband page.")
            return False
    except Exception as e:
        print("Campus broadband page check failed with error:", e)
        return False

def enter_credentials(account, password):
    # 输入账号和密码，根据实际情况编写相应的代码
    # 这里只是简单地打印了账号和密码
    print("Entering credentials...")
    print("Account: " + account)
    print("Password: " + password)

def select_carrier(carrier):
    # 选择运营商，根据实际情况编写相应的代码
    # 这里只是简单地打印了所选择的运营商
    print("Selecting carrier: " + carrier)

def get_current_time():
    return time.time()

def display_in_terminal(message):
    print(message)

def exit_program():
    print("Exiting program...")
    exit()

start_time = get_current_time()  # 记录程序开始时间

if not is_network_cable_connected():
    print("Network cable not connected.")
    exit_program()

if not is_campus_network():
    print("Not connected to campus network.")
    exit_program()

if not is_campus_broadband_page():
    exit_program()

enter_credentials(specified_account, specified_password)
select_carrier(specified_carrier)

end_time = get_current_time()  # 记录程序结束时间
execution_time = end_time - start_time  # 计算程序运行时间

display_in_terminal("Program execution time: " + str(execution_time))

if not is_network_cable_connected():
    print("Network cable disconnected after program execution.")
    exit_program()
