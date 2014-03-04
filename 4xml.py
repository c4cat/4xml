from xml.dom import minidom 
import traceback 

import urllib
import os,datetime,string
import sys,csv,re

from bs4 import BeautifulSoup

def getLink():
	csvfile = file('red.csv','rb')
	reader = csv.reader(csvfile)
	theid = 10000
	for line in reader:
		print 'please wait...'
		getDate(theid,line[2],line[3])
		print 'No.'+ str(theid-10000) +' is finish'
		theid = theid + 1

    hebing('xml/','hebing.xml')
    hebing('csv/','hebing.csv')

def getDate(theid,link,buylink):
	soup = BeautifulSoup(urllib.urlopen(link))
	details = soup.find_all("div", "std")[0].string
	sell = soup.find_all("span", "value-title")[0].string
	try:
		sell = str(soup.find_all("span", "value-title")[0].string.replace(" ", "").lower())
	except:
		sell = str(soup.find_all("span", "value-title")[1].string.replace(" ", "").lower())

		
	# print sell	
	if(len(sell)<10):
		option = str(soup.fieldset.find_all("script"))
		reg = re.compile('(?<=label\":\").*?(?=\")',re.S)
		reg_price = re.compile('(?<=basePrice\":\").*?(?=\")',re.S)
		reg_oldprice = re.compile('(?<=oldPrice\":\").*?(?=\",\"pro)',re.S)
		groups = re.findall(reg,option)
		groups_price = re.findall(reg_price,option)
		groups_oldprice = re.findall(reg_oldprice,option)
		#----------------------------------------------------------
		price = groups_price[0]
		oldprice = groups_oldprice.pop()
		#arr_size
		del groups[0]
	else:
		price = ''
		oldprice = ''
		groups= []

	img = soup.find(id="image").get('src')
	title = soup.h1.string

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


def createCsv(theid,imgLink):
	filename='csv/'+str(theid)+'.csv'
	csvfile = file(filename,'w')
	write = csv.writer(csvfile)
	write.writerow(['post_id','post_type','post_thumbnail'])
	data=[(theid,'product',imgLink)]
	write.writerows(data)
	csvfile.close()

def hebing(fdir,outfile):
    file_list = os.listdir(fdir)
    file_to_write = file(outfile,'w')
    for f in file_list:
        file_to_read = file(fdir + str(f),'r')
        # file_to_write.write('\r\n <!------------')
        # file_to_write.write(str(f))
        # file_to_write.write('------------> \r\n')
        # file_to_write.write('\r\n')
         
        while True:
            line = file_to_read.readlines();
            line= ''.join(line[1:])
            #delete first line
            if len(line) == 0:
                break
            else:
                file_to_write.write(line)
        file_to_read.close()
     
    file_to_write.close()

def createItem(a_title,a_id,a_des,a_status,a_price,a_old_price,arr_size,a_buylink,sell):
	filename = 'xml/' + str(a_id) + '.xml'
	f = open(filename, "w") 
	
	doc = minidom.Document() 
	## item start
	item = doc.createElement("item") 
	doc.appendChild(item) 

	title = doc.createElement("title") 
	item.appendChild(title) 
	text = doc.createTextNode(a_title) 
	title.appendChild(text)
	link = doc.createElement("link") 
	item.appendChild(link) 
	#
	link_content = a_title.replace(' ','-')
	#
	text = doc.createTextNode(link_content) 
	link.appendChild(text)
	pubDate = doc.createElement("pubDate") 
	item.appendChild(pubDate) 
	text = doc.createTextNode("Thu, 16 Jan 2014 06:49:40 +0000") 
	pubDate.appendChild(text)
	creator = doc.createElement("dc:creator") 
	item.appendChild(creator) 
	text = doc.createTextNode("Thu, 16 Jan 2014 06:49:40 +0000") 
	creator.appendChild(text)
	guid = doc.createElement("guid")
	guid.setAttribute("isPermaLink", "false")  
	item.appendChild(guid) 
	text = doc.createTextNode("http://dress4club.com/?post_type=product&#038;p="+str(a_id)) 
	guid.appendChild(text)
	description = doc.createElement("description")
	item.appendChild(description) 
	text = doc.createTextNode("") 
	description.appendChild(text)
	content = doc.createElement("content:encoded")
	item.appendChild(content) 

	# cdata = doc.createCDATASection(a_des)
	text = doc.createTextNode(a_des)
	# content.appendChild(cdata)
	content.appendChild(text)

	post_id = doc.createElement("wp:post_id")
	item.appendChild(post_id) 
	text = doc.createTextNode(str(a_id)) 
	post_id.appendChild(text)
	post_date = doc.createElement("wp:post_date")
	item.appendChild(post_date) 
	text = doc.createTextNode("2014-01-12 14:40:25") 
	post_date.appendChild(text)
	status = doc.createElement("wp:status")
	item.appendChild(status) 
	text = doc.createTextNode("draft") 
	status.appendChild(text)
	post_name = doc.createElement("wp:post_name")
	item.appendChild(post_name) 
	text = doc.createTextNode(link_content) 
	post_name.appendChild(text)
	post_type = doc.createElement("wp:post_type")
	item.appendChild(post_type) 
	text = doc.createTextNode("product") 
	post_type.appendChild(text)
	category = doc.createElement("category")
	category.setAttribute("domain", "brand") 
	category.setAttribute("nicename", "ami-clubwear") 
	item.appendChild(category) 
	cdata = doc.createCDATASection('AMI Clubwear')
	category.appendChild(cdata)

	# category = doc.createElement("category")
	# category.setAttribute("domain", "collection") 
	# category.setAttribute("nicename", "glitz-glam") 
	# item.appendChild(category) 
	# cdata = doc.createCDATASection('Glitz &amp; Glam')
	# category.appendChild(cdata)

	for i in arr_size:
		category = doc.createElement("category")
		category.setAttribute("domain", "size") 
		category.setAttribute("nicename", i) 
		item.appendChild(category) 
		cdata = doc.createCDATASection(i)
		category.appendChild(cdata)

	#wp:postmeta
	#1 seo-title
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("seo-title")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection(a_title)
	meta_value.appendChild(cdata)
	#1.1
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("seo_sep")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection('default')
	meta_value.appendChild(cdata)
	#2 price
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("price")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	text = doc.createTextNode(a_price)
	meta_value.appendChild(text)
	#3 status
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("status")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection(sell)
	meta_value.appendChild(cdata)
	# sell out of stock
	if(len(sell)>9):
		postmeta = doc.createElement("wp:postmeta")
		item.appendChild(postmeta) 
		meta_key = doc.createElement("wp:meta_key")
		postmeta.appendChild(meta_key) 
		text = doc.createTextNode("out_of_stock")
		meta_key.appendChild(text)
		meta_value = doc.createElement("wp:meta_value")
		postmeta.appendChild(meta_value) 
		cdata = doc.createCDATASection('1')
		meta_value.appendChild(cdata)

	#4 seo_title
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("seo_title")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	text = doc.createTextNode(a_title)
	meta_value.appendChild(text)
	#4 reg price
	
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("regular_price")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	if(a_old_price == a_price):
		text = doc.createTextNode('')
	else:
		text = doc.createTextNode('a_old_price')	
	meta_value.appendChild(text)

	#4 tagline_term
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("tagline_term")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection('size')
	meta_value.appendChild(cdata)
	#4 buylink
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("buylink")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection(a_buylink)
	meta_value.appendChild(cdata)

	#4 imagesize
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("imagesize")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection('pic-default')
	meta_value.appendChild(cdata)
	#4 imagecrop_method
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("imagecrop_method")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection('1')
	meta_value.appendChild(cdata)
	#4 imagecrop
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("imagecrop")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection('c')
	meta_value.appendChild(cdata)
	#4 imagecrop
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("imagecrop")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection('c')
	meta_value.appendChild(cdata)
	#4 mark_as_new
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("mark_as_new")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection('off')
	meta_value.appendChild(cdata)
	#4 mark_as_onsale
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("mark_as_onsale")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	cdata = doc.createCDATASection('off')
	meta_value.appendChild(cdata)
	#5 in_stock text
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("instock_text")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	text = doc.createTextNode('In Stock')
	meta_value.appendChild(text)
	#out stock
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("sold_text")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	text = doc.createTextNode('Out of Stock')
	meta_value.appendChild(text)




	# print doc
	doc.writexml(f, "\t", "\t", "\n", "utf-8") 
	f.close() 
	#end create xml


 


getLink()


