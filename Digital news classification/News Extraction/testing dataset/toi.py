from bs4 import BeautifulSoup
import urllib2
import re
from newspaper import Article
import csv
import articleDateExtractor
from geotext import GeoText
press=["https://www.ndtv.com/","http://www.news18.com/"]#"http://timesofindia.indiatimes.com/",
#press=["http://www.news18.com/"]
regexList = [r'www.news18.com/news',r'https://www.ndtv.com/']
count=0
for li in press:
	resp = urllib2.urlopen(li)
	soup = BeautifulSoup(resp,"html.parser")
	#count = 0
	news=list()
	for link in soup.find_all('a', href=True):
		#print link['href']
		news.append(link['href'])
		count=count+1
	print count
		#print news[0:50]
	flag=1
	for link in news[0:]:
		for regex in regexList:
			if(re.search(regex, link)):#|https://www.ndtv.com/	
				flag=0
		if(flag==0):
			news.remove(link)
print len(news)
#print news[0:50]
#if(re.search(r'timesofindia.indiatimes.com', news[4])):
#	print 'sandeep'
data=[]
with open('out.csv', 'w') as out:
	writer = csv.writer(out)
	for url in news[50:]:
		toi_article = Article(url, language="en") # en for English
		toi_article.download()
		toi_article.parse()
		titl=toi_article.title.encode('utf-8')
		txt=toi_article.text.encode('utf-8')
		d = articleDateExtractor.extractArticlePublishedDate(url)
		places = GeoText(txt)
		city=places.cities
		final = [titl, txt,d,city]
		writer.writerow(final)
		data.append(final)
		
# with open('out.csv', 'w') as out:
    # writer = csv.writer(out)
    # for e in data:
        # writer.writerow(e.split("-"))
