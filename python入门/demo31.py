#数据容器之set集合
#集合不支持元素的重复，且保持无序性，所以不支持下标索引
myset={1,2,3,"python",'a',4,5,6}#若集合内含有多个重复元素，则打乱顺序取其中任意一个相同元素
myset2=set()#表示空集合
print(f"myset的内容是{myset}，类型为{type(myset)}")

myset.add("hello")#添加新元素add
print(myset)

myset.remove("python")#删除元素remove
print(myset)

myset={"hello","python","world"}
element=myset.pop()#随机取一元素并从集合中删去
print(f"去除元素为{element}，剩余集合为{myset}")

myset.clear()#清空集合
print(myset)

set1={1,2,3}
set2={1,4,5}
set3=set1.difference(set2)#取set1有而set2没有的差集
print(set3)

set1={1,2,3}
set2={1,4,5}
set1.difference_update(set2)#消除set1中与set2相同的元素，set2不发生改变
print(set1)
print(set2)

set1={1,2,3}
set2={1,4,5}
set3=set1.union(set2)#合并set1和set2
print(set3)

myset={1,2,3,"python",'a',4,5,6}
print(len(myset))#统计集合元素总数量

#集合遍历只能for循环，因为不支持下标所以不能进行while循环遍历
for element in myset:
    print(element)