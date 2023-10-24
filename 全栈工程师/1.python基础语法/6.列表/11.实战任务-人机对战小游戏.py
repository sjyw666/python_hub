#研发者：时间遗忘
#开发时间：2022/10/7 19:43

#名字输入
print('-'*5,'人机对战小游戏','-'*5)
print('石头\t\t剪刀\t\t\t布')
game_player_name=input('请输入玩家姓名：')
computer_name_choice=eval(input('请选择电脑玩家：1.貂蝉  2.曹操 3.诸葛亮'))
if computer_name_choice==1:
    computer_name='貂蝉'
elif computer_name_choice==2:
    computer_name='曹操'
elif computer_name_choice==3:
    computer_name='诸葛亮'
else:
    computer_name='匿名'
print(game_player_name,'VS',computer_name)


count=0
game_player_score=0
computer_score=0
while True:
    count+=1
    #出拳
    game_player_choice=eval(input('请选择出：1.石头 2.剪刀 3.布'))
    if game_player_choice==1:
        player='石头'
    elif game_player_choice==2:
        player='剪刀'
    elif game_player_choice==3:
        player='布'
    else:
        player='石头'
        print('选择错误，已默认选择石头')

    import random
    computer_choice=random.randint(1,3)
    if computer_choice==1:
        computer='石头'
    elif computer_choice==2:
        computer='剪刀'
    elif computer_choice==3:
        computer='布'

    #判断输赢
    if game_player_choice==computer_choice:
        result='双方平手'
    elif (game_player_choice==1 and computer_choice==2) or (game_player_choice==2 and computer_choice==3) or (game_player_choice==3 and computer_choice==1):
        result='你赢'
        game_player_score+=1
    else:
        result='电脑赢'
        computer_score+=1

    #打印结果
    print(game_player_name,'出',player)
    print(computer_name,'出',computer)
    print(result)

    #使用到了无限循环，怎么退出？
    answer=(input('是否再来一局？y/n'))#使用eval的话就会把n当成变量了，而这个变量没定义，就会报错
    if answer=='n':
        break

#大总结
print('-'*5,game_player_name,'VS',computer_name,'-'*5)
print(f'一共对战{count}局')
print(f'{game_player_name}:{game_player_score}分')
print(f'{computer_name}:{computer_score}分')
if game_player_score==computer_score:
    print('平分秋色')
elif game_player_score>computer_score:
    print('完胜')
else:
    print('惜败，惜败')


print("---------------复习-------------")
import random
cisu=0
while True:
    print("可选择对手：1、欧斌  2、老肖  3、老潘")
    ds=eval(input('请选择：'))
    if type(ds)==int:
        if ds==1:
            ds_name='欧斌'
        elif ds==2:
            ds_name='老肖'
        elif ds==3:
            ds_name='老潘'
        else:
            print("别tm乱输，敲代码很累的，继续！")
            ds_name='欧斌'

    else:
        print("别tm乱输，敲代码很累的，继续！")
        ds_name = '欧斌'

    print(ds_name,"VS 你")

    print("请出拳：1、石头 2、剪刀 3、布")
    nichuquan=eval(input('出：'))
    if nichuquan==1:
        niquan='石头'
    elif nichuquan==2:
        niquan='剪刀'
    elif nichuquan==3:
        niquan='布'
    else:
        print("出拳有误，默认出石头")
        niquan='石头'


    randomchuquan=random.randint(1,3)#包含1 也包含3
    if randomchuquan==1:
        diannaochuquan='石头'
    elif randomchuquan==2:
        diannaochuquan='剪刀'
    elif randomchuquan==3:
        diannaochuquan='布'

    print(niquan,"VS",diannaochuquan)
    if nichuquan==randomchuquan:
        print("平局")
    #玩家赢的情况
    elif nichuquan==1 and randomchuquan==2:
        print("你赢")
    elif nichuquan==2 and randomchuquan==3:
        print("你赢")
    elif nichuquan==3 and randomchuquan==1:
        print("你赢")
    else:
        print("输了")

    zailai=(input("是否再来一局：y/n?"))
    if zailai=='n':
        break