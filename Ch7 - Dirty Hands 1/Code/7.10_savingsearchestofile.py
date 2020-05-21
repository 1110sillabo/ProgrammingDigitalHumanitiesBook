# Overcommented for explanatory reasons

# Imports - standard library first
import datetime # Needed to deal with time
import re  
import requests
from bs4 import BeautifulSoup as bs

# Ask the user for the search and process the query
userquery = input('Enter your query')
searchreq = requests.get('https://www.google.com/search?q='\
    + userquery)
searchreq.raise_for_status()

# Query  process
query = userquery.lower()
if len(query.split()) > 1:
    query = query.split()
    
# Soup objects and all links
soup = bs(searchreq.text, 'html.parser')
links = []
for a in soup.find_all('a', href=True):
    links.append(a['href'])
       
# Initialize results
results=[]

# Date processing - get today's date
today = str(datetime.datetime.now())

# Creating the file to save links
with open('Data_for_' + userquery +'.txt', 'a') as file:
    file.write('Results for \'' + userquery + \
    '\' performed on '+ today + ':\n')
    
    # Processing links
    for link in set(links):
        # Loop on queries
        # q is what we want to search on every item in the links
        for q in query:    
            if re.search(q, link) is not None and \
            re.search('google', link) is None \
            and re.search('search', link) is None \
            and link not in results:            
                link = link.replace('/url?q=', '')
                results.append(link)
                file.write(link + '\n')
    file.write('\n')
