#http://stackoverflow.com/questions/23064549/get-date-and-time-when-photo-was-taken-from-exif-data-using-pil

import os
from PIL import Image
from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory

def get_date_taken(path):
	return Image.open(path)._getexif()[36867]
	
def split_timestamp(stamp):
	print(stamp)
	stamp_split = [str(item.strip()) for item in stamp.split(':')]
	day_hour_split = stamp_split[2].split(' ')
	day = day_hour_split[0]
	hour= day_hour_split[1]
	year = stamp_split[0]
	month = stamp_split[1]
	minute = stamp_split[3]
	second = stamp_split[4]
	if(len(day) < 2):
		day = "0" + day
	split_list = [year, month, day, hour, minute, second]
	return split_list
	
def is_timestamp_greater(stamp_one, stamp_two):
	time_one_list = split_timestamp(stamp_one)
	time_two_list = split_timestamp(stamp_two)
	for index, entry in enumerate(time_one_list):
		print entry
		print time_two_list[index]
		if entry > time_two_list[index]:
			print(entry + " is greater than " + time_two_list[index])
			return 1
		elif entry < time_two_list[index]:
			return 0

Tk().withdraw() 
print("Location to put email folders")
email_directory = askdirectory() # get location to put email folders
print("Location of emails.txt")
emailsfull = [line.rstrip('\n') for line in open(askopenfilename())] # emails and timestamps
emails = emailsfull[0::2]
times = emailsfull[1::2]
	
for index, address in enumerate(emails):
	subdirectory = os.path.join(email_directory, address)
	if not os.path.exists(subdirectory):
		os.makedirs(subdirectory)


iterate = 0
print("Images Directory")
images_directory = askdirectory()
for item in os.listdir(images_directory):
	print iterate
	itempath = os.path.join(images_directory, item)
	if os.path.isfile(itempath):
		if (is_timestamp_greater(get_date_taken(itempath), times[iterate]) == 1):
			print("Incrementing")
			iterate += 1
		outpath = os.path.join(email_directory, emails[iterate])
		outfile = os.path.join(outpath, item)
		if os.path.exists(outpath):
			print("Moving")
			os.rename(itempath, outfile)
			

		