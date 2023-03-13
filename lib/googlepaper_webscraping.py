import requests
from bs4 import BeautifulSoup

from datetime import datetime
import os,sys


query=sys.argv[1]

f = open('googlepaperscraping.txt', 'w', encoding = 'utf-8')

for page in range(0,20,10):
		raw = requests.get("https://scholar.google.com/scholar?start="+str(page)+"&q="+query+"&hl=ko&as_sdt=0,5", headers={'User-Agent':'Mozilla/5.0'})
		html = BeautifulSoup(raw.text, "html.parser")
		articles = html.select("div.gs_r")

		for num in range(0,10):
				article = articles[num].select_one("div.gs_ri")
				title = article.select_one("h3 > a").text
				link = article.select_one("h3 > a")['href']
				author = article.select_one("div").text
				content = article.select_one("div.gs_rs").text

				result = title + "\n" + author + "\n" + content + "\n" + link
				f.write(result + "\n\n")
