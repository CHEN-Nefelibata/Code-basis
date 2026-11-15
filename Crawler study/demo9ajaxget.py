#ajax的get请求
#获取豆瓣电影第一页数据并保存
import urllib.request
url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0'
}

#请求对象定制
request=urllib.request.Request(url=url,headers=headers)
#发送请求
response=urllib.request.urlopen(request)
content=response.read().decode('UTF-8')
#将获取到的json数据保存到本地
fp=open('douban.json','w',encoding='UTF-8')
fp.write(content)
fp.close()