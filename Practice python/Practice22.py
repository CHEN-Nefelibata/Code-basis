#文件操作综合
f=open("D:/编程/python文件/文件综合.txt","r",encoding="UTF-8")#打开文件
k=open("D:/编程/python文件/文件综合2.txt","w",encoding="UTF-8")#准备写出文件
for line in f:
    line=line.strip()
    if line.split(",")[4]=="测试":
        continue#跳过
    k.write(line)
    k.write("\n")
f.close()
k.close()