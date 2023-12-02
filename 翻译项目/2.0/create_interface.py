# 研发者：时间遗忘
# 开发时间：2023/11/24 18:29
# 特点说明：
'''

'''
import tkinter as tk

def create_interface(root):
    """
    创建界面函数

    Args:
    - root: 主窗口对象

    This function creates the interface for text translation within the root window.
    """
    # 获取屏幕尺寸信息
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 设置窗口尺寸和位置
    window_width = int(screen_width * 0.5)
    window_height = int(screen_height * 0.5)
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 创建输入文本框和目标语言缩写文本框
    input_text = tk.Text(root, height=10, width=50)
    input_text.insert("1.0", "请输入要翻译的文本")  # 默认提示文本
    input_text.pack()

    input_text.config(fg='grey')  # 设置文本颜色为灰色
    input_text.bind("<FocusIn>", lambda event: clear_default_text(input_text))  # 绑定焦点事件
    input_text.bind("<FocusOut>", lambda event: show_default_text(input_text, "请输入要翻译的文本"))

    input_language = tk.Text(root, height=1, width=20)
    input_language.insert("1.0", "请输入目标语言的缩写")  # 默认提示文本
    input_language.pack()

    input_language.config(fg='grey')  # 设置文本颜色为灰色
    input_language.bind("<FocusIn>", lambda event: clear_default_text(input_language))  # 绑定焦点事件
    input_language.bind("<FocusOut>", lambda event: show_default_text(input_language, "请输入目标语言的缩写"))

    # 创建翻译按钮
    translate_button = tk.Button(root, text="翻译", command=lambda: translate_text(input_text, input_language, translated_text))
    translate_button.pack()

    # 创建用于显示翻译结果的文本框
    translated_text = tk.Text(root, height=10, width=50)
    translated_text.pack()

    # 绑定回车键到翻译函数
    input_text.bind("<Return>", lambda event: on_return(event, input_text, input_language, translated_text))
    input_language.bind("<Return>", lambda event: on_return(event, input_text, input_language, translated_text))

def clear_default_text(text_widget):
    """
    清除默认文本函数

    Args:
    - text_widget: 文本框对象

    This function clears the default text when the text widget is clicked.
    """
    if text_widget.get("1.0", "end-1c") == "请输入要翻译的文本" or text_widget.get("1.0", "end-1c") == "请输入目标语言的缩写":
        text_widget.delete("1.0", "end")
        text_widget.config(fg='black')

def show_default_text(text_widget, default_text):
    """
    显示默认文本函数

    Args:
    - text_widget: 文本框对象
    - default_text: 默认显示的文本

    This function shows the default text when the text widget is left empty.
    """
    if text_widget.get("1.0", "end-1c").strip() == "":
        text_widget.insert("1.0", default_text)
        text_widget.config(fg='grey')
