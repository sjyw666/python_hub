#研发者：时间遗忘
#开发时间：2022/11/5 13:55

choir=input('请选择是否查询票房：y查询票房 n查看全部票房')
film=['第1名：《长津湖》57.44亿','第2名：《战狼2》56.95亿','第3名：《你好，李焕英》54.14亿','第4名：《哪吒之魔童降世》50.36亿','第5名：《流浪地球》46.91亿']
if choir=='y':
    query=eval(input('请输入您要查询的电影票房：第？名'))
    if type(query)==int:
        if query>=1 and query<=5:
            print(film[query-1])
        else:
            print('输入错误，已显示所有票房')
            for index, item in enumerate(film):
                print(item)
    else:
        print('输入错误，已显示所有票房')
        for index, item in enumerate(film):
            print(item)

elif choir=='n':
    print('已显示所有票房')
    for index, item in enumerate(film):
        print(item)

else:
    print('输入错误，已显示所有票房')
    for index, item in enumerate(film):
        print(item)



