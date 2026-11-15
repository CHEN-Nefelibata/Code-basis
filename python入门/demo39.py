#文件的写入操作
#文件不存在时的写入
#f=open("D:/编程/python文件/文件写入.txt","w",encoding="UTF-8")
#f.write("Hello World!!!")#只写入为存入
#f.flush()#保存至硬盘中
#f.close()
#覆盖
#f=open("D:/编程/python文件/文件写入.txt","w",encoding="UTF-8")
#f.write("itheima")#覆盖原有内容
#追加
f=open("D:/编程/python文件/文件写入.txt","a")
f.write("\tHello World!!")
f.flush()
f.close()