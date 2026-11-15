#构造方法
#__init__()方法是类的构造方法，当创建类的实例时会自动调用该方法。它通常用于初始化对象的属性。
#__init__()方法属于魔术方法
class Student:
    name=None#可以省略
    age=None#可以省略
    tel=None#可以省略

    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print("构造方法被调用了")

stu=Student("张三",18,"12345678901")#创建类的实例时会自动调用构造方法

print(stu.name)
print(stu.age)
print(stu.tel)