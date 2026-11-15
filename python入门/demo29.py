#数据容器之字符串
#字符串无法修改
mystr="python and hello"
element=mystr[2]#查询元素
print(element)

element=mystr.index("and")#通过index查找起始字母的下标
print(element)

my_str="itheima and itcast"
element=my_str.replace("it","程序")#通过replace(x,y)将x全部替换为y
print(element)

new_mystr="hello itheima itcast python"
element=new_mystr.split(" ")#通过split将字符串以空格分割，输出为列表形式
print(element)

mystr="  python and hello  "
element=mystr.strip()#通过strip(),括号内无参数则将字符串前后的空格删去；若有参数则去除所有括号内参数
print(element)

mystr="itheima and itcast"
count=mystr.count("it")#通过count统计括号内字符出现次数，注意存在顺序
print(count)

mystr="itheima and itcast"
print(len(mystr))#通过len统计字符串中所有字符数量