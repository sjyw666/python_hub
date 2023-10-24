# coding:utf-8
# author:杨淑娟
s='杨淑娟'
s_code=s.encode(encoding='utf-8') # encode是方法,encoding 是方法的参数，指定编码的编码格式
print(s_code) # utf-8每个中文占3个字节
s_code1=s.encode(encoding='gbk') # gbk一个中文占2个字节
print(s_code1,type(s_code1)) # 在输出结果之前都有一个b

# encode 编码  str-->bytes的过程
# decode 解码  bytes-->str的过程
print(bytes.decode(s_code1,encoding='gbk'))
print(bytes.decode(s_code,encoding='utf-8'))