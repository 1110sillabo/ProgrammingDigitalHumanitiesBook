# Overcommented for explanatory reasons
# Load the library that handles connecting to the internet
import requests
from bs4 import BeautifulSoup as bs

# Ask the user for a the search term 
query = input('What do you want to search?')

# Performing the search 
searchres = requests.get('https://www.google.com/search?q='+ query)
# Make sure the request works (check it)
searchres.raise_for_status() 

# Create a beautifulsoup object (soup, by convention)
soup = bs(searchres.text, 'html.parser')

# Extract what we need
extraction = soup.select('[insert relevant tag]')
