#常见魔术方法
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

#__str__()字符串方法
    def __str__(self):#调用__str__()方法时会返回一个字符串，该字符串通常用于描述对象的属性或状态。
        return f"姓名：{self.name}，年龄：{self.age}"

#__lt__()比较方法
    def __lt__(self,other):#调用__lt__()方法时会比较两个对象的大小关系，返回一个布尔值。
        return self.age<other.age

#__le__()比较方法
    def __le__(self,other):#调用__le__()方法时会比较两个对象的大小关系，返回一个布尔值。
        return self.age<=other.age  

#__eq__()比较方法
    def __eq__(self,other):#调用__eq__()方法时会比较两个对象的相等关系，返回一个布尔值。
        return self.age==other.age 
stu1=Student("张三",18)
stu2=Student("李四",20)
print(stu1)#输出内存地址，需调用__str__()方法才能输出对象的属性
print(str(stu1))
print(stu1<stu2)#调用__lt__()方法比较两个对象的大小关系
print(stu1>stu2)#调用__lt__()方法比较两个对象的大小关系
print(stu1<=stu2)#调用__le__()方法比较两个对象的大小关系
print(stu1>=stu2)#调用__le__()方法比较两个对象的大小关系
print(stu1==stu2)#调用__eq__()方法比较两个对象的相等关系，若无__eq__()方法则会比较两个对象的内存地址，则会输出False