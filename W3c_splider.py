#下载W3c的教程
import requests;
from pyquery import PyQuery as pq;

index_url='https://www.w3school.com.cn/python/index.asp';
header={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
#网站的基础目录
baseUrl= 'https://www.w3school.com.cn';

#获取返回结果
def getResponse(url):
    response=requests.get(url=url,headers=header);
    return response.text;

#获取跳转链接
def getLinkUrl(indexHtml):
    get_css(indexHtml);
    links=[];
    doc=pq(indexHtml);
    elements=doc('#course');
    a=elements.find('a');
    lis = doc(a).items();
    for mid in lis:
        links.append(mid.attr('href'));
    return links;

#提取css文件
def get_css(html):
    doc = pq(html);
    cssLink = doc('head link');
    links=cssLink.items();
    hrefs=[];
    for midLink in links:
        href=doc(midLink).attr('href');
        hrefs.append(href);
    cssUrl=hrefs[0];
    cssUrl = baseUrl+cssUrl;
    cssFile=getResponse(cssUrl);
    downLoadHtml(cssFile,'c5','css');

#爬取指定url的页面
def getLinksHtml(urls):
    count=1;
    for midUrl in urls:
        url = baseUrl + midUrl;
        response=getResponse(url);
        downLoadHtml(response,str(count),'html');
        count=count+1;

#写文件
def downLoadHtml(content,filename,type):
    f=open('C:\\Users\\iao\\Desktop\\w3c\\'+filename+'.'+type,'w',encoding='utf-8');
    f.write(content);
    f.close();
    print("下载完成："+filename);

def main():
    html=getResponse(index_url);
    links = getLinkUrl(html);
    getLinksHtml(links);

main();
