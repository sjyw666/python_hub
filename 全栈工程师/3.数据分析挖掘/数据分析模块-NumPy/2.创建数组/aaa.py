# 研发者：时间遗忘
# 开发时间：2023/8/22 16:07
# print("111")


'''

21013
空（hegiht（i） = 0） &&  两侧相邻高度>hegiht（i）(hegiht（i）+-1)
相邻-》if（相邻是否相等），，else -》for
相邻取最低（木桶效应）
'''


def trap():
    height = [2, 0, 2]
    out = 0
    for nowH in range(max(height)+1):
        while True:
            if height[0] >= nowH and height[len(height) - 1] >= nowH:
                height.reverse()
                break
            if height[len(height) - 1] < nowH:
                height.pop()
            else:
                height.reverse()
        print(height)
        for i in height:
            print(i,nowH)
            if i < nowH:
                print("out:",out)
                out += 1
    return out


print(trap())
