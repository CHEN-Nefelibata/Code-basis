#ajax的get请求
#获取豆瓣电影前十页数据并保存

#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'（第一页前20条）
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20'（第二页前20条）
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20'（第三页前20条）
#找到规律：start参数每次增加20
#start=(page-1)*20



#建立程序
import urllib.request
import urllib.parse
def create_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data={
        'start':(page-1)*20,
        'limit':20
    }
    data=urllib.parse.urlencode(data)
    url=base_url+data
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_response(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def download(page, content):
    with open('douban_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__=='__main__':
    start_page=int(input('请输入起始页码：'))
    end_page=int(input('请输入结束页码：'))
    for page in range(start_page,end_page+1):
        request=create_request(page)
        content=get_response(request)
        download(page, content)