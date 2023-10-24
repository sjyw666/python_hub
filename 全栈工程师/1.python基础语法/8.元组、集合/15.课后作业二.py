# 研发者：时间遗忘
# 开发时间：2023/5/12 17:22
'''import random

qList = ["1111", "2222", "3333"]

for i in range(8):
    v = random.choice(qList)
    i = random.randint(0, 3)

    answer = v[i]
    r = list(v)
    r[i] = "_"
    print("".join(r))
    answer_input = input("答案是：")

    answer = v[i]

    if answer_input == "":
        print("过")
    elif answer_input == answer:
        print("正确，你真棒")
    else:
        print("错了")'''


import random

Idiom_List={
    "念念不忘":{"__念不忘":"念",
              "念__不忘":"念",
              "念念__忘":"不",
              "念念不忘":"忘"},
    "落花流水":{"__花流水":"落",
              "落__流水":"花",
              "落花__水":"流",
              "落花流__":"水"},
    "马到成功":{"__到成功":"马",
              "马__成功":"到",
              "马到__功":"成",
              "马到成__":"功"},
    "白手起家":{"__手起家":"白",
              "白__起家":"手",
              "白手__家":"起",
              "白手起__":"家"},
    "十字路口":{"__字路口":"十",
              "十__路口":"字",
              "十字__口":"路",
              "十字路__":"口"},
    "春风化雨":{"__风化雨":"春",
              "春__化雨":"风",
              "春风__雨":"化",
              "春风化__":"雨"},
    "一往无前":{"__往无前":"一",
              "一__无前":"往",
              "一往__前":"无",
              "一往无__":"前"},
}



Initial_score=20
for i in range(8):

    word = random.choice(list(Idiom_List.keys()))  # 得到一个随机词


    word_dictionary = Idiom_List.get(word)  # 得到对应单词的字典


    word_all_topic = word_dictionary.keys()  # 单词所有随机空的题目


    topic = random.choice(list(word_all_topic))  # 设置题目
    print(topic)

    answer = word_dictionary.get(topic)  # 设置答案


    answer_input = input("输入答案：")
    if answer_input==answer:
        print("正确，你真棒")
        Initial_score+=2

    elif answer_input=="":
        print("过")

    else:
        print("错了，正确答案："+answer)
        Initial_score-=2

print("选手最后得分：",Initial_score)