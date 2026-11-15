#列表的遍历(有需求的从列表中取出若干元素)
mylist=[1,2,3,"python",[1,2,3],"a"]
def mylist_while_func():#以while循环为基础的遍历函数可随意改动循环条件
    index=0
    while index<len(mylist):#小于mylist长度
        element=mylist[index]
        print(element)
        index+=1

mylist_while_func()#调用

def mylist_for_func():#以for循环为基础的遍历函数只能进行简单的排列
    for element in mylist:
        print(element)

mylist_for_func()