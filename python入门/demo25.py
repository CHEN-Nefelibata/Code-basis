#列表的方法
#1、查询元素下标索引用index()，如果元素不存在会报错
my_list=[1, 2, 3, 'hello', [4, 5], True]
print(my_list.index(3))#3在第二位，输出2

#2、修改元素值
my_list[0]=100
print(my_list)

#3、插入元素值即insert(x,y),在x处插入y
my_list.insert(1,'world')
print(my_list)

#4、追加单个元素值即append(x),在列表尾部加上x
my_list.append("python")
print(my_list)

#5、追加多个元素值即extend(x),在列表尾部加上x
my_list.extend([6, 7, 8])
print(my_list)

my_list=[1, 2, 3, 'hello', [4, 5], True]
#6、删除元素值,分为del和pop
del my_list[0]
print(my_list)

my_list=[1, 2, 3, 'hello', [4, 5], True]
element=my_list.pop(0)#删除第一个元素并将该元素返回至element
print(my_list)
print(element)

#7、删除指定元素值remove(x),删除列表中第一个值为x的元素
my_list=[2,3,1, 2, 3, 'hello', [4, 5], True]
my_list.remove(2)
print(my_list)

my_list=[1, 2, 3, 'hello', [4, 5], True]
#8、清空列表值clear()
my_list.clear()#将列表变为[]
print(my_list)

my_list=[1,1,1,1,2,2,2,3,3,3]
#9、统计元素在列表中出现的次数count(x)
m=my_list.count(1)
print(m)

my_list=[1,1,1,1,2,2,2,3,3,3]
#10、统计列表中所有元素数量len()
n=len(my_list)
print(n)