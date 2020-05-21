# Overcommented for explanatory reasons

import webbrowser

with open("urllist.txt") as file_with_urls:
    # Build a list of all the links and find length
    links = file_with_urls.readlines() 
    length = len(links) 
    
    # Ask how many pages to open 
    # remember int conversion
    views = int(input('How many links do you want \
    to open per batch?'))
    # Initialize counter to retrive links
    link_count = 0
    # Open the first link
    webbrowser.open(links[link_count])
    # Start iterate on the length of all the links
    while link_count in range(length):
    # Move to the next item
        link_count = link_count+ 1
        # Check if we reached the end of the file
        if link_count == length:
            print('You opened all the links')
            break
        webbrowser.open(links[link_count])       
        # Check if we have displaued all the items
        # in the view
        if (link_count+1)%(views) == 0:
            question = input('Do you want to see \
            the next ' + str(views) + ' results? \
            (y to get them, n to close)')
            if question == 'y':
                link_count = link_count + 1
                webbrowser.open(links[link_count])
            if question == 'n':
                break
