#异常
#异常具有传递性
#1、常规捕获
#try:
#    f=open("D:/编程/python文件/abc.txt","r")
#except:
#    print("出现异常，改为w模式打开")
#    f=open("D:/编程/python文件/abc.txt","w")
#2、指定捕获
try:
    print(name)
except NameError as e:#多种错误类型,如此时为未定义name
    print("出现异常")
    print(e)
#3、捕获多个异常
try:
    print(1/0)
except (NameError,ZeroDivisionError) as e:#未正确定义异常类型则无法捕获异常
    print("出现异常")
    print(e)
#4、捕获全部异常
try:
    f=open("D:/编程/python文件/abc.txt","r")
except Exception as e:
    print("出现异常")
    print(e)
#5、异常else
try:
    f=open("D:/编程/python文件/abc.txt","r")
except Exception as e:
    f=open("D:/编程/python文件/abc.txt","w")
    print(e)
else:
    print("正常")
finally:
    print("无论是否正常都执行")
    f.close()