#初识面向对象
class Student:#设计类
    name=None#记录姓名
    gender=None#记录性别
    nationality=None#记录国籍
    native_place=None#记录籍贯
    age=None#记录年龄
stu1=Student()#创建对象
stu1.name="林俊杰"#给对象属性赋值
stu1.gender="男"
stu1.nationality="中国"
stu1.native_place="福建省"
stu1.age=30
print(stu1.name)
print(stu1.gender)
print(stu1.nationality)
print(stu1.native_place)
print(stu1.age)