#文件的读取操作
f=open("D:/编程/python文件/文件读取.txt","r",encoding="UTF-8")#open("文件路径"，"w/r/a",encoding="语言")，r表示只读打开文件；w表示写入文件覆盖原有内容，若没有则创建新文件；a表示在原有基础上添加，若不存在则添加新文件
#默认为"UTF-8"语言
print(type(f))
#文件对象.read(num),num表示需要读取的大小，若为填入num则读取全部内容
#文件对象.readlines(),以行的形式，通过列表将每一行作为一个元素输出
#print(f.read(10))#10个字节
#print(f.readlines())#不会重复读取前面已读取的内容

#文件对象.readline(),调用一次读取一行
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readline())

#for循环读取文件行
#for line in f:
#    print(line)

#程序关闭
#f.close()

#with open 语句
with open("D:/编程/python文件/文件读取.txt","r",encoding="UTF-8") as f:#读取结束自动关闭
    for line in f:
        print(line)