import requests
from bs4 import BeautifulSoup

from datetime import datetime
import os,sys


query=sys.argv[1]

f = open('naverscraping.txt', 'w', encoding = 'utf-8')

for page in range(1,20,10):
		raw = requests.get("https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query="+str(query)+"&start="+str(page), headers={'User-Agent':'Mozilla/5.0'})
		html = BeautifulSoup(raw.text, "html.parser")
		articles = html.select("ul.list_news > li")	
		
		for num in range(0,10):
				title = articles[num].select_one("a.news_tit").text
				journal = articles[num].select_one("div.info_group > a.info").text
				time = articles[num].select_one("div.info_group > span.info:last-of-type").text
				
				result = journal + "\t" + title + "\t" + time
				f.write(result + "\n\n")

