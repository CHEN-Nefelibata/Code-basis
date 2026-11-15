#post请求百度翻译
import urllib.request
import urllib.parse
import json
url="https://fanyi.baidu.com/sug"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0'
}
data={
    'kw':'spider'
}
#post请求的参数必须是bytes类型的数据，所以需要使用urlencode()方法将字典类型的数据转换为url编码的形式，然后再使用encode()方法将url编码后的数据转换为bytes类型的数据
data=urllib.parse.urlencode(data).encode('utf-8')
#post请求的参数不能直接拼接到url中，而是需要将参数放在Request对象的data参数中
request=urllib.request.Request(url=url,data=data,headers=headers)
#模拟浏览器向服务器发送请求


response=urllib.request.urlopen(request)
#获取响应内容
content=response.read().decode('utf-8')
content=json.loads(content)#将json格式的字符串转换为字典类型的数据
print(content)

#post请求的定制，参数放在Request对象的data参数中，不能直接拼接到url中