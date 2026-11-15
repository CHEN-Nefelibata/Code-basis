import urllib.request
url='https://www.baidu.com'
#url的组成
#协议             主机           端口号
#http/https  www.baidu.com      80/443

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0'
}

#请求对象的定制，UA反爬
#因为urlopen中不能存储字典，所以headers不能传入
request=urllib.request.Request(url=url,headers=headers)#参数顺序问题，不能直接写，中间还有date，需要关键字传参

response=urllib.request.urlopen(request)
content=response.read().decode('UTF-8')
print(content)