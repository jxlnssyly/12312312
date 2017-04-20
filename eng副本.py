# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import thread
import time
import sys
from bs4 import BeautifulSoup
import sys
import json



jsonArr = []

def catchContent(page):
	url = 'https://www.shanbay.com/wordlist/104215/206779/'+'?page=' + str(page)
	try:
	    request = urllib2.Request(url)
	    response = urllib2.urlopen(request)
	    soup = BeautifulSoup(response.read())
	    engResult = soup.select('td > strong')
	    chineseResult = soup.find_all('td',class_='span10')
	    newArr = zip(engResult,chineseResult)
	    for eng,chinese in newArr:
	    	chineseStr = chinese.string
	    	engStr = eng.string
	    	dict = { 'eng': engStr, 'chinese': chineseStr}
	    	jsonArr.append(json.dumps(dict, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4))
	except urllib2.URLError, e:
	    if hasattr(e,"code"):
	        print e.code
	    if hasattr(e,"reason"):
	        print e.reason

for i in range(1,11):
	catchContent(i)
f=file("/Users/user/Desktop/eng6.json","w+")
strArr = json.dumps(jsonArr, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
f.writelines(strArr.encode('utf8'))

f.close()
