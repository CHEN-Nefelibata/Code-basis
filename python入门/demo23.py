#函数变量的作用域
a=100
def func_a():
    global a#global声明a为全局变量 ，可直接赋值替换
    a=200
    print(a)

func_a()
print(a)