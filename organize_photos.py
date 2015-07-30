#http://stackoverflow.com/questions/23064549/get-date-and-time-when-photo-was-taken-from-exif-data-using-pil

import os
from PIL import Image
from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory

def get_date_taken(path):
	return Image.open(path)._getexif()[36867]

Tk().withdraw() 
directory = askdirectory() # get location to put email folders
emailsfull = [line.rstrip('\n') for line in open(askopenfilename())] # emails and timestamps
emails = emailsfull[0::2]
times = emailsfull[1::2]
	
stamps = {}
for index, address in enumerate(emails):
	stamps[address] = times[index]
	subdirectory = os.path.join(directory, address)
	if not os.path.exists(subdirectory):
		os.makedirs(subdirectory)
	
for address, time in stamps.iteritems():
	print address
	print time
	

	
	
	
	
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