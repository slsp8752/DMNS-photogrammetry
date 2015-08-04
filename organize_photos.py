#http://stackoverflow.com/questions/23064549/get-date-and-time-when-photo-was-taken-from-exif-data-using-pil

import os
from PIL import Image
from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory

def get_date_taken(path):
	return Image.open(path)._getexif()[36867]
	
def split_timestamp(stamp):
	stamp_split = [str(item.strip()) for item in stamp.split(':')]
	day_hour_split = stamp_split[2].split(' ')
	day = day_hour_split[0]
	hour= day_hour_split[1]
	year = stamp_split[0]
	month = stamp_split[1]
	minute = stamp_split[3]
	second = stamp_split[4]
	split_list = [year, month, day, hour, minute, second]
	return split_list
	
def is_timestamp_greater(stamp_one, stamp_two):
	time_one_list = split_timestamp(stamp_one)
	time_two_list = split_timestamp(stamp_two)
	for index, entry in enumerate(time_one_list):
		print entry
		print time_two_list[index]
		if entry > time_two_list[index]:
			return 1

Tk().withdraw() 
print("Location to put email folders")
directory = askdirectory() # get location to put email folders
print("Location of emails.txt")
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
	
	
	# parse time
	# compare to every photo taken that hasn't been sorted (?)
	# 

	
	
	
	
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