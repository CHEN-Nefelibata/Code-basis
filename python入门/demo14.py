#if判断
score=int(input("请输入成绩："))#int(input())将字符串类型改为整形
if score>=60:#输入内容默认字符串类型，需加''
    print("good")
if score<60:
    print("bad")

a="嘿嘿"
b="哈哈"
if a=="嘿嘿"and b=="哈哈":#and表示逻辑运算符并且，需要两边全部满足才能进行下一步
    print("很开心")

fruit='苹果'
if fruit=='苹果'or fruit=='桃子':#or表示逻辑运算符或者，两边有一边满足即可进行下一步
    print("是水果")

print(not 3>9)#not表示否定，即为9>3

#三目运算符：真结果+if+判断条件+else+假结果
c=8
d=5
if c>=d:
    print("c大于等于d")
else:
    print("c小于d")
#可改写为
print("c大于等于d") if c>=d else print("c小于d")