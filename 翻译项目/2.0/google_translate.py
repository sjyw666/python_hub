# 研发者：时间遗忘
# 开发时间：2023/11/24 18:29
# 特点说明：
'''

'''
from googletrans import Translator


def translate_text(input_text, input_language, translated_text):
    """
    调用 Google API 进行翻译函数

    Args:
    - input_text: 输入文本框对象
    - input_language: 目标语言文本框对象
    - translated_text: 用于显示翻译结果的文本框对象

    This function uses Google Translate API to translate the text entered in input_text to the target language specified in input_language, and displays the result in translated_text.
    """
    text = input_text.get("1.0", 'end-1c')  # 获取输入文本框中的文本内容
    dest_language = input_language.get("1.0", 'end-1c')  # 获取目标语言文本框中的内容

    translator = Translator()  # 创建 Translator 对象
    translated = translator.translate(text, dest=dest_language)  # 使用 Google 翻译库进行翻译

    translated_text.delete("1.0", "end")  # 清空翻译结果文本框
    translated_text.insert("1.0", translated.text)  # 将翻译结果插入到翻译结果文本框中


def on_return(event, input_text, input_language, translated_text):
    """
    回车键事件绑定函数

    Args:
    - event: 事件对象
    - input_text: 输入文本框对象
    - input_language: 目标语言文本框对象
    - translated_text: 用于显示翻译结果的文本框对象

    This function binds the 'Return' key event to call the translation function when pressed.
    """
    translate_text(input_text, input_language, translated_text)  # 调用翻译函数
