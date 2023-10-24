# 研发者：时间遗忘
# 开发时间：2023/10/21 20:35
# 特点说明：无
'''
对象的创建又称为类的实例化
语法：
    实例名 = 类名
意义：
    有了实例，就可以调用类中的内容
输出对象的值实际是输出16进制的一个内存地址，根据类对象创建出来的叫做实例对象，创建完后就可以使用这个类的实例属性以及这个类的相关方法
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

'''
实例后再调用只需要   实例对象.属性/方法  就可以进行调用
实例=类（参数1，参数2）   等价于     类.方法（实例/类的对象）#实际上就是调用self      
'''
shilim = Student('张三',18)           # 创建Student类的实例对象
shilim.person()         # 实例方法
shilim.eat()
shilim.food()
print(shilim.name)      # 实例属性
print(shilim.age)

print(shilim)
print(id(shilim))
print(type(shilim))


print('-'*70)


print(Student)
print(id(Student))      # 查看是否分配内存地址
print(type(Student))
