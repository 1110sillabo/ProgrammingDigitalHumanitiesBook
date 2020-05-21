# Automation startup script

# Overcommented for extra explanational purposes

# Start with imports
import os
import webbrowser

# Construct your daily routine
WEBSITES = ['mail',
            'some other website',
            'telegram',
            ]

PROGRAMS = ['Rstudio',
            'word.exe',
            'somethingelse',
            ]
            
# Functions

def openwebpage(url):
    """Return a browser tab for a given url"""
    webbrowser.open_new_tab(url)

# Openprograms
def startprogram(path):
    """Open the path with a .exe program"""
    # We use raw strings (r') to avoid escaping
    # path characters
    pathlocation = r'path
    # os has a method to start a file ready for us
    os.startfile(pathlocation)

# Main automation function

def automationfunction():
    """Open all websites and programs in the routine"""
    for site in WEBSITES:
        openwebpage(site)
    for program in PROGRAMS:
        startprogram(program)

# Run the main function
automationfunction()
