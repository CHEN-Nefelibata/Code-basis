#return的用法
def add(a,b):
    result=a+b
    return result#函数调用到return时会结束函数的执行,并将返回值传给调用函数的变量
    #不写return时,函数默认返回None

r=add(1,2)
print(r)