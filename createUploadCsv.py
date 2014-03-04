import os
import sys,csv
     
def createCsv():
	txtfile = open('data/TBDress.txt','r')
	os.mkdir("csv") 
	for line in txtfile:
		arr = line.split('|')

		# filename='csv/'+str(arr[0])+'.csv'
		# csvfile = file(filename,'w')
		# write = csv.writer(csvfile)
		# write.writerow(['post_id','post_type','post_thumbnail'])
		# data=[(arr[0],'product',arr[6])]
		# write.writerows(data)
		# csvfile.close()
		#-------------------------------------------------------------------------
		img = os.path.basename(arr[6])
		img = 'http://dress4club.com/wp-content/uploads/2014/00/' + str(img)
		filename='csv/'+str(arr[0])+'.csv'
		csvfile = file(filename,'w')
		write = csv.writer(csvfile)
		write.writerow(['post_id','post_type','post_thumbnail'])
		data=[(arr[0],'product',img)]
		write.writerows(data)
		csvfile.close()
		#-------------------------------------------------------------------------

	if __name__ == '__main__':
    	 hebing('csv/') #fdir must end with '/'
    	 print 'all done!'

def hebing(fdir):
    file_list = os.listdir(fdir)
    start = str(file_list[0])[0:-4]
    end = str(file_list[-1])[0:-4]
    fn = start + '-' + end + '-upload' + '.csv'

    file_to_write = file(fn,'w')
    file_to_write.write('post_id,post_type,post_thumbnail')
    file_to_write.write('\r\n')
    for f in file_list:
        file_to_read = file(fdir + str(f),'r')
        
        while True:
            line = file_to_read.readlines();
            line= ''.join(line[1:])
            if len(line) == 0:
                break
            else:
                file_to_write.write(line)
        file_to_read.close()
     
    file_to_write.close()

createCsv()

