# 研发者：时间遗忘
# 开发时间：2023/11/24 17:54
# 特点说明：
'''
创建一个50%的窗口，并居中，将原来的控制台输入换成两个输入框，提示信息放在输入框中用于提示，通过创建一个确定按键模拟回车
输入en，可以中文转英文
输入zh-CN，可以英文转中文
'''
import tkinter as tk
from googletrans import Translator


# 翻译函数
def translate_text():
    text = input_text.get("1.0", 'end-1c')  # 获取输入文本框中的文本内容
    dest_language = input_language.get("1.0", 'end-1c')  # 获取目标语言文本框中的内容

    translator = Translator()  # 创建 Translator 对象
    translated = translator.translate(text, dest=dest_language)  # 使用 Google 翻译库进行翻译

    translated_text.delete("1.0", "end")  # 清空翻译结果文本框
    translated_text.insert("1.0", translated.text)  # 将翻译结果插入到翻译结果文本框中


def on_return(event):
    translate_text()


root = tk.Tk()  # 创建主窗口
screen_width = root.winfo_screenwidth()  # 获取屏幕宽度
screen_height = root.winfo_screenheight()  # 获取屏幕高度

window_width = int(screen_width * 0.5)  # 设置窗口宽度为屏幕宽度的一半
window_height = int(screen_height * 0.5)  # 设置窗口高度为屏幕高度的一半
x = (screen_width - window_width) // 2  # 计算窗口x轴起始位置，使窗口居中显示
y = (screen_height - window_height) // 2  # 计算窗口y轴起始位置，使窗口居中显示

root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # 设置窗口大小和位置

# 创建用于输入文本的文本框，并添加提示文本
input_text = tk.Text(root, height=10, width=50)
input_text.insert("1.0", "请输入要翻译的文本")  # 默认提示文本
input_text.pack()

# 添加提示文本，并设置为灰色、半透明
input_text.config(fg='grey')
input_text.bind("<FocusIn>", lambda event: clear_default_text(input_text))  # 清除默认文本
input_text.bind("<FocusOut>", lambda event: show_default_text(input_text, "请输入要翻译的文本"))  # 显示默认文本

# 创建用于输入目标语言缩写的文本框，并设置提示文本和样式
input_language = tk.Text(root, height=1, width=20)
input_language.insert("1.0", "请输入目标语言的缩写")  # 默认提示文本
input_language.pack()

input_language.config(fg='grey')
input_language.bind("<FocusIn>", lambda event: clear_default_text(input_language))  # 清除默认文本
input_language.bind("<FocusOut>", lambda event: show_default_text(input_language, "请输入目标语言的缩写"))  # 显示默认文本

# 创建翻译按钮
translate_button = tk.Button(root, text="翻译", command=translate_text)
translate_button.pack()

# 创建用于显示翻译结果的文本框
translated_text = tk.Text(root, height=10, width=50)
translated_text.pack()

# 绑定回车键到翻译函数
input_text.bind("<Return>", on_return)
input_language.bind("<Return>", on_return)


# 清除默认文本的函数
def clear_default_text(text_widget):
    if text_widget.get("1.0", "end-1c") == "请输入要翻译的文本" or text_widget.get("1.0","end-1c") == "请输入目标语言的缩写":
        text_widget.delete("1.0", "end")
        text_widget.config(fg='black')


# 显示默认文本的函数
def show_default_text(text_widget, default_text):
    if text_widget.get("1.0", "end-1c").strip() == "":
        text_widget.insert("1.0", default_text)
        text_widget.config(fg='grey')


root.mainloop()  # 运行主循环
