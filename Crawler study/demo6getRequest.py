#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
#get请求的编解码
#将周杰伦变为Unicode编码的形式，需要依赖urllib.parse
import urllib.request
import urllib.parse

url='https://www.baidu.com/s?wd='#因为只识别ASCLL码，所以会报错

#请求对象的定制作为解决反爬的手段
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0'
}

name=urllib.parse.quote("周杰伦")
url=url+name#将周杰伦变为Unicode编码形式

#请求对象定制
request=urllib.request.Request(url=url,headers=headers)

#模拟服务器向浏览器发送请求
response=urllib.request.urlopen(request)

#获取响应的内容
content=response.read().decode('UTF-8')

#打印数据
print(content)