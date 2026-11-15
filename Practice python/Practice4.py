#if嵌套
import random
num = random.randint(1,10)#随机生成1-10
i=int(input("输入您要猜测的数字："))
if i==num:
    print("恭喜您第一次就对了")
else:
    if i<num:
        print("比答案小")
    else:
        print("比答案大")

    i=int(input("请再次输入您猜测的答案："))
    if i==num:
        print("恭喜您第二次猜对了")
    else:
        if i<num:
            print("比答案小")
        else:
            print("比答案大")

        i=int(input("请第三次输入您的答案："))
        if i==num:
            print("恭喜您第三次答对了")
        else:
            if i<num:
                print("比答案小")
            else:
                print("比答案大")

            i=int(input("请输入您的最终答案："))
            if i==num:
                print("恭喜您最终答对了")
            else:
                print("机会用完了，您没答对")