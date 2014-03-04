import os,datetime,string
import sys,csv,re

txtfile = open('data1-10.txt','r')
shoes = ['Heels','Sandals','Boots','Booties','Wedges','Flats','Pumps','Sneaker','Slipper']
dress = ['dress','Dress','Dresses','dresses','jumpsuit','jumpsuits','Skirts','rompers','romper']
x = 0
y = 0
z = 0
for line in txtfile:
		# print 'please wait...'
		arr = line.split('|')
		arr2 =  arr[1].split(' ')
		if(set(arr2).intersection(set(shoes))):
			print arr[0]+' is shoessss!'
			print list(set(arr2).intersection(set(shoes)))
			x = x + 1
		elif(set(arr2).intersection(set(dress))):
			print arr[0]+' is dresssss!'
			y = y + 1
		else:
			print arr[0]+' both not'
			z = z + 1

print str(x) + '-' + str(y)	+ '-' + str(z)	

		# print 'No.'+ str(arr[0]) +' is finish'