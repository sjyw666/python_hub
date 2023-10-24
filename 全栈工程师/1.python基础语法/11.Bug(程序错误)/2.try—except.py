# 研发者：时间遗忘
# 开发时间：2023/10/21 16:02
# 特点说明：
'''
被动掉坑程序代码逻辑没有错，只是因为用户错误操作或者一些“例外情况"而导致的程序崩溃
解决方案：
Python提供了异常处理机制，可以在异常出现时即时捕获，然后内部“消化"，让程序继续运行
'''
'''
try:
    可能出现的错误的代码
except  异常类型(可选参数，由报错得来)：
    异常处理代码(报错后执行的代码)
'''

try:
    print(10/0)
except:
    print("程序出错")

'''
try:
    ……
except  Exception1:
    ……
except  Exception2:
    ……
except  BaseException:#所有情况
    ……
'''

try:
    print(10/0)
except Exception:
    print("第一种错误")
except BaseException:   # 所有报错情况
    print("所有情况")