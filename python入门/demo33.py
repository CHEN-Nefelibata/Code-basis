#数据容器通用操作
mylist=[1,2,3,4,5]
mytuple=(1,2,3,4,5)
mystr="abcdefg"
myset={1,2,3,4,5}
mydict={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}

#len统计元素个数
print(f"元素个数为{len(mylist)}")
print(f"元素个数为{len(mytuple)}")
print(f"元素个数为{len(mystr)}")
print(f"元素个数为{len(myset)}")
print(f"元素个数为{len(mydict)}")

#max选取最大元素
print(f"元素最大为{max(mylist)}")
print(f"元素最大为{max(mytuple)}")
print(f"元素最大为{max(mystr)}")
print(f"元素最大为{max(myset)}")
print(f"元素最大为{max(mydict)}")

#min选取最小元素
print(f"元素最小为{min(mylist)}")
print(f"元素最小为{min(mytuple)}")
print(f"元素最小为{min(mystr)}")
print(f"元素最小为{min(myset)}")
print(f"元素最小为{min(mydict)}")

#list转列表
print(f"列表转列表为{list(mylist)}")
print(f"元组转列表为{list(mytuple)}")
print(f"字符串转列表为{list(mystr)}")
print(f"集合转列表为{list(myset)}")
print(f"字典转列表为{list(mydict)}")

#tuple转元组
print(f"列表转元组为{tuple(mylist)}")
print(f"元组转元组为{tuple(mytuple)}")
print(f"字符串转元组为{tuple(mystr)}")
print(f"集合转元组为{tuple(myset)}")
print(f"字典转元组为{tuple(mydict)}")

#str转字符串
print(f"列表转字符串为{str(mylist)}")
print(f"元组转字符串为{str(mytuple)}")
print(f"字符串转字符串为{str(mystr)}")
print(f"集合转字符串为{str(myset)}")
print(f"字典转字符串为{str(mydict)}")

#set转集合
print(f"列表转集合为{set(mylist)}")
print(f"元组转集合为{set(mytuple)}")
print(f"字符串转集合为{set(mystr)}")
print(f"集合转集合为{set(myset)}")
print(f"字典转集合为{set(mydict)}")

#进行容器的排序sorted()默认为正向即reverse=False
print(f"列表的排序结果为{sorted(mylist)}")
print(f"元组的排序结果为{sorted(mytuple)}")
print(f"字符串的排序结果为{sorted(mystr)}")
print(f"集合的排序结果为{sorted(myset)}")
print(f"字典的排序结果为{sorted(mydict)}")
#反向为reverse=True
print(f"列表的排序结果为{sorted(mylist,reverse=True)}")
print(f"元组的排序结果为{sorted(mytuple,reverse=True)}")
print(f"字符串的排序结果为{sorted(mystr,reverse=True)}")
print(f"集合的排序结果为{sorted(myset,reverse=True)}")
print(f"字典的排序结果为{sorted(mydict,reverse=True)}")