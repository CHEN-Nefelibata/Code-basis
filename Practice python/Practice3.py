#if-elif-else语句
num=10
if int(input("请输入您的数字："))==num:
    print("恭喜您猜对了")
elif int(input("猜错了再来一次："))==num:
    print("恭喜您猜对了")
else:
    print("您猜错了")