# 打印输出
print("hello world")

# 定义一个age变量
age = 18
# 输出age的数据类型
print(type(age))

# True:1; False:0
print(True + True)

# 三引号保留字符串格式
str1="""
   sdlf
     sdlf
   sdlf
"""
print(str1)

# 字符串值前加r表示原始字符串，转义字符失效
str2="你\t好"
str3=r"你\t好"
print(str2)
print(str3)

# 通过索引下标获取字符串
# 一个字符串从左往右索引下标值分别为: 0, 1, 2……; 从右往左索引下标值分别为: -1, -2, -3……
str3 = "好好学习，天天向上";
print(str3[2])

# 字符串切片
# 字符串[起始下标:结束下标:步长]。包含起始，不包含结束。切片不会索引越界。
print(str3[3:4:2])

# 字符串拼接
str4 = "你"
str5 = "好"
print(str4 + str5)

# 字符串重复
str6 = "哈"
print(str6 * 5)

# 去掉字符串首位字符(如果不传参数，是去掉首位空格)
str7 = "aaaxxxbbb "
print(str7.strip("a"))

# 字符串转大写
str8 = "abc";
print(str8.upper())

# 字符串转小写
str9 = "ABC"
print(str9.lower())

# 字符串替换
str10 = "AabcA"
print(str10.replace("A", "B"))

# f-string格式化字符串
name = "张三"
age = 18
print(f"名字:{name}; 年龄: {age}")

# 元组
temp_tuple = ("张三", 1, 2, 3)
print(temp_tuple[1])
# 元组最后一个元素赋值给c，倒数第二个元素赋值给b，其他元素赋值给a
*a, b, c = temp_tuple
print(a)
print(b)
print(c)

# 列表
temp_list = ["张三", 1, True, 18.23, 2, 3, 4, 5]
temp_list[0] = "lisi"
print(temp_list)
new_temp_list = temp_list[1:2:1]
print(new_temp_list)
temp_list[1:7:1] = ["a"]
print(temp_list)

# 集合
empty_set = set()
empty_set.add("a")
print(empty_set)
temp_set = {1, 2, 3}
print(temp_set)

# 字典
employee = {
    "name":"张三",
    "age":18,
    "gender":"male"
}
print(employee.get("name", "xxx"))
employee["age"] = 20
print(employee.get("age", 0))

# 输入
name = input("姓名:")
print(name)

# 输出
print("a", "b", "c", sep=",", end=";")
print()

# if判断
score = input("请输入分数: ")
score = float(score)
if score>=80:
    print("优", end="")
    print("秀", end="\n")
elif score>=60:
    print("及", end="")
    print("格", end="\n")
else:
    print("不及格")

# for循环
person0_dict = {
    "name":"张三",
    "age":18
}
person1_dict = {
    "name":"李四",
    "age":28
}
person_list = [person0_dict, person1_dict]
# 直接取元素值
for person_dict in person_list:
    for key, value in person_dict.items():
        print(key, value)
# 使用索引下标取值
for i in range(0, len(person_list), 1):
    temp_person_dict = person_list[i]
    for temp_key, temp_value in temp_person_dict.items():
        print(temp_key, temp_value)
# 同时获取计数和元素值
for index, person_dict in enumerate(person_list, 3):
    for key, value in person_dict.items():
        print(index, key, value)

# while循环
age = input("请输入年龄: ")
age = int(age)
while age < 18:
    print("年龄不符合条件，请重新输入", end="\n")
    age = input("请输入年龄: ")
    age = int(age)
print("年龄符合条件，成功")

# 函数
def get_name(person_dict=None):
    if person_dict is None:
        person_dict = {}
    return person_dict.get("name")
print(get_name())
person_dict = {
    "name": "刘六"
}
print((get_name(person_dict)))

# 可变参数和可变关键字参数
# *name_list是可变参数(参数名可以随便写，关键是前面的*), **people_dict是可变关键字参数(参数名可以随便写，关键是前面的**)
def hello(*name_tuple, **people_dict):
    for name in name_tuple:
        print(name)
    for key, value in people_dict.items():
        print(key, value)
hello("a", "b", "c", name="1", age=18)

# 返回多个值
def multi_return():
    return 1, 2, 3
a, *b = multi_return()
print(a)
print(b)

# 回调函数，将函数作为变量传进去
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def calculate(fun, a, b):
    return fun(a, b)
print(calculate(add, 1, 2))
print(calculate(sub, 3, 3))

# 使用递归实现阶乘
def temp_factorial(n):
    if n == 1:
        return 1
    return n*temp_factorial(n-1)
print(temp_factorial(5))

# 闭包
def outer():
    count = 0
    num = 0
    def inner():
        nonlocal count
        count += 1
        nonlocal num
        num += 2
        return num, count
    return inner
a = outer()
b = outer()
print(a())
print(a())
print(b())
print(b())
for name, cell in zip(a.__code__.co_freevars, a.__closure__):
    print(name, "=", cell.cell_contents)

# 装饰器
def calculate(a, b):
    print("正在执行原函数")
    return a + b
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("开始执行")
        result = func(*args, **kwargs)
        print("结束执行")
        return result
    return wrapper
calculate = log_decorator(calculate)
print(calculate(1, 2))

# 匿名函数
sum_func = lambda x, y: x + y
print(sum_func(1, 2))

# 高阶函数
def multiply_func(a, b):
    return a * b
def higher_order_func(func, a, b):
    return func(a, b)
print(higher_order_func(multiply_func, 2, 3))

# map
def map_learn0():
    temp_list = [1, 2, 3]
    iterator = map(
        lambda x: x + 1,
        temp_list
    )
    return iterator
print(list(map_learn0()))

def map_learn1():
    courses = [
        {
            "title": "Python",
            "level": 5
        },
        {
            "title": "java",
            "level": 8
        },
        {
            "title": "js",
            "level": 3
        },
    ]
    iterator = map(lambda temp:temp["title"], courses)
    return iterator
print(list(map_learn1()))


# sorted
def sorted_learn0():
    temp_list = [1, 2, 3, 9, 8, 3, 6]
    sorted_list = sorted(temp_list, key=lambda x: x, reverse=False)
    return sorted_list
print(sorted_learn0())

def sorted_learn1():
    courses = [
        {
            "title": "Python",
            "level": 5
        },
        {
            "title": "java",
            "level": 8
        },
        {
            "title": "js",
            "level": 3
        },
    ]
    sorted_courses = sorted(courses, key=lambda course: course["level"], reverse=False)
    return sorted_courses
print(sorted_learn1())

# filter
def learn_filter():
    courses = [
        {
            "title": "Python",
            "level": 5
        },
        {
            "title": "java",
            "level": 8
        },
        {
            "title": "js",
            "level": 3
        },
    ]
    iterator = filter(lambda course: course["level"]==5, courses)
    return iterator
print(list(learn_filter()))

# 三目运算符
def conditional_expression_learn():
    result = 1 if False else 2
    return result
print(conditional_expression_learn())

# 推导式练习

## 1~100 中 3 的倍数
print([x for x in range(0, 100) if x%3==0])

## 列表 ["a", "bb", "ccc"] 转成 {单词: 长度} 字典
print({x:len(x) for x in ["a", "bb", "ccc"]})