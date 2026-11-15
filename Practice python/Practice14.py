#列表常用功能
mylist=[21,25,21,23,22,20]#1、定义+变量接收
print(mylist)#输出列表

mylist.append(31)#2、追加单个元素
print(mylist)

mylist.extend([29,33,30])#3、追加多个元素
print(mylist)

num1=mylist[0]#4、取出第一个元素
print(num1)

num2=mylist[-1]#5、取出最后一个元素
print(num2)

location=mylist.index(31)
print(location)