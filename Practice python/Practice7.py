#while循环嵌套输出九九乘法表
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{i}*{j}={i*j}",end="\t")
        j+=1
    i+=1
    print()#输出空白即为换行