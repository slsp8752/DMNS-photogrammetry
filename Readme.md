# Photogrammetry Automation
#### This system organizes photos based on when they were taken and creates/distributes 3D models created with them.

##### About the Project
###### Context
This project was created as a part of CU-Boulder's Grand Challenge, a collaborative effort among educators, students, employees and the general public. The goal is to explore, understand, and influence how space-based science and technologies impact our daily lives, institutions and society. The Grand Challenge Event, where the project was presented, was hosted at the Denver Museum of Nature and Science.

###### Purpose
The purpose of the scripts is to allow for several users to take sets of pictures (one person at a time,) organize them by email address, and construct/distribute personalized 3D models using Agisoft PhotoScan. The scripts are not linked in any concrete manner, so using each portion of the system for other purposes would be relatively simple.

##### Usage
###### Website
The website portion was run locally through Microsoft WebMatrix for the purpose of this project, but there shouldn't be any issue actually hosting it online.

index.html has a form that accepts email address input, which is verified via HTML5's "email" form type. The page then calls process.asp

process.asp simply prints the email to a file named "emails.txt" and redirects to timestamp.html

timestamp.html then waits for the "-Next-" button is pressed, and then calls stamp.asp

stamp.asp writes the time the "-Next-" button was pressed to the emails.txt file, and then redirects to index.html

This is set up for organize_photos.py to sort the photos based on what timeframe they were taken within.

######organize_photos.py
Run organize_photos.py with *python organize_photos.py*
The program will prompt for three things in the following order:
1. The folder where you want to store the email-named folders that the program will create. Each email entered in the web form (listed in emails.txt) will get it's own folder inside the folder you specify. The folder you choose should be either **empty** or **a folder you've run the script with before.**
2. The location of emails.txt. This is the file created by the web form that contains the email adresses and the timestamps associated with them.
3. The folder containing the images you want to sort.

The script will then run and organize the photos into their respective folders.

######agisoft_automation.py
Run agisoft_automation.py by opening Agisoft PhotoScan (1.0 or later,) going to *Tools -> Run Script...* and locate *agisoft_automation.py*

The script then prompts for the folder containing the email named folders, which was specified in *prompt 1* of organize_photos.py

agisoft_automation will then run through the entire workflow and export a 3D model for each set of pictures to ezch of the respective email named folders.

###### email_automation.py
Run email_automation.py with *python email_automation.py*
**The email address automation must use a gmail email address as it is set up**

The script will prompt the following three things:
1. A valid gmail address and password
2. Again, the folder containing email named folders, specified in *prompt 1* of organize_photos.py
3. The location of emails.txt

As set up currently, email_automation.py will attach any pdf files in the email named folders, which should be exclusively the model produced by agisoft_automation.
