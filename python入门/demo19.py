#函数初步
def my_len(data):#定义函数
    count=0
    for i in data:
        count+=1
    print(f"字符串长度为：{count}")
my_len("hello world")
my_len("python")