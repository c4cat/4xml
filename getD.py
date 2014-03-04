from xml.dom import minidom 
import traceback 

import urllib2,cookielib
import os,datetime,string
import sys,csv,re

from bs4 import BeautifulSoup

# def getData(theid,title,link,img,oldprice,nowprice,stock):
def getData(theid,title,link,img,oldprice,nowprice,stock):
	soup = BeautifulSoup(urllib2.urlopen(link))
	getSize = str(soup.find_all("select","size_select"))
	regGetSize = re.compile('(?<=\"\>).*?(?=\<)',re.S)
	arrSize = re.findall(regGetSize,getSize)
	del arrSize[0:2]
	print arrSize


	# createCsv(theid,img)
	print 'csv is ok!'
	try:
		# createItem(title,theid,details,'publish',price,oldprice,groups,buylink,sell)
		print groups
		print oldprice
		print sell
		print buylink
	except:
		print 'no.'+str(theid)+'is worng'




link='http://www.shareasale.com/m-pr.cfm?merchantID=49928&userID=905184&productID=525471991'

def getTrueUrl(url):
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
	opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322)')]
	f = opener.open(url)
	c = f.read()
	f.close()
	# print c
	reg = re.compile('(?<=replace\(\').*?(?=\'\))',re.S)
	c = re.findall(reg,c)[0]

	#get data
	getData('1','title',c,'img','oldprice','nowprice','in stock')

getTrueUrl(link)