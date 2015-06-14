<%@LANGUAGE="VBSCRIPT"%> 
<%
set filesystemobject=Server.CreateObject("Scripting.FileSystemObject") 
set file=filesystemobject.OpenTextFile("G:\All Users\Documents\Dropbox\School\Summer Internship\Development\Website\emails.txt",8,true)

file.WriteLine(request.querystring ("email"))

file.Close 
set file=Nothing 
set filesystemobject=Nothing %>

<header>    
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400italic,600italic,700italic,400,600,700' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Bitter:400,700' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome/font-awesome.css" rel="stylesheet">
    <link href="css/base.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
</header>

  <body>
    <div id="main">
      <div class="container">
        <section>
                    <h2>Thanks! Your model will be sent to you soon.</h2>
        </section>
	  </div>
    </div>
  </body>

<%
Response.AddHeader "REFRESH","3;URL=/index.html"
%>
                      