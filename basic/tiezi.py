__author__ = 'baluw'
import urllib
import urllib.request
import re


class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr=re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine=re.compile('<tr>|<div>|</div>|</p>')
    # 将制表符<td>换成\n
    replaceTD=re.compile('<td>')
    # 将段落开头换为\n加空两格
    replacePara=re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR=re.compile('<br><br>|<br>')
    # 将其余标签剔除
    rmExtraTag=re.compile('<.*?>')

    def replace(self,x):
        x=re.sub(self.removeImg,"",x)
        x=re.sub(self.removeAddr,"",x)
        x=re.sub(self.replaceLine,"\n",x)
        x=re.sub(self.replaceTD,"\t",x)
        x=re.sub(self.replacePara,"\n",x)
        x=re.sub(self.replaceBR,"\n",x)
        x=re.sub(self.rmExtraTag,"",x)
        # strip()将前后内容删除
        return x.strip()

class TBSpider:
    # 初始化,传入基地地址,是否只看楼主得参数
    def __init__(self, baseUrl, seeLZ,floorTag):
        self.user_agent = 'Mozilla/4.0(compatible:MSIE 5.5;Windows NT)'
        #初始化headers
        self.headers = {'User-Agent': self.user_agent}
        self.baseURL = baseUrl
        self.seeLZ = "?see_lz=" + str(seeLZ)
        # 初始化Tool工具
        self.tool=Tool()
        self.file=None
        self.floor=1
        self.defaultTitle="百度贴吧"
        self.floorTag=floorTag

    #传入页码,获取该页面帖子的代码
    def getPage(self, pageNum) -> object:
        try:
            url = self.baseURL + self.seeLZ + "&pn=" + str(pageNum)
            request = urllib.request.Request(url, headers=self.headers)
            reqonse = urllib.request.urlopen(request)
            content = reqonse.read().decode("utf-8")
            return content
        except urllib.error.URLError as e:
            if hasattr(e, "reason"):
                print("连接百度贴吧失败,错误原因:", e.reason)
                return None

    #获取帖子标题
    def getTitle(self,page):
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    #提取帖子页数
    def getPageNum(self,page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getConetent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        # 楼层
        contents=[]
        self.floor=1
        for item in items:
            content="\n"+self.tool.replace(item)+"\n"
            #contents.append(content.encode('utf-8'))就是这句出问题了,整了一个小时,终于排查出错误了
            contents.append(content)
        return contents


    def setFileTitle(self,title):
        if title is not None:
            self.file=open(title+".txt","w+")
        else:
            self.file=open(self.defaultTitle+".txt","w+")

    def writeData(self,contents):
        for item in contents:
            if self.floorTag=='1':
                floorLine="\n-------------"+str(self.floor)+"楼--------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor+=1

    def start(self):
        indexPage=self.getPage(1)
        pageNum=self.getPageNum(indexPage)

        title=self.getTitle(indexPage)
        self.setFileTitle(title)

        if pageNum==None:
            print("URL链接已经失效,请重试")
            return
        try:
            print("该帖子共有{0}页".format(str(pageNum)))
            for i in range(1,int(pageNum)):
                print("正在写入第{0}页数据".format(str(i)))
                page=self.getPage(1)
                contents=self.getConetent(page)
                self.writeData(contents)
        except IOError as e:
            print("写入异常原因:",e.reason)
        finally:
            print("写入任务完成!")

#--------程序入口---------
print("""
------------------------------------
   程序：百度贴吧爬虫
   版本：1.0
   作者：{0}
   日期：2015-04-19
   语言：Python 3.4
   功能：百度贴吧里的内容,分段现实
------------------------------------
""".format(__author__))
print("请输入帖子代号")
baseURL = 'http://tieba.baidu.com/p/' + str(input('http://tieba.baidu.com/p/'))
seeLZ = input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag = input("是否写入楼层信息，是输入1，否输入0\n")
bdtb = TBSpider(baseURL,seeLZ,floorTag)
bdtb.start()