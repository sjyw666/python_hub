# coding:utf-8
# author:杨淑娟
name='Python娟子姐'
age=18
# 第一种方式
print('大家好，我叫%s,今年%d岁' % (name,age)) # C语言中常见 ,一般不使用
# 第二种是字符串对象的format方法
print('大家好，我叫{0},今年{1}岁'.format(name,age))
# 第三方法是f-string
print(f'大家好，我叫{name},今年{age}岁')
# 第四种，Python内存的format方法
#字符串对象的format方法，更容易控制数据
# 键盘上 6上面的
# 下面这段代码中的 :  ,必须要有，是提示符
print('{:*^25}'.format('hello')) # 显示宽度是25个字符的宽度，要求居中对齐，左右使用*填充
