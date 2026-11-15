#函数及方法的类型注解(形参及返回值)
#def 方法名(参数名: 参数类型, 参数名: 参数类型) -> 返回值类型:
#类型注解并不会影响代码的运行结果，即使写错也不会报错
def add(x:int,y:int)->int:
    return x+y
add(1,2)

def func(data: list) -> list:
    return data
func(1) # 这里传入的参数类型不对，但不会报错