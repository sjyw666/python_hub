# 研发者：时间遗忘
# 开发时间：2023/10/21 16:19
# 特点说明：无
'''
try……except……else结构
    如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
'''



try:
    print(10/0)
except  BaseException  as e:    # 起个别名
    print(e)
else:
    print("except没抛出异常")

'''
try……except……else……finally结构
    finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源
'''

try:
    print(10/0)
except BaseException as e:
    print("第一条路")
else:
    print("第二条路")
finally:
    print("最后都要回到这里")
