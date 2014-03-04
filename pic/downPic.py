import os,urllib,csv

class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0"

def getLink():

	csvFile = file('data-csv-1.csv','r')
	csvFile = csv.reader(csvFile)

	for line in csvFile:
		if(line):
			print line[2]

			urllib._urlopener = AppURLopener()
			filename = os.path.basename(line[2])
			urllib.urlretrieve(line[2] , filename)
			
			print 'ok'

	print 'done'

getLink()