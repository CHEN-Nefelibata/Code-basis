#数据容器之列表
#空列表为[]或list()
#列表支持多种类型，可以嵌套
#正向排序为0，1，2，3。。。；反向排序为。。。-5，-4，-3，-2，-1
my_list=[1, 2, 3, 'hello', [4, 5], True]
print(my_list)
print(type(my_list))
print(my_list[0])  #正向索引
print(my_list[-1]) #反向索引
print(my_list[4][1]) #嵌套索引