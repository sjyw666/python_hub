# 研发者：时间遗忘
# 开发时间：2023/10/28 16:29
# 特点说明：输入藏头诗就可以输出藏的话
print("请输入4句藏头诗")
i = 0
hide_head_poem = ""
while i<4:
    # 输入字符串
    poem = str(input(""))
    i+=1
    hide_head_poem = hide_head_poem + poem[0]

print(f'藏头诗为：{hide_head_poem}')