# 研发者：时间遗忘
# 开发时间：2023/5/12 16:48
import time

print("百词斩")
input_time = int(input("请设置每个单词停留的时间"))

content = {
    "counter": "",
    "stall": "",
    "shelf": "",
    "price tag": "",
    "discount": "",
    "change": "",
    "bank": "",
    "shop": "",
    "柜台": "",
    "售货架": "",
    "货架": "",
    "标价签": "",
    "打折扣": "",
    "零钱": "",
    "银行": "",
    "商店": ""
}

# print(input_time)
# key=content.keys()
for i in content:
    print(i, end="")
    print("________")
    time.sleep(input_time)
