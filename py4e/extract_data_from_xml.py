import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter url - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2051610.xml'

lst = list()

print('Retrieving', url)
xh = urllib.request.urlopen(url)
data = xh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
for item in counts:
    lst.append(int(item.text))

print(sum(lst))