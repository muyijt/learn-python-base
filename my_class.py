# 封装一个类。类名后可以不加()，不加括号代表继承自Object；加了括号，括号要指定上继承自哪个类
class Student:
    # 初始化函数。除self参数外，其他参数一般设置为None，表示那个参数的默认值为None
    def __init__(self, name=None, age=None):
        # 属性以__开头，代表是私有属性
        # 使用初始化函数中参数为私有属性赋值
        self.__name = name
        self.__age = age

    # 获取name属性的值
    @property
    def name(self):
        return self.__name

    # 设置name属性的值
    @name.setter
    def name(self, value):
        self.__name = value

    # 获取age属性的值
    @property
    def age(self):
        return self.__age

    # 设置age属性的值
    @age.setter
    def age(self, value):
        self.__age = value

# 创建类的对象时，如果有对应属性的参数没传，实例化出的对象该属性的值就是初始化函数中默认值
stu1 = Student(age=18)
# 获取对象的属性值时会调用类中的对应的获取属性值的方法
print(stu1.name)
print(stu1.age)
# 设置对象的属性值时会调用类中的对应的设置属性值的方法
stu1.name="李悝"
print(stu1.name)
print(stu1.age)

#######################################################################################################
# 继承
class People:
    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value

# 括号中的类就是父类
class Student(People):
    def __init__(self, name=None, age=None, class_name=None):
        super().__init__(name, age)
        self.__class_name = class_name

    @property
    def class_name(self):
        return self.__class_name
    @class_name.setter
    def class_name(self, value):
        self.__class_name = value

stu1 = Student(name="sam", age=20, class_name="Python")
print(f"姓名:{stu1.name}，班级:{stu1.class_name}")
stu1.class_name="Java"
print(f"姓名:{stu1.name}，班级:{stu1.class_name}")

#########################################################################################################
# 多态
class Cash:
    def pay(self):
        print("现金支付")

class Qr:
    def pay(self):
        print("扫码支付")

class People:
    def __init__(self, pay_able):
        self.__pay_able = pay_able

    def buy(self):
        self.__pay_able.pay()

people0 = People(Cash())
people0.buy()
people1 = People(Qr())
people1.buy()
