import urllib.request
import json

lst = list()
url = input('Enter url- ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2051611.json'

print('Retrieving', url)
jh = urllib.request.urlopen(url)
data = jh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
for item in info['comments']:
    lst.append(item['count'])

print(sum(lst))