import requests
from pyquery import PyQuery as pq
import time

def get_url(url):#请求页面
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    try:
        r=requests.get(url,headers=headers,timeout=10)
        r.encoding=r.apparent_encoding
        if r.status_code==200:#如果响应状态码等于200，表示成功
            return r.text
    except:
        print('请求时出现异常')

def one_parser(html):#解析页面
    doc=pq(html)#初始化
    result={}
    result['lp-name']=doc('h3 >span.items-name').text()
    result['adress']=doc('a.address >span.list-map').text()
    result['huxing']=doc('a.huxing >a.huxing').text().strip()#strip()去除左右两边的空字符串
    price=doc('p.price').text()
    result['price']=price
    result['tel']=doc('p.tel').text()
    print(result)
    return result

if __name__ == '__main__':
    MAX_PAGE=40#爬取安居客武汉二手房数据40页，因为没有使用selenium所以手动添加总页数
    url='https://wh.fang.anjuke.com/loupan/s?kw='
    html=get_url(url)#处理第一页的请求
    result=one_parser(html)#解析第一页
    print('开始执行下一页')
    for i in range(1,MAX_PAGE+1):
        url2='https://bj.fang.anjuke.com/loupan/all/'
        end_url=url2+str(i)+'/'#拼接url
        print(end_url)
        time.sleep(3)
        html2=get_url(url2)
        one_parser(html2)
        print('开始执行下一页')
    print('19页完成')
