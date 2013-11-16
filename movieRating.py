#http://www.imdb.com/title/tt0114369/
#<div class="titlePageSprite star-box-giga-star"> 8.7 </div>

import sys
import urllib2
import re
import StringIO

#IMDB
urlIMDB = "http://www.imdb.com/title/tt0114369/"
response = urllib2.urlopen(urlIMDB)
content = StringIO.StringIO(response.read())

for line in content:
	if "titlePageSprite star-box-giga-star" in line:
		result = line.split()
		print "IMDB: " + result[3]


#Rotten Tomatoes
urlRT = "http://www.rottentomatoes.com/m/seven" #+ sys.argv[1]
response = urllib2.urlopen(urlRT)
content = StringIO.StringIO(response.read())
 
for line in content:
	if "meter certified numeric" in line:
		result = line.split()
                print "RT: " + result[3]
