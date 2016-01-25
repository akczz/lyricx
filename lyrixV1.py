import urllib.request as ur
import re
import os
import time
from datetime import datetime
i = 1



def checkdir(a):
    if not os.path.exists(a):
        os.makedirs(a)

while True:
 try:
  artist = input('Enter artist name :  ')
  initial = artist[0]
  url = 'http://www.azlyrics.com/'+initial+'/'+artist+'.html'
  req = ur.urlopen(url)
  data = str(req.read())
  break
 except Exception as e:
  print(str(e)+'\nTry Again !_!')

startTime = datetime.now()
match = r'<a href="../lyrics/'+ artist
match1 =r'/(\w+).html"'
fmatch = match + match1
# fmatch = <a href="../lyrics/'+artist/(\w+).html"
# where \w = name of song

regex = re.findall(fmatch,data)

path = 'c:/lyrics/'+ artist
checkdir(path)


for song in regex:
 url0 ="http://www.azlyrics.com/lyrics/"+artist+"/"+song+".html"
 try:
  req0 = ur.urlopen(url0)
  data0 = str(req0.read()) #full_webpage
 except:
  data0 = "null"
 test = path + '/test.html'
 loc = path + '/' + song + '.html'
 path0 = open(test,'w')
 path0.write(data0)
 path0.close()
 
 path0 = open(test,'r')
 path1 = open(loc,'w')
 
 path1.write('''
<html>
<style type="text/css">
body {
background-color:#000000;
color:#00FF00
}


</style>

<body>
''')
 path1.close()
#^Html tags in song.html
 

 lyrics = re.findall(r'<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->(.{1,})<form id="addsong"',path0.read())
 
 try:
  lyrics = lyrics[0]
 except:
  lyrics ="null"
#Relacing \n \r  with new lines and '
 lyrics_newline = lyrics.replace("\\n","<br />")
 lyrics_slash = lyrics_newline.replace("\\","")
 lyrics_quote = lyrics_slash.replace("\\r","")
 lyrics_final = lyrics_quote.replace("xe2x80x99","'")


 path1 = open(loc,'a')
 head = "<h3> **"+song+" BY "+artist+"** </h3> <br /><hr />"
 head = head.upper()
 path1.write(head)
 path1.write(lyrics_final)
 path1.write('''
</body>
</html>
'''
)
 path1.close()
 path0.close()

 print('>> '+str(i)+" : "+str(song),"Done! ^_^")
 i += 1

 #If we will not use time interval azlyrics will detect us as robot block our ip for godmn week.

print("Over!")
print("TimeTaken: ",datetime.now()-startTime)
print("Check out location :",path)
