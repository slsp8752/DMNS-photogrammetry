<%@LANGUAGE="VBSCRIPT"%> 
<%
set filesystemobject=Server.CreateObject("Scripting.FileSystemObject") 
set file=filesystemobject.OpenTextFile(Server.MapPath("emails.txt"),8,true)

file.WriteLine("Testing")

file.Close 
set file=Nothing 
set filesystemobject=Nothing %>


<%
Response.AddHeader "REFRESH","1;URL=/index.html"
%>
                      