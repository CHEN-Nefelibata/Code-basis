#格式化
name="sixstar"
print(name)
print("我的名字是：%s"% name)#%s定义字符串，%作占位符，不输出
age=18
print("我的年龄是：%d"% age)#%d定义整形
print("我的名字是：%s  我的年龄是：%d"%(name,age))
a=123
print("%6d"% a)#不足d前数字补空白
print("%06d"% a)#6d前加什么将补空白改为补什么
b=1.2
print("%f"% b)#默认6位小数，遵循四舍五入原则
print("%.4f"% b)#f前加.x为x位小数，遵循四舍五入原则
print("我是%%的%%")#%%输出%字符
print(f"我的名字是{name},我的年龄是{age}")#f"{}"格式化