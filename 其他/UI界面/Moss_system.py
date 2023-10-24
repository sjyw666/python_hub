'''界面创建'''
'''职能：覆写，启动，运行，计算'''


#导入库
import PySimpleGUI as sg

#定义输入
name=sg.Text('姓名')
input_name=sg.InputText('')
cipher=sg.Text('密码')
input_cipher=sg.InputText('')



#定义布局，确定行数
layout=[

            [sg.Text('欢迎登录智能量子计算机Moss系统')],#第一行
            [name,input_name],#一个文本，一个输入框，中间用逗号隔开
            [cipher,input_cipher],
            [sg.Button('确认'),sg.Button('取消')]#两个按键
                     ]

#创建窗口
window=sg.Window('Python GUI',layout)#括号里面一个是窗口的标签，一个是引入的布局

#事件循环
while True:
    event,values=window.read()#窗口的读取，有两个返回值（1，事件  2，值）

    if event==None:#窗口关闭事件
        break
    if event=='确认':#事件
        sg.Popup('执行了确认任务')#执行一个弹窗任务
    if event=='取消':#事件
        sg.Popup('执行了取消')



if type(name)==str:
    if name == "赵泰康":
        '''if type(cipher)==int  and cipher==050220:
            pass
        else:
            print("密码错误，您还有两次机会")'''
    else:
        print(f'用户{name}无管理员权限')
else:
    print("输入错误")









#关闭窗口
window.close()






















#爬取今年高考志愿学校资料（专业，科目，学费）

#爬取过去两年高考录取学校公布的分数线
#所有资料统一整理为一个表格（按照地区分数，学校综合排名进行排列）

#输入姓名，成绩

score=input('请输入您的成绩:')


#设置可删除地区，专业，科目
录取表格=open('D:/最佳录取报考名单.txt','a+')#a+如果文件不存在就创建，存在就在文件内容的后面继续追加
print('最佳录取报考名单.text',file=录取表格)
录取表格.close()


#打印表格，包含姓名，成绩，条件，表格
print(name,score)
