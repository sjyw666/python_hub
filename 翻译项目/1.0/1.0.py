# 研发者：时间遗忘
# 开发时间：2023/11/24 17:26
# 特点说明：
'''
具有基础翻译功能
'''
from googletrans import Translator

def translate_text(text, dest_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

if __name__ == "__main__":
    text_to_translate = input("请输入要翻译的文本：")
    destination_language = input("请输入目标语言的缩写（例如，英文为'en'，中文为'zh-CN'）：")
    translated_text = translate_text(text_to_translate, destination_language)
    print(f"翻译结果：{translated_text}")
