#http://stackoverflow.com/questions/23064549/get-date-and-time-when-photo-was-taken-from-exif-data-using-pil

from PIL import Image
from tkFileDialog import askopenfilename

def get_date_taken(path):
	return Image.open(path)._getexif()[36867]

emailsfull = [line.rstrip('\n') for line in open(askopenfilename())] # emails and timestamps
emails = emailsfull[0::2]
times = emailsfull[1::2]
	
	

	
	
for index, address in enumerate(emails):
	print index
	print address
	#stamps[address] = times[index]
	#create a folder
	
	
	
	
# for each email, create a folder

# create a dictionary of emails and session end times?

# for each email
#    get session end timestamp
#    compare against each of the photos ***that haven't been sorted***
#    if images were taken before timestamp, store in email's folder
#    else, nothing
#    ***mark photos stored as sorted*** possibly by them being moved? 
#
#