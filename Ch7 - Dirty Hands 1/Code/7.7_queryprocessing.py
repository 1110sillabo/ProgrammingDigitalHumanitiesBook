# Overcommented for explanatory reasons
# Imports
import requests
from bs4 import BeautifulSoup as bs

# Asking for query annd building the request
userquery =  input('What do you want to search?')
searchreq = requests.get('https://www.google.com/search?q=' + \
    userquery)
searchreq.raise_for_status()

# Query processing: lowercase
query = userquery.lower()

# Query processing: splitting if it has more than 1 word
if len(query.split()) > 1:
    query = query.split()


