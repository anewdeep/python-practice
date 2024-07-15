import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

url_list = list()

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Aiyanna.html'
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')
    url_list.append(tag[position - 1].get('href', None))
    url = tag[position - 1].get('href', None)

for url in url_list:
    print(url)
print('Last name in sequence:', re.findall('known_by_(\S+).html', url_list[-1])[0])