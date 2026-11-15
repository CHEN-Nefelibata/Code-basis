#while循环猜测随机数
import random
num=random.randint(1,100)
flag=True
count=0
while flag:
    guess_num=int(input("请输入您猜测的数字："))
    count+=1#计算猜测次数
    if guess_num==num:
        print("猜对了")
        flag=False#终止循环的条件
    else:
        if guess_num<num:
            print("您猜小了")
        else:
            print("您猜大了")
print(f"您猜测了{count}次")