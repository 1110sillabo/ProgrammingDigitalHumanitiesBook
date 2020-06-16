{#ch8}
# Scraping Bibliographies with Bibliographer

The program for this section is a more systematic implementation of the practice session of regex we had in chapter [5](#ch5) - Cory Doctorow was right after all, regex matters. This time we are going through the whole process: we start with a pdf paper, read it, extract the references, and end up with a .csv file with the needed references.

From there, you can go into whatever program you like and represent the references in a graph. Welcome data visualization!

Here we are going to work on:

- data extraction (references from papers);
- data conversion (from pdf to txt, from txt to csv);
- data cleaning (there will be a lot to fix from the pdf);
- regular expressions (many of them).

We are going to extract more data than we are going to use (for now), like *how many times a certain reference appears* in a paper.

## Bibliographer: Program Overview

*HumanDemia* wants you again. This time they need a program that reads a file (pdf files, you learn) and tries to extract bibliographic references from them. *Scopus* or other platforms are not enough: you cannot find everything there.

Humanities is full of standards or supposed standards for bibliographies.
Further, a lot of publications are not archived. You need to work on your corpus and extract the data from there.

Now that it is clear what we want our program to do, here are the main building elements we are going to cover:


- *get the input file from pdf to txt*: pdf is good for humans, bad for machines. We need to turn this into a txt, then the machine can read the txt and extract data from there;
- *cleaning the txt*: we need our txt to be cleaned such that we can process it with regexes;
- *regex processing*: we scan our text with a series of regex to get the data and process them to a standard output format. We use this format ('Author Year') to visualize a citation graph;
- *save the data*: self-explaining;
- *export the data in a visualization friendly mode*: we are going to handle the visualization over to other software or, at least, that's what *HumanDemia* requires us. We need to properly store our files as a CSV (comma separated values).

The areas we highlighted offer us a first idea of the main function of our program. One of the most problematic issues is that we have no guarantee the regexes are going to match everything we need. In fact, we know something about the formatting of the references, but that's not enough to be able to get everything: references are everywhere in the pages, titles can be arbitrarily long, etc. Still, it's worth trying it out.


### General Settings and Imports

There is quite a lot we need to import for the project, mostly to handle the pdf to txt transcription.

*Bibliographer imports*

```{python eval=FALSE, include=TRUE}

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

# Pandas and NumPy for visualization
import numpy as np
import pandas as pd
```


We are also using typing to insert some type annotation. Pandas is used to format the data and output them to CSV.

### From Pdf to Txt

Here we start reading the pdf and turning it into text we can use (txt). Pdfs are great for humans to read, but terrible for machines to operate on.

The code below is far from being optimal. It required me a lot of search, tries, and attempts. Most standard procedures did not work: I wasn't able to read the pdfs. So I have to resort to **pdfminer** (a module no longer maintained: https://github.com/euske/pdfminer) but that somehow got me where I need to.
In the process there were black boxes to trust.

Anyway, we start slicing the pdf name to keep only the file name and not the .pdf extension. We are going to save the text as Paper 2019.txt and not Paper 2019.pdf.txt.

The conversion happens as follows:

- we need an interpreter object - PDFInterpreter - that takes a manager object and a converter object. We import both from pdfminer: PDFResourceManager() and TextConverter();
- all the conversion process revolves around these three items: the *interpreter* (1) matches a *manager* (2) and a *converter* (3). We pass all the pages of the files we want to convert to the interpreter and get our result;
- the output we use is StringIO(), i.e. a buffer for input/output, https://docs.python.org/3.8/library/io.html?highlight=stringio#io.StringIO;
- we set the pagenums value to the empty set (i.e. set());
- the conversion starts when we open the *infile* by opening the pdf in read binary mode;
- we then start a for loop to get all the pages with the PDFPage.get_pages and then we call the interpreter on each page;
- we then close both files (infile and converter);
- all the information is in the output as a StringIO. We get the values from there, assign this content to filetxt, and close the output;
- now we have all the data we need and are ready to write it to txt...;
- ... well, we are not. Before our with-statement and a standard write to file, we need to *encode the stream tobyte*. The latin-1 encoding was the only one able to go through to pdfs I wanted to analyze, the same holds for the backslashreplace error. I had to experiment. Hopefully your corpus will be nicer than mine.

Are you ready? Here comes the code...

*Pdf goes txt*

```{python eval=FALSE, include=TRUE}

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
        
```

Ok, that was hard. I managed to retrieve the text only with Latin1 as encoding.
Usually you would expect a suboptimal start at your first level to propagate at a further level. The bad news? Programming follows the usual. We have to take care of Latin1 encoding next.^[If you are not satisfied with this extraction routine you can try building one based on PyPDF2, here's an overview of the module https://realpython.com/pdf-python/ then use the docs, and... ok, know you know it.]

### Cleaning the Txt

Somehow we managed to have our pdf turned into a txt. We can now read it but, before we do it, we need to *preprocess* it. Depending on what you want to do with a document, there a variety of operations to perform.

If you do some natural language processing, you will remove stop words (i.e. articles, propositions, etc.) that may clutter your analysis. Remember machines are dumb. If you count what is the most occurring world in a paper you don't want it to be 'the' but something more significant.

Of course, identifying stop-words is complex. What to do with 'no' and 'not'? Their input on meaning is quite important. Anyway, head over to SpaCy (https://spacy.io/) or NLTK (https://www.nltk.org/) to explore this more. Also, as far as pre-processing is concerned, you are likely to have all your words in lower case. Python is case sensitive and you don't want your word count to be messed by the fact that 'This is this' doesn't have two 'this' for your machine.

Here we have different concerns. Capitalization will be important to match the authors' surnames. It's one of the few elements we have to spot the references! Nonetheless, get ready for a lot of false-positive like June (2006), etc. Journals like to repeat the month of the current issue every other page! We do not recognize this as readers, but our machine reader spots this... further, we can't exclude authors named that way. Suppose you work on Japan in the media and have to deal with May (2020)...

To extract the references, we need to remove the newlines. You don't want a newline to break our regex. We also need due care with items that occur in the references formatting information: dots, coma, semi-colons, etc. Nasty spaces are to be avoided. This processing is going to make our hardly converted txt file very hard to be read for us, but pretty easy to be processed for our machine.

Still, even before we go there, we need to be sure that all characters of our text went through the pdf to txt journey. That is not going to be the case. Latin-1 fails with many characters. They appear as 'u25a0' and other strange characters. Before working on our hardly acquired data we have to check out for their integrity.
Search these codes and figure out what they mean. Then go heavy on the replace function.

Basically cleaning the txt is nothing but a with statement reading the file and then a lot of replace statements to insert back the code that was missing.

That's the (long) cleaning function I had to use. It is extra-long and super verbose, but at least it explains what it does. You may have used a dictionary with key and value pairs to specify the replacement operations. Then you have to loop on each pair.

Feel free to go that way.

*Cleaning the txt*

```{python eval=FALSE, include=TRUE}

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


```

To preprocess the txt all you need is to apply the cleaning function on the text. Note, again, that we are dividing the tasks: one function defines all the replacement, another calls the replacements to be applied.

(Here we keep track of what happened to a file by adding a specific name after it is processed. A preprocessed file is saved with the '_prep.txt' ending. In that way we know that we can retrieve the file name by slicing -9. You are invited to achieve the same results using the **endswith()** string method.)

Code-wise, we have what follows:

*Applying cleaning, i.e. preprocessing*

```{python eval=FALSE, include=TRUE}

def preprocess(txt: Text) -> Text:
    """
    Clean txt for regex processing using the
    cleantxt function. 
    """
    filename = txt[:-4]
    with open(filename +'_prep.txt', 'w') as preptxt:
        preptxt.write(cleantxt(txt))
    return cleantxt(txt)
```


### Regex Processing

Now that we have the text ready to be processed, it is regexes time.

We already know how this is going to work from chapter [5](#ch5). Nonetheless, here we are testing a *whole* paper on *different* regexes. If you have a small set of papers you can define further rules to optimize the regex for the different journals, but if you are working on a general purpose tool you can't rule out cases.

Different regexes are stored in the constant list REGEX_LIST. Feel free to uncomment some of them if you need to.

Another major difference is due to how we retrieve the information: we want to know which regex we are using to see the one that is bringing us the best results. We can keep track of this by printing with regex is giving us the results.

We further standardize all the results as Author Year, so watch out for capturing groups in the regexes. In that way, we can produce a CSV of 'Author Year', 'Author Year', which we can graph easily.

```{python eval=FALSE, include=TRUE}

REGEX_LIST = [#'\(([A-Z][a-z]*),?\s(\d\d\d\d)\D?\)',
             #'([A-Z]\S*),\s"[A-Za-z\s?,"]*\((\d\d\d\d)\)', 
              #'([A-Z]\S*),\s"?[A-Za-z\s?,\(]*(\d\d\d\d)\)', 
              #'([A-Z]\S*),\s"?[A-Za-z\s?,\(]*,\s(\d\d\d\d)\)',
              '([A-Z]\S*),\s\'?"?[A-Za-z\s?,:\(]*\'?\s\(?(\d\d\d\d)\)',
              '\(?([A-Z][a-z]*),?\s\(?(\d\d\d\d[a-f]?)',
              '[A-Z]\S*\s([A-Z]\S*),\s[^\(]*\s\([^\(]*(\d\d\d\d)\)',
              '[A-Z]\S*\s([A-Z]\S*),\s[^\(]*\s\([^\(]*\s\(?(\d\d\d\d)\)',
              '[A-Z]\S*\s([A-Z]\S*),\s[^\(]*\s\([^\(]*\([^\(]*(\d\d\d\d)',
              '[A-Z]\S*\s([A-Z]\S*),?\s[^\(]*\s\([^\(]*\([^\(]*(\d\d\d\d)',
              ]
    
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
    return extractedlist
        
```        

If you want to save the data you need to add a save-to-file part like the following or a dedicated save_bib() function, your choice.

```{python eval=FALSE, include=TRUE}

# Saving to file   
with open(filename + '_biblio.txt', 'w') as f:
    for item in sorted(extractedlist):
        f.write(item + '\n')

```

### Getting Data with Regexes

If you are using this tool you have to build you own regexes. A lot depends on the journals you explore. It is way better to use papers from one source. Even better if they use Author-Date and if the have a reference list at the end. Having a reference section will make it easier to check we extracted all the data and evaluate the performance of our regexes.

Choosing if and when to save to file is a difficult call. If you are working only on author-date you can do it as part of the extracting functions. Otherwise you may not want to save too early. Your regexes might be full of false-positive or missing cases. You may want to have a different file for each regex (you can use an identifier for the regex pattern in the file name, like "paperX_refs_regex1.txt" or similar).

You probably don't want to save data to txt if you are processing your text with 20 and more different regexes. Check the results against the reference list (if provided - join me in hating styles that don't do that). You can try to automate such a check.
In general: fulldata is hard, process it all and get more matches.

Sometimes you discover errors by the authors and issues with the journal instructions that were not respected (nor caught by the reviewers). That is cool. 

Note that there's more to the data we are extracting than what we are printing.
We get all the *occurrences* of a reference. This means we can check how many times they occur. We can attach a weight to the references. This is something worth considering.

Further, from the txt you can go further and extract named entities and create conceptual maps. These are more advanced features that require more machine time and some performance optimization. Again, NLTK and SpaCy are probably going to be your extraction tools.

### Exporting to CSV

Ok, we are almost there. I assume you manage to have a clean version of the data. Now it is time to export them to visualize them. We are actually buck-passing it Gephi (download and install it, you know the deal by now - actually beware of Gephi).
We need to have them in a CSV format and we are going to use pandas to achieve this.

Pandas is one of the main data analysis tool in Python. It gives us a new kind of object, dataframe (frames for short). You can think of a frame as an Excel table (on steroids).

Pandas is imported as **pd** by convention. And, also by convention, a dataframe is created as **df**.

We created our dataframe based on the references we extracted from the paper. To do that, we need to read our text file with the bibliography. We can do this with the **read_csv()** function of pandas. In fact, CSV are txt files with a specific separator.

While reading the references we specify our separator using the 'sep' parameter and we use the newline '\\n'. (In a standard CSV you are likely to have either, or ;). We then skip any header (if present) with 'header=None' and we start assigning the names to the columns of the frame.

Gephi needs a list of edges (paper - reference) and a weight indicator, in that order. We start importing the references and add paper and weight. Then we add the missing data and reorder the columns.

To access columns in the dataframe we use square bracket syntax. In this way we assign the weight value to 1 and the paper name takes the paperwithyear value we pass and capitalizes it.

Our function has no idea about who is the author of the paper we are processing. According to the structure of the program, the naming depends on the starting pdf. There's no one-catch-all solution to go from a file name to the author(s) of a paper. That's why we ask the user to input it.

The format we need is Author(space)year, i.e. one that matches the one we have in the references. *Be sure to capitalize it*, otherwise you risk to have a format like 'author(space)year' which is not going to match.

```{python eval=FALSE, include=TRUE}

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

```



### Helper Functions

Helper functions are there to make things easier for you and the users. 

Suppose you want to map a debate involving 10 papers and that you successfully obtained the data for all 10. You now have to join all these 10 CSV into a single file you are going to use in your visualization process.

That's perfect for a helper function like the following.

*Helper function joining CSVs*

```{python eval=FALSE, include=TRUE}

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
```

In this helper function we are using Pandas to create a frame and then export the frame to CSV (**frame.to_csv()**). As we did before.

The new function we called here is the **pd.concat** which allows us to concatenate the different CSVs of different papers into one.


Also, a real-life usage of the tool calls to have a way to actually read, preprocess, and extract the bibliographic data. Like that.

```{python eval=FALSE, include=TRUE}
def textprocess(txt):
    """
    (Helper function) Read, proprocess and extract references.
    """
    filename = txt[:-4]
    read(txt)
    preprocess(filename + '.txt')
    extractbiblio(filename + '_prep.txt')

```

### Tips for Graphing a Debate

I can't stress this enough, there are a lot of things that can go wrong while extracting the references and use them to produce a graph of a debate. This is a list of some of the things to watch out:

- different editions can give you two books when there's only one (except cases in which the different edition is quite a different book you can consider as a different one);
- classics being quoted as modern (Aristotle 1923);
- co-authored papers: they need specific regexes;
- a, b, c, etc. (Author 2000a, Author 2000b and the fact that they may change across different papers);
- authors having the same surname;
- tricky surnames (van Der Torre, von Fintel, etc.).

Some can be taken into account improving the program, others are harder.



## Summary

This chapter ends the *HumanDemia* training. We have a program and project that fits into a variety of different academic enterprises. We can (improve it and) use it to strengthen our research. Have fun!

### More Resources

Here are two projects that do similar things to the one we tried:

- https://www.rletters.net/ (this is in Ruby);
- https://www.bibliometrix.org/.

NLTK has a free book documenting the library. Academics should feel at ease there: http://www.nltk.org/book/. (Format is suboptimal and the printed version uses Python 2)

If you are interested in Natural Language Processing, *Text Analytics with Python
A Practitioner's Guide to Natural Language Processing* by Dipanjan Sarkar has a lot to offer to you.

### Further Work

Pdfminer is no longer maintained but there's pdfminer.six that is. It offers an extract text function: simplify the workflow by using it. https://pdfminersix.readthedocs.io/en/latest/api/highlevel.html#api-extract-text

Instead of Gephi we can visualize our graph with Python, for example using NetworkX (https://networkx.github.io/).