#文件读取之单词计数#文件在D盘编程中
f=open("D:/编程/python文件/word.txt","r",encoding="UTF-8")
content=f.read()
count=content.count("itheima")
print(count)