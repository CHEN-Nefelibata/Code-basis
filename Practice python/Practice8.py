#for循环计数字符串中字母数量
name = "itheima is a brand of itcast"
count = 0
for i in name:
    if i=="a":
        count+=1
print(f"被统计的字符串中有{count}个a")