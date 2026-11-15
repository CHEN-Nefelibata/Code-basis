#类的成员方法
#类中定义属性（变量）表示成员变量，定义行为（函数）表示成员方法
#定义在类中的函数名为方法
class Student:
    name=None

    def say_hi1(self):#必须填写self参数，表示当前对象
        print(f"大家好，我是{self.name}")

    def say_hi2(self,msg):#必须填写self参数，表示当前对象
        print(f"大家好，我是{self.name},{msg}")#设置msg变量，自由输入进行调用
stu1=Student()
stu1.name="小明"
stu1.say_hi1()

stu2=Student()
stu2.name="小红"
stu2.say_hi1()

stu3=Student()
stu3.name="小刚"
stu3.say_hi2("很高兴认识大家")

stu4=Student()
stu4.name="小李"
stu4.say_hi2("hello everyone")
