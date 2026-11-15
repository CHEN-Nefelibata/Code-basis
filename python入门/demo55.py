#变量的类型注解
#用途为帮助第三方IDE进行类型检查和代码提示
#类型注解并不会影响代码的运行结果，即使写错也不会报错
#基础类型注解
import random
import json

var_1:int =1
var_2:str = "hello"
var_3:float = 1.0
var_4:bool = True

#类对象类型注解
class Student:
    pass
stu:Student=Student()

#基础容器类型注解
my_list:list = [1,2,3]
my_tuple:tuple = ("hello",1)
my_dict:dict = {"name":"Tom","age":18}

#容器类型详细注解
my_list:list[int] = [1,2,3]
my_tuple:tuple[str, int, bool] = ("hello",1, True)
my_dict:dict[str, int] = {"name":"Tom","age":18}

#注释中的类型注解
var_5=random.randint(1,10) # type: int
var_6=json.dumps({"name":"Tom","age":18}) # type: str
def func():
    return 10
var_7=func() # type: int