import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_2051608.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
lst = list()

# Retrieve <span> tags
tags = soup('span')
for tag in tags:
    lst.append(int(tag.contents[0]))

print(sum(lst))