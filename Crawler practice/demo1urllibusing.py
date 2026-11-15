import urllib.request
url='http://www.luogu.com.cn'
response=urllib.request.urlopen(url)
content=response.read().decode('UTF-8')
print(content)