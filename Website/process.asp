<%@LANGUAGE="VBSCRIPT"%> 
<%
set filesystemobject=Server.CreateObject("Scripting.FileSystemObject") 
set file=filesystemobject.OpenTextFile("G:\All Users\Documents\Dropbox\School\Summer Internship\Development\Website\emails.txt",8,true)

file.WriteLine(request.querystring ("email"))

file.Close 
set file=Nothing 
set filesystemobject=Nothing %>
                      