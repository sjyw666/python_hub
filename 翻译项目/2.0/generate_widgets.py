# 研发者：时间遗忘
# 开发时间：2023/11/24 18:29
# 特点说明：
'''

'''
import tkinter as tk
from google_translate import translate_text, on_return

def generate_widgets(root):
    """
    生成界面组件函数

    Args:
    - root: 主窗口对象

    This function generates the necessary widgets for the translation interface within the root window.
    """
    # 创建输入文本框
    input_text = tk.Text(root, height=10, width=50)
    input_text.insert("1.0", "请输入要翻译的文本")  # 默认提示文本
    input_text.pack()

    input_text.config(fg='grey')  # 设置文本颜色为灰色
    input_text.bind("<FocusIn>", lambda event: clear_default_text(input_text))  # 绑定焦点事件
    input_text.bind("<FocusOut>", lambda event: show_default_text(input_text, "请输入要翻译的文本"))

    # 创建输入目标语言的文本框
    input_language = tk.Text(root, height=1, width=20)
    input_language.insert("1.0", "请输入目标语言的缩写")  # 默认提示文本
    input_language.pack()

    input_language.config(fg='grey')  # 设置文本颜色为灰色
    input_language.bind("<FocusIn>", lambda event: clear_default_text(input_language))  # 绑定焦点事件
    input_language.bind("<FocusOut>", lambda event: show_default_text(input_language, "请输入目标语言的
