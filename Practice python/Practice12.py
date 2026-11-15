#函数传入参数的应用
def check(temp):
    print("请出示您的72小时核酸码")
    if temp<=37.3:
        print("体温正常，请入内")
    else:
        print("体温异常，请隔离")

check(38.5)