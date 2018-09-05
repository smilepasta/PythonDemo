#coding:utf-8
import  requests
import threading
from bs4 import BeautifulSoup
import re
import os
import time
import sys
content_url = "http://www.biquge.com.tw/12_12603/"
kv = {'user_agent': 'Mozilla/5.0'}  # 表示是一个浏览器
try:
    r = requests.get(content_url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    article_name = soup.select('#wrapper .box_con #maininfo #info h1')[0].text
    # article_author = soup.select('#wrapper .box_con #maininfo #info p')[0].text
    article_intro = soup.select('#wrapper .box_con #maininfo #intro p')[0].text.strip()
    print('article name:'+article_name)
    # print('article author:'+article_author)
    print('article intro:'+article_intro)
    content_list = soup.find(id='list')
    chapter_list = soup.find_all('dd')
    fo = open(article_name+'.txt', "ab+")         
    fo.write((article_name+"\r\n").encode('UTF-8'))
    fo.write(("*******简介*******\r\n").encode('UTF-8'))
    fo.write(("\t"+article_intro + "\r\n").encode('UTF-8'))
    fo.write(("******************\r\n").encode('UTF-8'))
    count = 0
    while (count < len(chapter_list)):
    	print('this count is:'+str(count))
    	print(chapter_list[count].find('a').text)
    	zhangval = chapter_list[count].find('a')['href'].split('/')[2]
    	urlll = content_url+str(zhangval)
    	print('url:'+urlll)
    	res = requests.get(content_url+str(zhangval), headers=kv)
    	res.encoding = 'gb18030'
    	soups = BeautifulSoup(res.text,"html.parser")
    	section_text = soups.select('#wrapper .content_read .box_con #content')[0]
    	# mytxt = re.sub( '\s+', '\r\n\t', section_text.text).strip('\r\n')
    	fo.write(('\r'+chapter_list[count].find('a').text+'\r\n').encode('UTF-8'))
    	fo.write((section_text.text).encode('UTF-8'))
    	count = count + 1
    fo.close()
except:
	print('error')
