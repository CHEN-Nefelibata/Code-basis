#while循环嵌套
i=1
while i<=3:
    print(f"外循环执行{i}次")#第i次下套一个j次循环
    j=1
    while j<=5:
        print(f"内循环执行{j}次")
        j+=1
    i+=1