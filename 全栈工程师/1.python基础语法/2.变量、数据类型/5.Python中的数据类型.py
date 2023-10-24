#一旦变量的值发生改变，内存地址就变了，这种类型就称为  不可变数据类型
#或内存地址发生改变了就叫  不可变数据类型
#现在所学的四种类型都为不可变类型
a=10
print(a,id(a))#id输出内存地址


a=20
print(a,id(a))#将a的值更改，那么内存地址也发生更改



#整数类型--》int(integer)--》98
#可以表示正数，负数，零
n1=98
n2=-76
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
#正数可以表示为二进制，十进制（默认），八进制，十六进制
print('十进制',118)
print('二进制',0b10101111)#二进制以0b开头，转换为十进制。不加0b会默认输出十进制，加上0b用于区分
print('八进制',0o176)#八进制以0o开头,没有8和9，只有01234567
print('十六进制',0x1EAF)#十六进制以0x开头，十六进制是以123456789ABCDEF来表示的
print('十六进制X大小写不区分',0X1EAF)


print("--------------------")


n1=98
n2=-76
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
print("十进制",89)
print("二进制",0b10101010100101)#b:binary system
print("八进制",0o173)#o:octal number system
print("十六进制",0x153EABF)#x:hexadecimal



#浮点类型--》float--》3.1415926
a=3.14159
print(a,type(a))
n1=1.1
n2=2.2
n3=2.1
print(n1+n2)#计算机采用的是二进制储存，计算浮点数的时候会产生误差，有一定的不准确性（二进制的底层问题），这时候需要较型(导入模块dedcimal)
print(n1+n3)
from decimal import Decimal#大小写必须区分，因为前面那个是decimal函数的Decimal工具，必须区分大小写
print(Decimal('1.1')+Decimal('2.2'))

from decimal import Decimal
print('小数相加',Decimal('1.1')+Decimal('2.2'))#Decimal工具后面带小括号

from decimal import Decimal
print("小数相加",Decimal('31.1')+Decimal('43.2'))#不加单引号也会引发二进制的底层问题，小数点后会出现多位数




print("---------------------")




#布尔类型--》bool（boolean）--》True(是），False（否）
f1=True
f2=False#必须都是大写，小写不行
print(f1,type(f1))
print(f2,type(f2))
print(f1+f2)#布尔值可以直接转成整数运算
print(f1+1)#True是1
print(f2+2)#False是0

print('第二次输入')
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
print(f1+f2)
print(f1+1)
print(f2+2)



#字符串类型--》str--》‘name’（使用单引号，双引号，三引号括起来的内容）
str1='人生苦短'
str2="人生苦短"#单引号和双引号只能在单行实现
str3='''人生苦短，
及时行乐'''
str4="""人生苦短，
及时行乐"""#三引号可以在多行实现
##和三引号都可用于多行注释

print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))