#1、for循环
#str='helloworld'
#for i in str:#i为临时变量，可随便写,字符串为可迭代对象，整形和浮点型不行
#    print(i)

#2、range(start,end,step)用来记录循环次数
#for i in range(1,6):#范围为[1,6),若括号里只有一个数，表示循环次数，默认从0开始
#    print(i)

#3、s=0
#for i in range(1,101):
#    s+=i
#print(s)

#4、break表示终止循环，continue表示终止该循环进入下一循环
#i=1
#while i<=5:
#    print(i)
#    if i==3:
#        print("OK")
#        break
#    i+=1

#5、continue前要修改计数器，否则陷入死循环
i=1
while i<=5:
    print(i)
    if i==3:
        print("out")
        i+=1
        continue
    i+=1