<%@LANGUAGE="VBSCRIPT"%> 
<%
set filesystemobject=Server.CreateObject("Scripting.FileSystemObject") 
set file=filesystemobject.OpenTextFile(Server.MapPath("emails.txt"),8,true)

time24 = FormatDateTime(now(),vbshorttime)

secs = Second(now())
theTime = time24 & ":" & secs

file.WriteLine(Year(now()) & ":" & Right("0" & Month(now()),2) & ":" & Day(now()) & " " & theTime)

file.Close 
set file=Nothing 
set filesystemobject=Nothing %>


<%
Response.AddHeader "REFRESH","1;URL=/index.html"
%>
                      