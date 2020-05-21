# Overcommented for explanatory reasons

# Import to have regex
import re
import requests
from bs4 import BeautifulSoup as bs

# Searchrequest and soup
searchreq = requests.get('https://www.google.com/search?q=Goofy')
searchreq.raise_for_status()
soup = bs(searchreq.text, 'html.parser')

# Getting links as a href
links = []
for a in soup.find_all('a', href=True):
    links.append(a['href'])

# Initialize the noise list
noise = []    
# Definition of the filter function
def filter_noise_from_links(links):
    # List of expressions to detect noise
    noise_detection = ['/search\?rlz', '/search\?ie=utf',
    '/search\?q=', '/policies\.google\.com/',
    'www\.google\.com/policies']
    # Checking detectors on links
    for link in set(links):
        for noise_item in noise_detection:        
            test = re.search(noise_item, link)
            if test is not None:
                print(test)
                noise.append(link)
    return list(set(links)-set(noise))

filter_noise_from_links(links)
