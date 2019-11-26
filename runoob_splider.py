import requests;
from pyquery import PyQuery as pq;
import re;

indexUrl="https://www.runoob.com/manual/pythontutorial3/docs/html/index.html";
header={
    "cookie":"_ga=GA1.2.1752118345.1556243636;gads=Test; Hm_lvt_3eec0b7da6548cf07db3bc477ea905ee=1573780500,1574757294,1574757384,1574760387; Hm_lpvt_3eec0b7da6548cf07db3bc477ea905ee=1574760387",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
};

#根据url获取地址
def requestUrl(url):
    response=requests.get(url=url,headers=header);
    return response;

#获取跳转连接
def getALink(response):
    list=set();

    doc=pq(response.text);
    links=doc('a').items();
    regnex='(href=.*html)"';
    for item in links:
        result = re.search(regnex,str(item));
        if(None != result):
            midResult=result.group(0);
            midResult=re.sub("href=\"",'',midResult);
            midResult=re.sub("\"",'',midResult);
            list.add(midResult);
    return list;

#循环下载网页
def downloadHtml(list):
    bfUlr="https://www.runoob.com/manual/pythontutorial3/docs/html/";
    count=0;
    for midLink in list:
        url = bfUlr+midLink;
        with open(str(count)+'.html','w',encoding='utf-8') as f:
            content=requestUrl(url).content;
            content=content.decode('UTF8');
            #print(content);
            f.write(content);
        f.close();
        count = count + 1;



def main():
    response=requestUrl(indexUrl);
    lists=getALink(response);
    downloadHtml(lists);

main();
