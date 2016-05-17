# ash-ishh.. <mr.akc@outlook.com>

import urllib.request
import re
import os

def checkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

## ## ## ## ## ## ## ## ## ## ## ##
def main():
    try:
        song = input('Song Name :\n>> ')
        artist = input('Artist Name :\n>> ')

        url="http://www.azlyrics.com/lyrics/{0}/{1}.html".format(artist.replace(' ','').lower(),song.replace(' ','').lower())

        req = urllib.request.urlopen(url)
        data = req.read() #full_webpage      
  
    except Exception as e:
        print("\n\n"+str(e))
        print("Try Again! !_!\n\n")
        main()

      
    song = song.title()
    artist = artist.title()
    base_path = "c:\\lyrix\\"
   
    checkdir(base_path+artist)
    lyrics = re.findall(r'Sorry about that. -->(.*)<form id="addsong"',str(data))
    lyrics = lyrics[0].encode('ascii','ignore').decode()
    lyrics_final = lyrics.replace('\\n','<br />').replace('\\r','').replace('\\','')
  

    file_location = (base_path+'{0}\\{1}.html').format(artist,song)
    with open(file_location,'w') as fo:

    #HTML tags in in file   
        fo.write('''
<html>
<style type="text/css">
body {
background-color:#000000;
color:#00FF00
}


</style>

<body>
'''    )


        head = "<h3> ** {0} - {1} ** </h3> <br /><hr />".format(artist,song)
        
        fo.write(head.upper())
        fo.write(lyrics_final)
        fo.write('''
</body>
</html>
'''
        )
 
    print("Done :) Check the lyrics Folder! ({0})".format(file_location))
    option = input("\nEnter 'Yo' to download another lyrics :\n>> ").lower()
    if option == 'yo':
        start()
    else:
        exit(0)

if __name__ == '__main__':
    print("Lyrix".center(40,'-'))
    main()
