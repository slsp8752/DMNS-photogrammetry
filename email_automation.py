import smtplib
import os
import getpass
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory

COMMASPACE = ', '

# Credentials

username = raw_input('Email: ')
password = getpass.getpass()

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Email Testing 2'
msg['To'] = ''
msg['From'] = username

body = 'Thank you for visiting our exhibit. Attached below is a pdf file containing your 3D model. For best results, open with Adobe Acrobat Reader.'

from_addr = msg['From']

Tk().withdraw() 
directory = askdirectory() # show an "Open" dialog box and return the path to the selected file

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(username,password)

# Loop through all the email addresses and send out their respective files
emailsfull = [line.rstrip('\n') for line in open(askopenfilename())] # emails and timestamps
emails = emailsfull[0::2]
for address in emails:
	for folder in os.listdir(directory):
		if address == folder:
			msg.set_payload(None)
			subdirectory = os.path.join(directory, folder)
			msg.replace_header('To', address)
			
			for filename in os.listdir(subdirectory):
				if filename.endswith('.pdf'):
					path = os.path.join(subdirectory, filename)
					fp = open(path, 'rb')
					msg.attach(MIMEText(body, 'plain'))

					pdf = MIMEBase('application', 'pdf')
					pdf.set_payload(fp.read())
					encoders.encode_base64(pdf)
					pdf.add_header('Content-Disposition', 'attachment', filename=filename)				
					msg.attach(pdf)
					
			s.sendmail(from_addr, msg['To'], msg.as_string())
			
			print "sent message to: "
			print msg['To']

			

s.quit()
