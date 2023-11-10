# 研发者：时间遗忘
# 开发时间：2023/10/28 14:44
# 特点说明：无
class Student():
    location = '学校'
    def __init__(self,name,age):
        self.name =name
        self.age = age
    @staticmethod
    def eat():
        print('饭')

    @classmethod
    def play(cls):
        print('玩')

stu1 = Student('张三',18)
stu2 = Student('李四',19)

print(stu1.eat())
print()

