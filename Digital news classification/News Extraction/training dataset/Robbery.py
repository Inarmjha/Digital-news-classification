from google import search
from newspaper import Article
import urllib2
from bs4 import BeautifulSoup
import csv
from time import sleep
# to search
years=['2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004']
states=['Maharashtra','UttarPradesh','Gujarat','Westbengal','Punjab','Rajasthan','Karnataka','Bihar']
links = []
query = []
for state in states:
	for year in years:
			
		query.append('epidemic disease breakout in '+state+' in '+year)
#with open('out.csv', 'w') as out:
#	writer = csv.writer(out)
f = open('epidemicbreakout.txt','a')	    
#query="floods in bihar"
count=0
for q in query: 
	for j in search(q, tld="co.in", num=30, stop=1, pause=2):
         try:
         	thepage = urllib2.urlopen(j)
        	soup = BeautifulSoup(thepage, "lxml")
        	data=soup.title.text
        	count=count+1
    		print count,q
        	f.write('\n'+data)
    	 except urllib2.URLError as e:
    		print e
    	 except urllib2.HTTPError as err:
    	 	print err
    	 except:
    	    print "error"
    	 
    	     

# data = []
# count=0
# for url in links:
#     try:    
#         thepage = urllib.urlopen(url)
#         soup = BeautifulSoup(thepage, "lxml")
#         data=soup.title.text
#     	#writer.writerows(data)
#         #print()
#         print(data)
#         count=count+1
#         print count

#     except:
#         print('error')             	
      