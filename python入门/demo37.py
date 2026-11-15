#匿名函数之作为参数传递
def test_func(compute):
    result=compute(1,2)#确定compute为函数
    print(f"compute参数类型为{type(compute)}")
    print(f"计算结果为{result}")

def compute(x,y):
    return x+y

test_func(compute)

#匿名函数之lambda函数
#与一般函数区别在于，一般函数具有对应名称，可重复使用；而lambda函数不具有名称，只可临时使用一次
def testfunc(summer):
    result=summer(1,2)
    print(result)

testfunc(lambda x,y:x+y)