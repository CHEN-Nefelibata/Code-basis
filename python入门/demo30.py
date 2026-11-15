#数据容器之序列及其切片操作
#语法为序列[起始下标:终止下标:步长]

#列表
mylist=[0,1,2,3,4,5,6]
result=mylist[1:4:1]#步长默认为1，可省略
print(result)

result=mylist[3:1:-1]
print(result)

#元组
mytuple=(0,1,2,3,4,5,6)
result=mytuple[:]#空冒号表示从头到尾，默认步长为1
print(result)

result=mytuple[::-2]
print(result)

#字符串
mystr="0123456"
result=mystr[::2]#从头到尾，步长为2
print(result)

result=mystr[::-1]#表示从尾取到头，翻转，步长为1
print(result)