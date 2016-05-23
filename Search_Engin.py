from bs4 import BeautifulSoup, SoupStrainer
import urllib
import httplib2
import requests
import re
import json


def stripper(text):
    return text.lower().replace('\n',''
                      ).replace('\f',''
                      ).replace('\v',''
                      ).replace('\t',''
                      ).replace('\r',''
                      ).replace('&#39;', '\''
                      ).replace('</br>',' '
                      ).replace('<br/>',' '
                      ).replace('<b>',''
                      ).replace('</b>',''
                      ).replace('<br>',''
                      ).replace('<kw>',''
                      ).replace('</kw>',''
                      ).replace('<p>',''
                      ).replace('</p>',''
                      ).replace('?', ''
                      )

def googleSearch(query):
	encoded = urllib.quote(stripper(query))
	rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encoded).read()
	jsonData = json.loads(rawData)

	searchResults = jsonData['responseData']['results']
	for i in range(3):
		title= stripper(searchResults[i]['title'])
		link = searchResults[i]['url']
		content = stripper(unicode(searchResults[i]['content']))
		print "URL: "+link
		print "Short Description: "+content
		print '\n'

def bingSearch(query):
	encoded = urllib.quote(stripper(query))
	url = 'http://www.bing.com/search?format=rss&q='+encoded
	rawData = urllib.urlopen(url).read()
	res_links = []
	res_desc = []
	soup = BeautifulSoup(rawData)
	all_links = soup.find_all('link')
	all_contents = soup.find_all('description')

	for a in all_links:
		if a.parent.name == 'item':
			res_links.append(a.string)
	for b in all_contents:
		if b.parent.name == 'item':
			res_desc.append(b.string)

	for i in range(3):
		print "URL: "+ str(res_links[i])
		print "Short Description: "+res_desc[i]
		print '\n'

googleCount = 0
bingCount = 0





def choiceCheck(choice):
	global googleCount
	global bingCount
	if int(choice) == 1:
		googleCount = googleCount+1

	elif int(choice) == 2:
		bingCount = bingCount+1

	else:
		choiceCheck(raw_input("Please select the better result 1 or 2: "))



for i in range(3):
	print "==============================================================================================================================="
	print "In this program we apply double-blind testing method to evaluate the performance "
	print "of any two search engines (here, Google.com vs Ask.com)"
	print "You shall input any search query and our program will return the 3 top most results from"
	print "each of the engines. The search is blind, meaning that you won't know which engine produced the results."
	print "We ask you to pick which result is better every iteration. Based on your picks, we will decide which search engine is better."
	print "==============================================================================================================================="
	print "\n"
	print "Search Round ", i+1, '\n'
	query=raw_input("Enter a search query: ")
	print '\n'+"Blind Search"
	print "======================================================="
	googleSearch(query)
	print "Blind Search"
	print "======================================================="
	bingSearch(query)
	print '\n\n'
	choiceCheck(raw_input("Please select the better result:"+ "\n" + "(for the results at the top enter 1) (for the results at the bottom enter 2)"))

print "\n\n"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "Result: ", googleCount, " vs " , bingCount
if googleCount > bingCount:
	print "Google wins!"
else:
	print "Bing wins!"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"	