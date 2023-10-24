#研发者：时间遗忘
#开发时间：2023/5/25 14:57
'''
split()
    从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
    以通过参数sep指定劈分字符串是劈分符
    通过参数maxsplit指定劈分字符串时的最大劈分次数,在经过最大次数劈分之后，剩余的子串会单独做为一部分
rsplit()
    从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
    以通过参数sep指定劈分字符串是劈分符
    通过参数maxsplit指定劈分字符串时的最大劈分次数,在经过最大次数劈分之后，剩余的子串会单独做为一部分
'''
s='hello world Python'
lst=s.split()
print(lst)

s1='hello|world|Python'
print(s1.split())
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))#限定了只能分一次

print("-"*70)
'''rsplit()从右侧开始劈分'''
print(s.rsplit())       #没设定，默认是空格
print(s1.rsplit('|'))    #进行了设定，设定为|
print(s1.rsplit(sep='|',maxsplit=1))   #不指定分割次数，左右分割效果相同