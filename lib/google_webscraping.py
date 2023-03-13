import requests
from bs4 import BeautifulSoup
import sys


query=sys.argv[1]

f = open('googlescraping.txt', 'w', encoding = 'utf-8')

url_template = "https://www.google.com/search?q={query}&start={start}"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

results = []

for page in range(2):
		start = page * 10
		url = url_template.format(query=query, start=start)
		response = requests.get(url, headers=headers)
		soup = BeautifulSoup(response.content, "html.parser")

		results += soup.find_all("div", {"class": "g"})

for i, result in enumerate(results):
		link = result.find("a")["href"]
		title = result.find("h3").get_text()
		f.write(f"{i+1}. {title}: {link}\n")


