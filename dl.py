#!/usr/bin/env python3
import re
import urllib
from bs4 import BeautifulSoup
     
html = urllib.urlopen('http://r-a-d.io/api')
soup = BeautifulSoup(html)
data = soup.findAll(text=True)
     
def visible(element):
	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		return False
	elif re.match('<!--.*-->', str(element.encode('utf-8'))):
		return False
	return True
     
result = filter(visible, data)
     
print (visible_texts)