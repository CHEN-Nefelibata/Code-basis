#get方法请求的定制
#urlencode()方法的使用在多个参数的get请求中非常有用
#https://www.baidu.com/s?wd=周杰伦&sex=男
import urllib.request
import urllib.parse
base_url='https://www.baidu.com/s?'
data={
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国'
}
new_data=urllib.parse.urlencode(data)#将字典类型的数据转换为url编码的形式
url=base_url+new_data#将url编码后的数据拼接到url中
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0'
}
request=urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(request)
content=response.read().decode('UTF-8')
print(content)