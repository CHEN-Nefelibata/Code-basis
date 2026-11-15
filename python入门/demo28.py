#元组的遍历
t1=(1,2,3,"hello",(1,2,3),4,5,6,'h')
index=0
while index<len(t1):#while循环遍历
    element=t1[index]
    print(element)
    index+=1

for element in t1:#for循环遍历
    print(element)