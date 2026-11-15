#列表的遍历(取偶数)
mylist=[1,2,3,4,5,6,7,8,9,10]
#1、while循环遍历的写法
index=0
newlist=[]
while index<len(mylist):
    element=mylist[index]
    if element%2==0:
        newlist.append(element)
    index+=1
print(newlist)

#2、for循环遍历的写法
newlist=[]
for element in mylist:
    if element%2==0:
        newlist.append(element)
print(newlist)