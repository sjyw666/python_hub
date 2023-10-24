#研发者：时间遗忘
#开发时间：2023/6/14 20:50
'''为什么需要字符串的编码转化：
字符串在网络中进行传输的话，
A计算机                                                  B计算机
str在内存中以Unicode表示   --》编码 --》byte字节传输--》解码--》 显示

编码：将字符串转换为二进制数据（byte）
解码：将bytes类型的数据转换成字符串类型'''

s='你食不食荔枝'

#编码
print(s.encode(encoding='GBK'))     #在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))   #在UTF-8中，一个中文占3个字节


#解码
#byte代表就是一个二进制数据（字节类型的数据），爬虫的时候可能会用到
byte=s.encode(encoding='GBK')       #编码
print(byte.decode(encoding='GBK'))  #解码，括号里面是解码格式
#print(byte.decode(encoding='UTF-8'))  #解码格式与编码格式不相同，程序报错


byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))