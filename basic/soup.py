from bs4 import BeautifulSoup
import bs4

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...<p>我是最亮的子孙结点</p></p>
"""

soup = BeautifulSoup(html,"html.parser")

#获取标签
# print(soup.title)
#获取标签中的文字
# print(soup.title.string)
#判断标签中的文字是不是注释，如果是注释，就显示
# if type(soup.a.string)==bs4.element.Comment:
	# print(soup.a.string)

#遍历所有直接子结点
# for child in soup.body.children:
    # print(child)

#递归遍历所有子孙结点
# for child in soup.descendants:
	# print(child)

