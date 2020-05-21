# Import to have regex
import re

# We have links list from bs4
links = ['items', 'from', 'soup']

# We processed and split the query
query = ['terms', 'of', 'query', 'from', 'user']

# Scrape links for relevant terms
# Initialize a list of filtered results
filter = []
for link in set(links):
    for q in query:
        if re.search(q, link) is not None and link not in filter:
            link = link.replace('/url?q=', '')
            filter.append(link)

# Simple test
assert('from' in filter)
