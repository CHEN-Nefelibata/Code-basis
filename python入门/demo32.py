#数据容器之字典dict={key:value}
#通过某变量可查找对应的另一变量
#若有重复，则后一个将覆盖前一个
mydict={"A":99,"B":88,"C":77}
my_dict={}#空字典，也可以my_dict=dict()
print(f"字典内容为{mydict},类型为{type(mydict)}")

score=mydict["A"]#调用字典
print(score)

#字典的嵌套
mydict1={"A":{"语文":77,"数学":66,"英语":33},"B":{"语文":88,"数学":86,"英语":55},"C":{"语文":99,"数学":96,"英语":66}}
score1=mydict1["A"]["语文"]
print(score1)

#字典的常用操作
mydict={"A":99,"B":88,"C":77}
mydict["A"]=100#更新字典
mydict["D"]=66#增加字典
print(mydict)

mydict={"A":99,"B":88,"C":77}
element=mydict.pop("A")#从字典中删除并赋值给变量
print(f"删除为{element},剩余字典为{mydict}")

mydict={"A":99,"B":88,"C":77}
mydict.clear()#清空字典
print(mydict)

mydict={"A":99,"B":88,"C":77}
keys=mydict.keys()#取所有key
print(keys)

for key in keys:#1、通过获取全部key进行遍历
    print(key)
    print(mydict[key])

for key in mydict:#2、通过直接对字典for循环进行遍历
    print(key)
    print(mydict[key])

print(len(mydict))#统计字典内所有元素数量