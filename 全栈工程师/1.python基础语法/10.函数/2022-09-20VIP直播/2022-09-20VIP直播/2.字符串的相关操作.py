# coding:utf-8
# author:杨淑娟
print('-'*70) # 这个是就是复制符 *
for i in range(70):
    print('-',end='')
print()
#判断符 in
city='北京'
if city in '北京 - 长春':
    print('在')
else:
    print('不在')
# 函数和方法的区别吗？ 字符串处理函数， 字符串处理方法

# 直接使用的叫函数， 使用字符串对象打点调用的叫方法
print(len('helloworld')) # 计算出字符串的长度

print('helloworld'.upper()) # 字符串对象打点调用的叫方法
# 字符串处理函数，有的不仅字符串能使用，其它类型的对象也能使用，比如说len
print(len([10,30,40])) # 计划列表的长度
# 字符串处理方法，只能字符串对象使用
# 字符串的劈分
s='杨-淑-娟'
lst=s.split('-') #'-'叫劈分 符 ,可以默认
print(lst)
s='杨- 淑-娟'
lst2=s.split() # 没有写劈分符，不是没有，是按 空格进行劈分
print(lst2)
print('helloworld'.count('o')) # o出现了几次？
print('helloworld'.replace('l','哎欧'))
print('helloworld'.replace('l','哎欧',1))  #指定替换次数 1次数
print('   hello   world   '.strip()) # 没有指定参数的时候，去掉字符串左右的空格
print('helloworldeh'.strip('he')) # 字符串后面的eh会不会去掉？会，去掉提定的字符，与顺序无关
lst=['hello','world','python']
s='@'.join(lst)
print(s)
