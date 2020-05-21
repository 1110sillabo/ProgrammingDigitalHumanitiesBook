# Overcommented for explanatory reasons
# Load the library that handles connecting to the internet
import requests

# Ask the user for the search term 
query = input('What do you want to search?')

# Performing the search 
searchres = requests.get('https://www.google.com/search?q='+ query)
# Make sure the request works (check it)
searchres.raise_for_status() 
