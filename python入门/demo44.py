#开发可视化折线图
#1、JSON数据格式
#JSON是一种轻量级的数据交互格式，本质上是一个带有特定格式的字符串
#python转化多为多字典构成的列表和纯字典
import json#调用内置json模块
data1=[{"name1":"key1","age1":18},{"name2":"key2","age2":19},{"name3":"key3","age3":20}]
json_str1=json.dumps(data1)#从列表转化为字符串
print(type(json_str1))
print(json_str1)
data2={"name4":"key4","age4":21}
json_str2=json.dumps(data2)#从字典转化为字符串
print(type(json_str2))
print(json_str2)

str='[{"name5":"key5","age5":18},{"name6":"key6","age6":19},{"name7":"key7","age7":20}]'
restr=json.loads(str)#从字符串转变为列表
print(type(restr))
print(restr)

dictionary='{"name8":"key8","age8":21}'
redict=json.loads(dictionary)#从字符串转变为字典
print(type(redict))
print(dictionary)