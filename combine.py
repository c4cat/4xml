import os
 
def hebing(fdir):
    file_list = os.listdir(fdir)
    start = str(file_list[0])[0:-4]
    end = str(file_list[-1])[0:-4]
    fn = start + '-' + end +'.csv'

    file_to_write = file(fn,'w')
    file_to_write.write('post_id,post_type,post_thumbnail')
    file_to_write.write('\r\n')
    for f in file_list:
        file_to_read = file(fdir + str(f),'r')
        # file_to_write.write('\r\n <!------------')
        # file_to_write.write(str(f))
        # file_to_write.write('------------> \r\n')
        # file_to_write.write('\r\n')

        
        while True:
            line = file_to_read.readlines();
            line= ''.join(line[1:])
            if len(line) == 0:
                break
            else:
                file_to_write.write(line)
        file_to_read.close()
     
    file_to_write.close()

def hebingXML(fdir):
    file_list = os.listdir(fdir)

    start = str(file_list[0])[0:-4]
    end = str(file_list[-1])[0:-4]
    fn = start + '-' + end +'.xml'

    file_to_write = file(fn,'w')
    file_to_write.write('<?xml version="1.0" encoding="UTF-8" ?>')
    file_to_write.write('\r\n')
    file_to_write.write('<rss version="2.0" xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:wp="http://wordpress.org/export/1.2/">')
    file_to_write.write('\r\n')
    file_to_write.write('<channel><title>Dress4Club</title><link>http://localhost/dress</link><description>Choose the best clubwear/sexy dresses in here !</description><pubDate>Mon, 27 Jan 2014 16:20:32 +0000</pubDate><language>en-US</language><wp:wxr_version>1.2</wp:wxr_version><wp:base_site_url>http://localhost/dress</wp:base_site_url><wp:base_blog_url>http://localhost/dress</wp:base_blog_url>')
    file_to_write.write('\r\n')
    file_to_write.write('<wp:author><wp:author_id>1</wp:author_id><wp:author_login>admin</wp:author_login><wp:author_email>highrising@163.com</wp:author_email><wp:author_display_name><![CDATA[dress4club]]></wp:author_display_name><wp:author_first_name><![CDATA[]]></wp:author_first_name><wp:author_last_name><![CDATA[]]></wp:author_last_name></wp:author>')
    file_to_write.write('\r\n')
    file_to_write.write('<generator>http://wordpress.org/?v=3.8.1</generator>')
    file_to_write.write('\r\n')
    for f in file_list:
        file_to_read = file(fdir + str(f),'r')
        file_to_write.write('\r\n <!------------')
        file_to_write.write(str(f))
        file_to_write.write('------------> \r\n')
        file_to_write.write('\r\n')

        
        while True:
            line = file_to_read.readlines();
            line= ''.join(line[1:])
            if len(line) == 0:
                break
            else:
                file_to_write.write(line)
        file_to_read.close()
    
    #wirte the end
    file_to_write.write('\r\n')
    file_to_write.write('</channel></rss>')
    file_to_write.write('\r\n')

    file_to_write.close()    
 
if __name__ == '__main__':
    hebing('csv/') #fdir must end with '/'
    hebingXML('xml/') #fdir must end with '/'
    print 'all done!'
