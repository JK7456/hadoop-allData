# https://tieba.baidu.com/p/5815297430
import re
import urllib.request

#1.发送请求，获取html
def getHtmlContent(url):
    page=urllib.request.urlopen(url)
    return page.read().decode('utf-8')
#2.从html中解析出图片url
def getJPGS(html):
    #创建正则
    jpgReg=re.compile('<img class="BDE_Image".*?src="(.*?\.jpg)".*?>')
    jpgs=re.findall(jpgReg,html)
    return jpgs

#3.用图片url保存成文件名
def downloadJpgs(imgurl,filename):
    urllib.request.urlretrieve(imgurl,filename)

#4.批量下载图片，保存在当前目录文件夹下
def batchDownloadJPGs(imgUrls,path='./杨幂/'):
    # 用于给图片命名
    count=1
    for url in imgUrls:
        downloadJpgs(url,''.join([path,'{0}.jpg']).format((count)))
        print('下载完成第{}张图片'.format(count))
        count=count+1

#5.函数回调
def download(url):
    html=getHtmlContent(url)
    jpgs=getJPGS(html)
    batchDownloadJPGs(jpgs)

#定义主函数
def main():
    # url='https://tieba.baidu.com/p/5815297430'
    url='http://tieba.baidu.com/p/5814412543'
    download(url)

if __name__=='__main__':
    main()




