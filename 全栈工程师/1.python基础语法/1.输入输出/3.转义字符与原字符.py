#转义字符
print('hollo\nworld')#\   +转义字符的首字母     n--》newline的首字母表示换行
print('hollo\tworld')#\t表示出现单元空格并对单元格的补充    一个单元格是四个字母     t--》tab
print('holloooo\tworld')#\t前面的制表位占满了就重新开启一个指表位
print('hollo\rworld')#\r表示回车  后面的覆盖掉前面的内容      r--》return
print('hollo\bworld')#\b是退一个格   将前面的一个字母给覆盖掉     b--》backspace




#输入网址时的两个反斜杠，第一个会理解为转移字符的反斜杠，第二个反斜杠会理解为不是转义字符首字母符号，从而只表现出一个反斜杠
print('http:\\www.baidu.com')
#需要多补两个反斜杠进行补充，才能体现出完整的网址
print('http:\\\\www.baidu.com')
#想要输出单引号也可以在前面加入反斜杠，这样确保单引号不是字符串的边界，而是我字符串中应该出现的内容，双引号同理
print('老师说：\'大家好\'')



#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r,或R
print(r'hollo\nworld')
#注意事项，最后一个字符不能是反斜杠，否则无法运行，可使用双反斜杠来抵消
print(r'hollo\nworld\\')