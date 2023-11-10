#研发者：时间遗忘
#开发时间：2023/7/19 13:50
# encoding: utf-8
word = '当下两军相对，玄德出马，左有云长，右有翼德，扬鞭大骂：“反国逆贼，何不早降！”程远志大怒，遣副将邓茂出战。张飞挺丈八蛇矛直出，手起处，刺中邓茂心窝，翻身落马。程远志见折了邓茂，拍马舞刀，直取张飞。云长舞动大刀，纵马飞迎。程远志见了，早吃一惊，措手不及，被云长刀起处，挥为两段。'
name = '云长翼德'

acount = 0
number = 0
for i in word:
    if word[number] == name[0] and word[number+1] == name[1]:
        acount += 1
    number += 1

start = 0
location_list = []
while True:
    location = word.find(name[0:2],start)
    if location != -1:
        location_list.append(location)
        start = location + 1
    else:
        break




print(f' {name[0:2]} 出现次数：{acount}')
print(f' {name[0:2]} 出现位置：{location_list}')

'''写法二'''
word = '当下两军相对，玄德出马，左有云长，右有翼德，扬鞭大骂：“反国逆贼，何不早降！”程远志大怒，遣副将邓茂出战。张飞挺丈八蛇矛直出，手起处，刺中邓茂心窝，翻身落马。程远志见折了邓茂，拍马舞刀，直取张飞。云长舞动大刀，纵马飞迎。程远志见了，早吃一惊，措手不及，被云长刀起处，挥为两段。'
name = '云长翼德'
find_name = name[0:2]

acount = 0
location_list = []
start = 0

while True:
    location = word.find(find_name, start)
    if location != -1:
        acount += 1
        location_list.append(location)
        start = location + 1
    else:
        break

print(f' {find_name} 出现次数：{acount}')
print(f' {find_name} 出现位置：{location_list}')
