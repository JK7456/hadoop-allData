# http://www.runoob.com/python/python-100-examples.html
import urllib.request
from bs4 import BeautifulSoup

#1.拿到所有爬去的页面链接
def get_info_list(url):
    #(1)获取网页html
    html=urllib.request.urlopen(url).read()
    #(2)创建bs对象
    soup=BeautifulSoup(html,'lxml')
    #(3)遍历li得到里面详细页面的数据
    urls=soup.find(id='content').find_all('ul')
    for item1 in urls:
        lis=item1.find_all('li')
        for item2 in lis:
            As=item2.find_all('a')
            for item3 in As:
                #url重构
                yield 'http://www.runoob.com'+item3['href']


#2.获取详细页面的数据（标题，题目，程序分析）
def get_info_text(url_list):
    for item in url_list:
        #获取数据
        html=urllib.request.urlopen(item).read()
        #创建BS对象
        soup=BeautifulSoup(html,'lxml')
        content=soup.find(id='content')
        #如果获取到了id是content这个标签
        if content:
            # 找h1标签的文本
            title=content.find('h1').string
            # 找前三个p标签的文本
            content_list=content.find_all('p',limit=3)
            content=''
            # 往content_list追加数据
            for item in content_list:
                content+=item.get_text()
            yield (title,content)
        else:
            print(item)

#3.函数回调
url='http://www.runoob.com/python/python-100-examples.html'
urls=get_info_list(url)

content_list=get_info_text(urls)
# for i in content_list:
#     print(i)
#4.存储
#写入文本文件
# 用with体自动关闭文件
with open('python100例.txt','w',encoding='utf-8') as f:
    #循环写入标题，题目信息
    for title,content in content_list:
        f.write(title+'\n')
        f.write(content+'\n')
        f.write('*'*100+'\n')