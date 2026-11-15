#函数综合
money=5000000
name=input("请输入您的姓名：")
def query(head):
    if head:
        print("-----------查询余额-----------")
    print(f"您的余额为{money}元")
def saving(num):
    global money
    money+=num
    print("-----------存款-----------")
    print(f"{name}，您存款{num}元成功")
    query(False)
def withdraw(num):
    global money
    if num>money:
        print("余额不足，取款失败")
    else:
        money-=num
        print("-----------取款-----------")
        print(f"{name}，您取款{num}元成功")
        query(False)
def main():
    print("-----------欢迎使用ATM机-----------")
    print(f"{name},您好，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

while True:
    keyboard_input=main()
    if keyboard_input=="1":
        query(True)
        continue
    elif keyboard_input=="2":
        saving(int(input("请输入存款金额：")))
        continue
    elif keyboard_input=="3":
        withdraw(int(input("请输入取款金额：")))
        continue
    elif keyboard_input=="4":
        print("退出成功，欢迎下次使用")
        break
    else:
        print("输入有误，请重新输入")