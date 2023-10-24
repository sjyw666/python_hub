# coding:utf-8
# author:杨淑娟
# 要求统计 云长  的出现次数

word='当下两军相对，玄德出马，左有云长，右有翼德，扬鞭大骂：“反国逆贼，何不早降！”程远志大怒，遣副将邓茂出战。张飞挺丈八蛇矛直出，手起处，刺中邓茂心窝，翻身落马。程远志见折了邓茂，拍马舞刀，直取张飞。云长舞动大刀，纵马飞迎。程远志见了，早吃一惊，措手不及，被云长刀起处，挥为两段。'
name='云长翼德'
count=word.count(name[0:2])
order='' # 用于统计出现的次数
size=-2
for i in range(count):
    size=word.find(name[:2],size+len(name[0:2]))
    order+=str(size)+' '
print(name[:2],'出现次数:',count)
print(name[:2],'出现位置:',order)

