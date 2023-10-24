# 研发者：时间遗忘
# 开发时间：2023/10/21 20:21
# 特点说明：无
'''
类的组成：
    （初始化方法）
    类属性：直接写在类里面的变量
    实例方法：方法就是类里面定义的函数，要求参数中使用self（规范）
    静态方法：使用@staticmethod进行修饰，静态中不允许使用self
    类方法：使用@classmethod进行修饰，类方法中要求传一个cls
'''

class Student:      #Student:类名，由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_place='吉林'   # 类属性

    def __init__(self,name,age):        # 初始化方法，self后面可以传参数
        self.name = name                 # 赋值操作
        self.age = age
    '''self.name称为实体属性，进行了一个叫赋值的操作；
        局部变量赋给实体属性，实体属性可以不和局部变量名相同，但一般和实体属性名相同
    '''


    def eat(self):      # 实例方法
        print(self.age,"岁的干饭人：",self.name)

    @staticmethod       # 静态方法
    def person():
        print("静态方法")

    @classmethod        # 类方法
    def food(cls):
        print("类方法")


print(Student)
print(id(Student))      #查看是否分配内存地址
print(type(Student))
