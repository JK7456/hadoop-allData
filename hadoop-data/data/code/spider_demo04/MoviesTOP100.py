import re
import requests
import pymysql
from requests.exceptions import RequestException

#1.请求一个单页内容拿到html
def get_one_page(url):
    try:
        #构建headers
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            #返回页面的内容
            return response.text
    except RequestException:
        return '请求异常'

#2.解析html（排名，影名，海报链接，主演，上映时间，评分）
def parse_one_page(html):
    #创建正则
    #使用re.S可以使 元字符.匹配到换行符
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                        +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    # print(items)
    #3.数据处理
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],#去前后空格 ，切片
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

#4.数据存储
def write_to_mysql(content):
    #建立mysql链接
    conn=pymysql.connect(host='localhost',user='root',passwd='root',db='movie',charset='utf8')
    cursor=conn.cursor()
    index=content['index']
    image=content['image']
    title=content['title']
    actor=content['actor']
    time=content['time']
    score=content['score']
    sql='insert into maoyan values (%s,%s,%s,%s,%s,%s)'
    parm=(index,image,title,actor,time,score)
    cursor.execute(sql,parm)
    conn.commit()
    cursor.close()
    conn.close()

# 5.函数回调
def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_mysql(item)
if __name__=='__main__':
    for i in range(0,10):
        main(i*10)