# Overcommented for explanatory reasons
# Load the library that handles connecting to the internet
import requests

# Ask the user for a search term 
query = input('What do you want to search?')

# Performing the search 
searchres = requests.get('https://www.google.com/search?q='+ query)
