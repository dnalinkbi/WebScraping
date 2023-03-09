#!/bin/bash

if [ $# -ne 2 ]
then
		echo -e "usage : ./WebScraping.sh searchEngine keyword"
		exit
fi

searchEngine=$1
searchEngine=${searchEngine,,}
word=$2

python3 lib/${searchEngine}_webscraping.py ${word}
python3 lib/sendemail.py ${searchEngine} ${word}

rm -rf *scraping.txt
