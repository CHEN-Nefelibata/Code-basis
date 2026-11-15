#元组的基本操作
t1=("name",18,["football","music"])
#1、查找位置
print(t1.index(18))
#2、查询姓名
print(t1[0])
#3、删除爱好
del t1[2][1]
print(t1)
#4、添加爱好至列表中
t1[2].insert(0,"coding")
print(t1)