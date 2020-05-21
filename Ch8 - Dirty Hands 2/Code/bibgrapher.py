# Overcommented for explanatory reasons

import re 
import os

# Type annotations
from typing import IO, Text

# Reading pdf
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# Pandas and numpy for visualization
import numpy as np
import pandas as pd
def read(pdf: IO) -> Text:
    """Acquire a pdf and return a text file"""
    pdfname = pdf [:-4]
    # Setting the conversion trio
    pagenums = set()
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    
    # Opening the pdf
    infile = open(pdf, 'rb')
    
    # Readiing loop: get the page and use the interpreter
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    # Get the values and turn them to byte
    content = output.getvalue()
    output.close()
    # Specify encoding
    tobyte = content.encode(encoding="latin-1",\
        errors="backslashreplace")
    # Coping to txt, finally!
    with open(pdfname + '.txt', 'wb') as txt_file:
        txt_file.write(tobyte)


def cleantxt(filetxt: Text) -> Text:
    """
    Fix all the latin-1 badly imported chars.
    Remove extra newlines
    Ensure there's always a space after the dot
    Adjust bad inputs, such as:
        a. Ò is "
        b. Ó is "
        c. Õ is '
        d. Ð is -
        e. Ñ is -- (longdash)
    Fix spacing the *
    Fix space after )
    Fix space after ]
    """
    with open(filetxt) as f:
        ftxt = f.read()  
        ftxt=ftxt.replace('\\u25a0', ' * ') # Black dot 
        ftxt=ftxt.replace('\\u2013', '-')
        ftxt=ftxt.replace('\\u2014', '-')
        ftxt=ftxt.replace('\\u2019', '\'')
        ftxt=ftxt.replace('\\u2018', '\'')
        ftxt=ftxt.replace('\\u201c', '\'')
        ftxt=ftxt.replace('\\u201d', '\'')
        ftxt=ftxt.replace('\\ufb01', 'fi')
        ftxt=ftxt.replace('\\ufb02', 'fl')
        ftxt=ftxt.replace('\\u0152', 'oe')
        ftxt=ftxt.replace('\\u0153', 'oe')
        ftxt=ftxt.replace('\\u2022', '-') # Point
        ftxt=ftxt.replace('\\u27a4', '->') # Right arrow
        ftxt=ftxt.replace('\\u27a5', '->') # Right curved arrow
        ftxt=ftxt.replace('\\u2122', '')  # TM logo
        ftxt=ftxt.replace('\\u20ac', 'euro')  
        ftxt=ftxt.replace('\\u221e', 'infinity')  # Infinity
        ftxt=ftxt.replace('\x0c', '') # Up arrow
        ftxt=ftxt.replace('VC ', '') # Copyright
        
        # Umlaut related
        ftxt=ftxt.replace('\\u20aca', 'a')
        ftxt=ftxt.replace('\\u20aco', 'o')
        ftxt=ftxt.replace('\\u20acu', 'u')
        ftxt=ftxt.replace('\\u2026', '...')
        # Slavic
        ftxt=ftxt.replace('\\u017', 'z')
        ftxt=ftxt.replace('\\u0161', 's')
        ftxt=ftxt.replace('\\u0106', 'C')
        
        ftxt=ftxt.replace("\.", "\. ") 
        ftxt=ftxt.replace("Ò", "\"") 
        ftxt=ftxt.replace("Ó", "\"") 
        ftxt=ftxt.replace("Õ", "\'") 
        ftxt=ftxt.replace("Ð", "-")
        ftxt=ftxt.replace("Ñ", "--")
        
        # Ad hoc cleaning given my corpusx
        ftxt=ftxt.replace(" eg, ", "") # Messes up fulldata
        ftxt=ftxt.replace(" Ltd 2004", "") # Bad input 
        ftxt=ftxt.replace(" Malden 0214", "") # Bad input 
        
        # Spacing
        ftxt=ftxt.replace("\n", " ") # Newlines to space
        ftxt=ftxt.replace("*", "") # Clean *
        ftxt=ftxt.replace(")", ") ") # Space after )
        ftxt=ftxt.replace("]", "] ") # Space after ]
        ftxt=ftxt.replace(" ;", ";") # No space after ;
        ftxt=ftxt.replace(" ,", ",") # No space after ,
        ftxt=ftxt.replace(" .", ".") # No space after .
        ftxt=ftxt.replace("  ", " ") # 2 spaces into 1
        return ftxt

def preprocess(txt: Text) -> Text:
    """
    Clean txt for regex processing using the
    cleantxt function. 
    """
    filename = txt[:-4]
    with open(filename +'_prep.txt', 'w') as preptxt:
        preptxt.write(cleantxt(txt))
    return cleantxt(txt)


def extractbiblio(txt: Text) -> Text:
    """
    Apply regex patterns in REGEX_LIST to a 
    (processed) text. References are stored in 
    'Author Year' format.
    """
    # Initialize the list containing the extracted refs
    extractedlist = []
    filename = txt[:-9] # The file passes ended with "_prep.txt"
    for regex in REGEX_LIST:
        print('Processing ', regex)
        # Open the paper as corpus
        corpus = open(txt).read()
        # Run regexes over corpus
        matches =  re.findall(regex, corpus)
        # Save matches in the extracted list
        for match in matches:
        # We using capturing groups for author and date
            extractedlist.append(str(match[0]) \
            + ' ' + str(match[1]))    
        # Print statement to have an idea of the search
        # feel free to comment it out
        print(sorted(set(extractedlist)), len(set(extractedlist)))
    
    # Saving to file   
    with open(filename + '_biblio.txt', 'w') as f:
        for citatation in extractedlist:
            f.write(citation + '\n')
    return extractedlist
        

def extract_to_gephi(biblio: Text, papernamewithyear) -> Text:
    """
    Format the data for usage in gephi. The gephi table has:
    - a 'paper' column: the paper we exteracted references from;
    - a 'references' column: the outcome of our biblio extraction;
    - a 'weight' column: Gephi needs it set to 1.    
    
    The parameters are:
        -biblio: a txt file with the extract biblio (_biblio.txt 
        is the output name of the extractbiblio(txt) function);
        - papernamewith year: the paper we are extracting the 
        references from given the format we are using of 'Author 
        year' you have to insert it this way. Otherwise your Gephi
        network will not display there references to the paper
        you are processing.
    """
    references = pd.read_csv(biblio, sep='\n', header=None,\
        names = ['references', 'paper', 'weight'])    
    df = pd.DataFrame(references)
    # Be sure to capitalize the paper or your data won't match
    # author 2020 and Author 2020 are different
    df['paper'] = papernamewithyear.capitalize()
    df['weight'] = 1
    columns_titles = ["paper","references", "weight"]
    df=df.reindex(columns=columns_titles)
    df.to_csv(papernamewithyear + '.csv', index = False)
    print('Done')


def join_csv():
    """
    Helper function to join the results of various csv.
    """
    # Initialize csv container
    csv = []
    # Get all csv
    for item in os.listdir():
        if item.endswith('.csv'):
            csv.append(item)
    # Comprehension to come
    frame = pd.concat((pd.read_csv(item) for item in csv))
    # We skipped the index of csv after the first
    frame.to_csv('joinedfiles.csv', index = False)
    print('Done!')

def textprocess(txt):
    """
    (Helper function) Read, proprocess and extract references.
    """
    filename = txt[:-4]
    read(txt)
    preprocess(filename + '.txt')
    extractbiblio(filename + '_prep.txt')
