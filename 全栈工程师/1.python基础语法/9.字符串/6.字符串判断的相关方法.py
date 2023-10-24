#研发者：时间遗忘
#开发时间：2023/5/26 11:30
'''
isidentifier()
    判断指定的字符串是不是合法的标识符(字母，数字，下划线)
isspace()
    判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）
isalpha()
    判断指定的字符串是否全部由字母组成
isdecimal()
    判断指定字符串是否全部由十进制的数字组成
isnumeric()
    判断指定的字符串是否全部由数字组成
isalnum()
    判断指定字符串是否全部由字母和数字组成
'''
#合法的标识符
s='hello,python'
print('1.',s.isidentifier())            #False  逗号不是
print('2.','hello'.isidentifier())      #True
print('3.','张三_'.isidentifier())       #True
print('4.','张三_123'.isidentifier())    #True


#空白字符
print('5.','\t'.isspace())      #True

#字母
print('6','abc'.isalpha())      #True
print('7','张三'.isalpha())      #True
print('8','张三1'.isalpha())      #False   因为1不是字母

#十进制
print('9','123'.isdecimal())      #True
print('10','123四'.isdecimal())      #False
print('11','ⅡⅡⅡ'.isdecimal())      #False   罗马数字二不是十进制数

#数字
print('12','123'.isnumeric())      #True
print('13','123四'.isnumeric())      #True   文字的数字也是数字
print('14','ⅡⅡⅡ'.isnumeric())      #True   罗马数字是数字

#字母和数字
print('15','abc'.isalnum())      #True
print('16','张三123'.isalnum())      #True
print('17','abc！'.isalnum())      #False    ！不是字母也不是数字