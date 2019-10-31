#handles encoding problems
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#import libraries

import csv
import re
import requests
from BeautifulSoup import BeautifulSoup

#url of the site
url = 'https://gov.texas.gov/Apps/Music/Directory/talent/all/region/austin/genre/all/p1'

#sends request for html content
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)  

#finds location in DOM, uses re to match a substring of the id
div = soup.findAll('div', id=re.compile("ContentPlace"))

list_of_rows = []
#finds each div
for i in div:
	list_of_cells = []
	#gets the heading
	for k in i.findAll('h2'):
		text = k.text
		list_of_cells.append(text)
	#gets the list items
	for j in i.findAll('li'):
		text = j.text
		list_of_cells.append(text)
	#appends to list of rows    
	list_of_rows.append(list_of_cells)
  
#appends to the file, rather than write a new one
outfile = open("./music.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
