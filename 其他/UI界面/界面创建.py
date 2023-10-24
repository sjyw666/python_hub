#研发者：时间遗忘
#开发时间：2022/11/23 9:13

#导入库
import PySimpleGUI as sg

#定义布局，确定行数
layout=[

            [sg.Text('请输入您的信息')],#第一行
            [sg.Text('姓名'),sg.InputText('')],#一个文本，一个输入框，中间用逗号隔开
            [sg.Text('性别'),sg.InputText('')],
            [sg.Text('民族'),sg.InputText('')],
            [sg.Button('确定'),sg.Button('取消')]#两个按键
                     ]

#创建窗口
window=sg.Window('Python GUI',layout)#括号里面一个是窗口的标签，一个是引入的布局

#事件循环
while True:
    event,values=window.read()#窗口的读取，有两个返回值（1，事件  2，值）

    if event==None:#窗口关闭事件
        break

#关闭窗口
window.close()



