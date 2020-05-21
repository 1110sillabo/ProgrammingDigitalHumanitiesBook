# Overcommented for explanatory reasons
# Load the library that handles connecting to the internet
import requests
from bs4 import BeautifulSoup as bs

# Ask the user for the search
query = input('What do you want to search?')

# Search for our term with requests
searchreq = requests.get('https://www.google.com/search?q='+query)

# Ensure it works
searchreq.raise_for_status()

# Creating the Beautiful Soup object
soup = bs(searchreq.text, 'html.parser')

# Getting and printing results
results = soup.select('.r a') 
# Hopefully
print(results)
