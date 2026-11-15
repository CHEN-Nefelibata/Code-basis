#if-elif-else嵌套
#elif跟随if一起出现，else一般放于最后，表示均不满足时
#一个判断中可以有无数个elif，一般只能有一个if和else
score=int(input("请输入成绩："))
if 80<score<=100:
    print("优秀")
elif 60<=score<=80:
    print("良好")
elif score<60:
    print("不及格")
else:
    print("成绩无效")

ticket = bool(input("车票类型："))#bool有字符情况下默认为True，空字符为False
if ticket==True:
    temp= float(input("体温："))
    if 36<=temp<37:
        print("请进入")
    else:
        print("不能进入")
else:
    print("不能进入")