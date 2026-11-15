#模块
#1、import直接调用
#import time#调用time模块
#print("你好")
#time.sleep(5)#暂停运行5s
#print("我好")

#2、from import调用
#from time import sleep
#print("你好")
#sleep(5)
#print("我好")

#3、*调用全部模块
#from time import *
#print("你好")
#sleep(5)
#print("我好")

#4、as加别名
#import time as t#改time为t
#print("你好")
#t.sleep(5)
#print("我好")

from time import sleep as sl
print("你好")
sl(5)#改sleep为sl
print("我好")