import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://247wallst.com/media/2017/01/24/americas-100-largest-newspapers/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('div', attrs={'class': 'entry-content'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        list_of_cells.append(text.encode('utf-8'))
    list_of_rows.append(list_of_cells)

outfile = open("./newspapers.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)