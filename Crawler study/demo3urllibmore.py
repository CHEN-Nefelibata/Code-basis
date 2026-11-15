#urllib的一个类型和六个基本方法
import urllib.request
url='http://www.baidu.com'
#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(url)

#类型HTTPResponse
#print(type(response))

#按照一个字节去读
#content=response.read()#返回n个字节在()+n
#print(content)

#按照行读取
#content=response.readline()#只能读取1行
#print(content)

#按行全部读取
#content=response.readlines()
#print(content)

#返回状态码,如果值为200，则证明逻辑无误
#print(response.getcode())

#返回url地址
#print(response.geturl())

#返回获取到状态信息
#print(response.getheaders())