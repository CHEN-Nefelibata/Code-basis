#while循环
i=1
#while i<=100:#只要条件不是0或False，其他值也会进入死循环
#   print("Good!")
#   i+=2
s=0
while i<=50:
    s+=i#s为每次i的值之和，即为1+2+3+4+··· ···
    i+=1#i每次累加1
    print(s)