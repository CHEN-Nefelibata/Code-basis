#for循环和continue，break综合
money=10000
for i in range(1,21):
    import random
    num=random.randint(1,10)
    if num<5:
        print(f"员工{i}绩效考核不合格，不发工资，下一位")
        continue
    if money>=1000:
        money-=1000
        print(f"员工{i}绩效考核合格，发工资1000元，剩余工资{money}元")
    else:
        print(f"员工{i}绩效考核合格，但公司钱不够发工资，停止发工资")
        break