#ver for txt file
# shoes-2022 dress-443 notBoth-658

from xml.dom import minidom 
import traceback 

import urllib2,cookielib
import os,datetime,string
import sys,csv,re

from bs4 import BeautifulSoup

def getLink():
	txtfile = open('Shoespie.txt','r')

	shoes = ['Heels','Heel','Sandals','Sandal','Boots','Boot','Booties','Bootie','Wedges','Wedge','Flats','Flat','Pumps','Pump','Sneaker','Sneakers','Slipper']
	dress = ['dress','Dress','Dresses','dresses','jumpsuit','jumpsuits','Skirts','Skirt','rompers','romper']
	intimates = ['Lingerie','Corsets','Corset','Hosiery','Undergarment','Leggings','Legging','Pantyhose','Tights','Tight','Stockings','Stocking','Tutus','Tutu','Panties','Pantie','Thong','Boyshorts','Boyshort','Bra','Garter','Belt','Chemise','Teddy','Babydolls','Babydoll','Camis','Cami','Variety Teddies'] 
	accessories = ['Cuff','Set','Handbagg','Cincher','Belt','Scarf','Body','Mask','Props','Pendant','Hairpin','Caps','Wig','Brooch','Bracelet','Backpack','Earrings','Eyelash','Fragrance','Clutches','Wallet','Hair','HEAD' 'BANDS','BAND','Handbag','Bag','Bags','Hat','Necklace','Ring','Scarves','Accessory','Sunglass','Sunglasses','Glasses','Watch','Watches','Gloves','Cosmetic']
	clothing = ['tee','Jeggings','Maxi','Costume','Top','SheerLace','Blouse','Overcoat','Vest','Zentai','Denim','Cardigan','Corset','Bustier','Cape','Coats','Jacket','Blazer','Jumpsuit','Base Layer','Jeans','Sleepwear','Hoodies','Hoody','Knit','Knitwear','Tank','Tee','Shirt','Pant','Pants','Coat','Shorts','Bottom','Dancewear','Bodysuit','Suit','Cropped','Costume','Romper','Clubwear','Rave','Sweater','Outerwear','Outfit','Trousers']
	swimsuits =['One-Piece','Two-Piece','Pucker','Back','Scrunch','Butt','Lace','swimwear','Animal','Print','Bling','Sequin','Fringe','Crochet','Flags','Patriotic','Push-Up','Padded','Bandeau','LBB','LBD','Bikinis','High-Waist','Bandeau']

	for line in txtfile:
		print 'please wait...'
		arr = line.split('|')
		# print arr[11]
		arr[1]= arr[1].replace('-',' ')
		arr2 =  arr[1].split(' ')
		if(set(arr2).intersection(set(shoes))):
			# the_type = list(set(arr2).intersection(set(shoes)))
			the_type = ['Shoes']
			arrSize = ['6','7','8']
			print arr[0]+' is shoessss!'
			getData(arr[0],arr[1],arr[4],arr[6],arr[7],arr[8],arr[18],the_type,arrSize,arr[11])
			print 'No.'+ str(arr[0]) +' is finish'
		elif(set(arr2).intersection(set(dress))):
			arrSize = ['S','M','L']
			# the_type = list(set(arr2).intersection(set(dress)))
			the_type = ['Dresses']
			print arr[0]+' is dresssss!'
			getData(arr[0],arr[1],arr[4],arr[6],arr[7],arr[8],arr[18],the_type,arrSize,arr[11])
			print 'No.'+ str(arr[0]) +' is finish'
		elif(set(arr2).intersection(set(intimates))):
			arrSize = ['S','M','L']
			# the_type = list(set(arr2).intersection(set(intimates)))
			the_type = ['Intimates']
			print arr[0]+' is intimates!'
			getData(arr[0],arr[1],arr[4],arr[6],arr[7],arr[8],arr[18],the_type,arrSize,arr[11])
			print 'No.'+ str(arr[0]) +' is finish'
		elif(set(arr2).intersection(set(accessories))):
			the_type = ['Accessories']
			arrSize = ['ONE-SIZE']
			# the_type = list(set(arr2).intersection(set(accessories)))
			getData(arr[0],arr[1],arr[4],arr[6],arr[7],arr[8],arr[18],the_type,arrSize,arr[11])
			print arr[0]+' is accessories!'	
		elif(set(arr2).intersection(set(clothing))):
			arrSize = ['S','M','L']
			# the_type = list(set(arr2).intersection(set(clothing)))
			the_type = ['Clothing']
			getData(arr[0],arr[1],arr[4],arr[6],arr[7],arr[8],arr[18],the_type,arrSize,arr[11])
			print arr[0]+' is clothing!'
		elif(set(arr2).intersection(set(swimsuits))):
			the_type = ['Swimsuits']
			arrSize = ['S','M','L']
			the_type = list(set(arr2).intersection(set(swimsuits)))
			getData(arr[0],arr[1],arr[4],arr[6],arr[7],arr[8],arr[18],the_type,arrSize,arr[11])
			print arr[0]+' is swimsuits!'			
		else:
			arrSize = []
			the_type = ['']
			print arr[0]+' both not'



def getData(theid,title,url,img,price,oldprice,stock,the_type,arrSize,details):
	# try:
	createCsv(theid,img)
	print 'csv done!'
	try:
		createItem(title,theid,price,oldprice,arrSize,url,stock,the_type,details)
		print 'xml done!'
	except:
		print 'no.'+str(theid)+' is worng!'
	# except:
		# print 'no.'+str(theid)+' is 404!' 		


def createCsv(theid,imgLink):
	filename='csv/'+str(theid)+'.csv'
	csvfile = file(filename,'w')
	write = csv.writer(csvfile)
	write.writerow(['post_id','post_type','post_thumbnail'])
	data=[(theid,'product',imgLink)]
	write.writerows(data)
	csvfile.close()

def createItem(a_title,a_id,a_price,a_old_price,arr_size,a_buylink,stock,a_type,a_details):
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
	text = doc.createTextNode('') 
	description.appendChild(text)
	content = doc.createElement("content:encoded")
	item.appendChild(content) 

	# cdata = doc.createCDATASection(a_details)
	text = doc.createTextNode(a_details)
	# content.appendChild(cdata)
	content.appendChild(text)

	post_id = doc.createElement("wp:post_id")
	item.appendChild(post_id) 
	text = doc.createTextNode(str(a_id)) 
	post_id.appendChild(text)
	post_date = doc.createElement("wp:post_date")
	item.appendChild(post_date) 
	text = doc.createTextNode("2014-03-2 14:40:25") 
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
	category.setAttribute("nicename", "Shoespie") 
	item.appendChild(category) 
	cdata = doc.createCDATASection('Shoespie')
	category.appendChild(cdata)

	# category = doc.createElement("category")
	# category.setAttribute("domain", "collection") 
	# category.setAttribute("nicename", "glitz-glam") 
	# item.appendChild(category) 
	# cdata = doc.createCDATASection('Glitz &amp; Glam')
	# category.appendChild(cdata)

	if (a_type):
		for i in a_type:
			category = doc.createElement("category")
			category.setAttribute("domain", "product_category") 
			category.setAttribute("nicename", str(i))
			item.appendChild(category) 
			cdata = doc.createCDATASection(str(i))
			category.appendChild(cdata)

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
	cdata = doc.createCDATASection(stock)
	meta_value.appendChild(cdata)
	# out of stock
	if(len(stock)>9):
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
		text = doc.createTextNode(a_old_price)	
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

	#4 buylink ver-cdata
	# postmeta = doc.createElement("wp:postmeta")
	# item.appendChild(postmeta) 
	# meta_key = doc.createElement("wp:meta_key")
	# postmeta.appendChild(meta_key) 
	# text = doc.createTextNode("buylink")
	# meta_key.appendChild(text)
	# meta_value = doc.createElement("wp:meta_value")
	# postmeta.appendChild(meta_value) 
	# cdata = doc.createCDATASection(a_buylink)
	# meta_value.appendChild(cdata)
#4 buylink ver-ctext
	postmeta = doc.createElement("wp:postmeta")
	item.appendChild(postmeta) 
	meta_key = doc.createElement("wp:meta_key")
	postmeta.appendChild(meta_key) 
	text = doc.createTextNode("buylink")
	meta_key.appendChild(text)
	meta_value = doc.createElement("wp:meta_value")
	postmeta.appendChild(meta_value) 
	text = doc.createTextNode(a_buylink)
	meta_value.appendChild(text)

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


