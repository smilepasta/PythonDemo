import requests
from bs4 import BeautifulSoup
content_url = "http://www.biquge.com.tw/4_4038/"
kv = {'user_agent': 'Mozilla/5.0'}  # 表示是一个浏览器
try:
    r = requests.get(content_url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    content_list = soup.find(id='list')
    chapter_list = soup.find_all('dd')
    for chapter in chapter_list:
        print(chapter.find('a').text)
except:
    pass