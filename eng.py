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

reload(sys) 
sys.setdefaultencoding('utf-8')

def writeToDeskTop(jsonArr,z):
    print "第"+str(z)+ "个文件"
    f = file("/Users/LY/Desktop/english/eng"+str(z)+".json","w+")
    strArr = json.dumps(jsonArr, ensure_ascii=False)
    f.writelines(strArr)
    f.close()

jsonArr = []

def catchContent(url,i):
	try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request,timeout=60)
            soup = BeautifulSoup(response.read())
            engResult = soup.select('td > strong')
            chineseResult = soup.find_all('td',class_='span10')
            newArr = zip(engResult,chineseResult)
            for eng,chinese in newArr:
                chineseStr = chinese.string
                engStr = eng.string
                dict = { 'eng': engStr, 'chinese': chineseStr}
                jsonArr.append(dict)

	except urllib2.URLError, e:
	    if hasattr(e,"code"):
	        print e.code
	    if hasattr(e,"reason"):
	        print e.reason




def getOutUrl():
    url = 'https://www.shanbay.com/wordbook/104215/'
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response.read())
        z = 1
        for a in soup.select('td > a'):
            newUrl = 'https://www.shanbay.com' + str(a['href'])
            for i in range(1,11):
                finalUrl = newUrl +'?page=' + str(i)
                catchContent(finalUrl,i)
            writeToDeskTop(jsonArr,z)
            z = z + 1
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

getOutUrl()
