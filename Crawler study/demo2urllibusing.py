#使用urllib获取百度首页的源码
import urllib.request

#1、定义一个url，即要访问的地址
url='http://www.baidu.com' 

#2、模拟浏览器向服务器发送访问请求
response=urllib.request.urlopen(url)

#3、获取响应中的页面的源码
content=response.read().decode('UTF-8')#read方法返回的是字节形式的二进制数据，我们要将二进制数据转为字符串--解码(decode);decode(编码的格式)

#4、打印数据
print(content)