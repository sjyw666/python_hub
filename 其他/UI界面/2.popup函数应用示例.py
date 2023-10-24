#研发者：时间遗忘
#开发时间：2023/2/24 9:56
import PySimpleGUI as sg
sg.popup(
    '小白超可爱的',#显示的内容
    '小白宇宙第一可爱',#显示的内容
    title='嗷呜',#窗口名
    button_color=('#000000','#FFFFFF'),#按钮颜色（前景色和背景色）
    line_width=10,#每一行的字数
    custom_text='？',#按键显示内容
    location=(857,857),#屏幕显示的位置
    auto_close=True,#会自动关闭
    auto_close_duration=5,#自动关闭的时间，单位秒
    text_color='red',#文字颜色
    grab_anywhere=True,#窗口是否可以移动
    font='23',#字体大小
)
