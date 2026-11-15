#函数进阶之多返回值
def return_num():
    return 1,"hello",True#按顺序用多个变量接收即可

x,y,z=return_num()
print(x)#1
print(y)#hello
print(z)#True