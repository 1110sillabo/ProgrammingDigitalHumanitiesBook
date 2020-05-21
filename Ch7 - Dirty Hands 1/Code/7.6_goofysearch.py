# Overcommented for explanatory reasons

# Imports
import requests
from bs4 import BeautifulSoup as bs

# Searchrequest and soup
searchreq = requests.get('https://www.google.com/search?q=Goofy')
searchreq.raise_for_status()
soup = bs(searchreq.text, 'html.parser')

# Getting links as a href
links = []
for a in soup.find_all('a', href=True):
    print(a['href'])
    links.append(a['href'])
