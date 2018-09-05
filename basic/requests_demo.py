import requests

r = requests.get('https://api.github.com/events')

print('url='+r.url+"\n")
print('txt='+r.text+"\n")