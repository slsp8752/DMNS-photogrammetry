<%@LANGUAGE="VBSCRIPT"%> 
<%
set filesystemobject=Server.CreateObject("Scripting.FileSystemObject") 
set file=filesystemobject.OpenTextFile("\emails.txt",8,true)

file.WriteLine(request.querystring ("email"))

file.Close 
set file=Nothing 
set filesystemobject=Nothing %>


<%
Response.AddHeader "REFRESH","1;URL=/timestamp.html"
%>
                      