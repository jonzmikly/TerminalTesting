#handles encoding problems
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#import libraries
import time
import csv
import re
import requests
from BeautifulSoup import BeautifulSoup

#url of the site
site = 'https://gov.texas.gov/Apps/Music/Directory/talent/all/region/austin/genre/all/p'

#opens the file with a new write command
outfile = open("./music_austin.csv", "wb")

#loops through numbers in range for url suffix
#up to but not including so add one additional to the stop in range
for num in range(1,106):
    num = str(num)
    url = site + num
    
    #sends request for html content
    time.sleep(2)
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)  
    
    #finds location in DOM to repeat
    div = soup.findAll('div', id=re.compile("ContentPlace"))

    list_of_rows = []
    #finds each div
    for i in div:
        list_of_cells = []
        #gets the heading
        for k in i.findAll('h2'):
            text = k.text
            list_of_cells.append(text)
        #gets the list items including the link
        for j in i.findAll('li'):
            text = j.text

            #if the element contains a link
            if j.a:
                url = (i.a['href'])
                list_of_cells.append(url)
            else:
                list_of_cells.append(text)
                    
        #appends to list of rows    
        list_of_rows.append(list_of_cells)
      
    #appends to the file, rather than write a new one
    outfile = open("./music_austin.csv", "ab")
    writer = csv.writer(outfile)
    writer.writerows(list_of_rows)

