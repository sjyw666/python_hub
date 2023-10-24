# 研发者：时间遗忘
# 开发时间：2023/10/21 16:34
# 特点说明：无
import traceback
try:
    print("-"*70)   # 线在不同的位置说明是不同的进程
    print(10/0)
except:     # 不写也可以直接冒号
    traceback.print_exc()   # 用来打印错误信息，后面可放在日志文件

