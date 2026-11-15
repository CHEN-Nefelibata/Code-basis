#函数嵌套调用
def function_b():
    print("---2---")
def function_a():
    print("---1---")
    function_b()
    print("---3---")

function_a()    