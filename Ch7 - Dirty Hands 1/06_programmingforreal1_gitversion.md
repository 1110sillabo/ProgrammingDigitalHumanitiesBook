# StartUp Optimization, Corpora Builder and Corpora Opener {#ch7}

It is time to start building something that has tangible results.

We already had a taste of practicalities for Humanities exploring regexes and we know how to expand and improve our Python knowledge.

As at *HumandDemia* (and, also, as researchers in general) we are still thinking in terms of time and efforts (we are into programming when we could be reading and thinking and wasting time pretending we are doing "research" while we are browsing social media or failing at properly replying emails) there are some fun facts about the programs we are going to make.

A lot of these programs are less than 300 lines of code long. When printed, they are shorter than a 3 pages hand out.

"Oh," you think "at *HumanDemia* they went lightweight on marketing. They could have said something like *some super cool and useful scripts are shorter than 500 words, i.e. a (mostly useless) abstract of any paper we have to write*. It's good they don't have *me* as their marketing ops chief."

Here is what we are going to build. The list ranges from  utility tools to entire programs:

- a startup optimization tool that will open your main programs;
- a tool to retrieve and open links from a search engine;
- a tool to extract bibliographic data from papers.

Module-wise, we are going to use mainly the following tools from the standard library:

- the **webbrowser** module (to handle browser opening);
- the **re** module to perform regular expressions.

We are also going to need some tools outside the standard library (i.e. that you'll have to **conda install**, possibly in virtual environments):

- the **requests** module: to handle downloading and processing data from the web;
- **pandas**: to manage data table (pandas is included with Anaconda distribution of Python)
- **tqdm**: to add progress bars;
- **BeautifulSoup** to do some parsing on the webpages.

On the way to build all that you'll be pointed out to other tools and resources that will help you to:

- build a timer;
- build games (pong, Tetris, snake);


Well, enjoy your building.

## Startup Optimization: The Challenge

The days start in similar ways. Chances are there's a moment in time we flash our pc and we go through a kind of routine: emails, browsing, opening various software, etc. Why waste time opening the same stuff every day?

Luckily a simple script can do that for us and save us some clicks. We only have two steps to cover:

1. write the automation script;
2. schedule its daily execution.

### Automation Script: A Description

Each person is different and each day is different. Spend some time thinking about your main *HumanDemia* activities, identify a pattern, and code it.

I assume that the tasks you have to do are the following:

- open specific programs;
- open specific webpages.

After that, the real work starts.

The script will work like that:

1. we import os module to manage paths and open files;
2. we import webbrowser to handle browsing operations;
3. we define a list of our websites;
4. we define a list of the programs we need to open;
5. we define a function that opens a webpage in a new tab;
6. we define a function that opens the program;
7. we define an automation functions that does the following:
  
  - iterate through the list of webpages and open them;
  - iterate through the list of programs and open them.

Easy, right?

An implementation of the script is below. Notice that we have to pass path variables for opening the programs. You will need to find where the .exe files are on your machine. Be sure to pass raw strings to that variable, so that you don't run risks of escaping characters.

**Be sure to enter your relevant websites and programs before running the file**

*Startup optimization code - ch. 7.1*

```{python eval=FALSE, include=TRUE}

# Overcommented for extra explanation purposes
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

#openprograms
def startprogram(path):
    """Open the path with a .exe program"""
    # We use raw strings (r') to avoid escaping
    # path characters
    pathlocation = r'path
    # os has a method to start a file ready for us
    os.startfile(pathlocation)

```

```{python eval=FALSE, include=TRUE}
# Main automation function

def automationfunction():
    """Open all websites and programs in the routine"""
    for site in WEBSITES:
        openwebpage(site)
    for program in PROGRAMS:
        startprogram(program)

# Run the main function
automationfunction()
```

The program starts out importing the relevant modules (os and webbrowser). They are part of the standard library, so there's no need to worry about them.

We then define the pieces of our daily routine: websites we need to open and program we need to run. **Feel your list instead of the placeholders**. Websites are pretty easy to be opened, we'll pass them to webbrowser and use the webbrowser.open_new_tab() function. (I assume you want your sites opened in different tab rather than in N different windows. Feel free to look at the docs to learn how to open them to multiple windows.)

Yes, this is the first time we see it and it sounds mysterious. So we check out the docs: https://docs.python.org/3.8/library/webbrowser.html.

Programs are slightly more complex. Our pc doesn't know how to click on an icon. So we need to feed python the **.exe** file of the program we need to run. Basically we need to:

1. know the name of the file that runs the program;
2. figure out the path of the file.

(The first seems obvious but it can be tricky, e.g. if you want to run the SQL database SQlite, which is included into Python).

Once you find the program open the folder in a new window. You can right-click on the path and click the copy path option. Now this is the path you have to paste in the PROGRAMS list (be sure to include the .exe file: you need a path and a file).

We then define a function that opens the webpages (using webbrowser) and one opening the programs. For this function we convert the path inserted in the PROGRAMS list to a raw string (**r'**) to avoid escaping all the slashes in the path.

All we need is to define an automation function that iterates through the two lists of tasks.


### Scheduling the Task

Ok, we have the program. Test it and be sure everything goes as intended.
Our program actually opens all we need, still, it is not able to run every time we fire our workstation. (Bonus points for writing tests for that. The testing goat book has a routine to check that the page opened is the right one.)

To schedule this automation - at least in Windows - we need to call the Task Scheduler. (Look here if you have troubles finding it: https://www.isunshare.com/windows-10/4-ways-to-open-task-scheduler-on-windows-10.html). Then we need to create your activity that runs our program. Suppose we save it as **automationscript.py**.

Creating the task is intuitive except for the action part. In fact, you have to set *three* different parameters, two of which are optional.

1. when asked about which program or script to run type in the path to your python.exe;
2. the first optional field (argument) is the name of the program you want python to run, i.e. how you named the script;
3. the last parameter (second optional field - called start or something similar) is the path to the folder you stored the program into.

To recap, here's what these parameters are for our script:

1. the python.exe path, something like "C:\\Users\\AppData\\Local\\Programs\\Python\\Python37";
2. .py script (here automationscript.py);
3. path for the .py script (i.e. where you saved it), something like "C:\\Users\\Desktop\\PythonDigitalHumanities\\".

Nice, isn't it?

### Extend It

We said tutorials are only a first step and should prompt you to do more. So here are a few extra ideas.

First general consideration. As it is now, you get the same setup every time the program runs, that is every time you fire your pc. Weekends included. Wouldn't it be nice to set the script to work only on workdays?

There should be some condition checking, maybe an if statement. You check what's the day in the week and then you fire your setup 5 days out of 7. So, the flow control is easy. Now you need to interact with time objects. That's more tricky, you'll need to find a way to deal with it and then read the docs. A first way to go through time objects in Python is the **datetime** module, which will keep you inside the standard library.

- What if you are reading or studying something that requires your pc to access the material? Think about extending the program to open a pdf at a specific page.
- To make it really hard, think about ways to track your progress of the day: either add a while loop that asks you the page you reached at the end of the session and updates the page or write an extra program.
- What if we change the data structure and use a dictionary? (Hint: use to keys to store the different activities). How do we have to change the automation function? Is there any change in the performances? (Hint: you'll need to run specific tests adding many inputs to see if something is changing. Read the **unittest** library docs.)

## Corpora Builder: Program Overview

Our task for Corpora Builder is more ambitious.

People from *HumanDemia* want you to create a text corpus for collaborative research (you're right, you'll be in charge of publishing the results on GitHub).
The issue you have to track is the different methods and debates on the adoption of Digital Humanities tools both in secondary school and university.

From the human point of view, this requires something like:

- perform a variety of searches on different search engines;
- open all the links;
- check them and see if they fit or not.

While we can narrow down items that are not going to match our criteria with a decent query, we can't but open the resulting links to see if they match our criteria or not. (Unless probably we turn full time into programming and do some super cool machine learning trick... but that failure is good for us: researcher are still needed and not all research is carried out in a way that can be easily automated.)

Once we go through all the results of the search, we probably store elsewhere the links to the articles we are interested in. 
This whole process is time-consuming and complex.

Further, with the ever changing news you may end up with significant methodological issues such as the fact that the data selected are nonrepresentative because the order of the search results changes: (i) over time, (ii) over browser, (iii) over cookies, (iv) etc.


To solve the previous point you end up freezing time at a certain point. It is then really hard to justify why time was frozen on a certain date. Even if you have a decent justification for that, the research may benefit if you can track what goes on after you froze the time. Maybe you'll get extra data for your research, maybe you can further prove your point, develop a new hypothesis, squeeze in another paper. 

Alternatively, you may defuse the above objection ending up selecting your corpus and sources in a kind of arbitrary way that is highly peculiar such that it gets close to being a personal preference (hardly justifiable, no matter how reasonable) and then say "according to the literature".

With a bit of code we mitigate these issues by way of tracking down data and what has been used. Our first implementation of our Corpus Builder will do the following:

1. take as an input the string we want to search;
2. perform the search on a certain search engine;
3. save the results of the search across all the pages;
4. extract the links from the above pages;
5. saving them to a file, together with the date in which the whole operation was performed;
6. (opt.) sending all to reviewers.

We've already seen that these operations can take quite long, if there are a lot of results (i.e. if the search is poorly defined).
We then may be in need of considering some safety device such as:

- interrupt the whole process after some time;
- skip items in case there are issues connecting to the page.

To build this more complex program we are going to divide and conquer the different operations and implement them one after the other. We'll try to always have a program that is working: the first goal is that of having some that works. Then we are going to iterate and add functions.

### Connecting to the Search Engine and Performing the Search

The first operation we want to do is that of connecting to a search engine and perform the search.

This is going to be quite simple. We use the **requests** module to access the web. From there, we access a search engine and do our query. We need to accept an input from the user for the search she wants to perform.

Let's write our first bit of code. Comments are included to start explaining what we are doing, a full discussion follows.

*Searching a term - ch. 7.2*

```{python eval=FALSE, include=TRUE}
# Overcommented for explanatory reasons
# Load the library that handles connecting to the internet
import requests

# Ask the user for a search term 
query = input('What do you want to search?')

# Performing the search 
searchres = requests.get('https://www.google.com/search?q='+ query)

```

We import the requests module that, as it says in its documentation (https://2.python-requests.org/en/master/), is meant to make HTTP handling easy for humans.
We then define a variable that stores the term we want to search, called **query** which is filled through an input.

The next step is initializing the search, which basically simulates what goes on when we access our search engine and perform the search.
Here we are using Google for convenience. Basically we want to access Google and type in the search term.

In order to do that we need to find out what's the form of Google results. After a little messing around with the https bar, we find out that if you type this in the browser:

**https://www.google.com/search?q=**

then whatever we add after the '=' will perform the search for us.

Once we discovered this, we can name another variable to store the results of our search - I chose **searchres**, but you are encouraged to change this.

We use the **requests.get()** method to store a copy of the page of the results we want. The page with the result is found at 'https://www.google.com/search?q=', which tells our machine to search on Google, and adds the text we wanted to search for (which we stored in the **query** variable).

### Corpora Builder: Adding Safe Tests and Ensuring our Connection Works

So far so good.
But what if the request to the server doesn't work? Suppose the connection gets down or something goes wrong and the page does not exist? (Ok, probably that's not gonna happen with a search).

We want to handle this event for us to avoid the program breaks down. Luckily, requests have this feature built-in. All we need is to add the following instruction:

**raise_for_status()**

to the object that contains our request (**searchres** for me). Thanks request library for making it that simple to check that.^[You are encouraged to look in the models.py file (yes, on GitHub) for the code actual code of raise_for_status(), here: https://github.com/psf/requests/blob/9ed5db8ed28e816b597dafd328b342ec95466afa/requests/models.py ]

Code-wise, we get this:

*Check with raise_for_status() - ch. 7.3*

```{python eval=FALSE, include=TRUE}
# Overcommented for explanatory reasons
# Load the library that handles connecting to the internet
import requests

# Ask the user for the search term 
query = input('What do you want to search?')

# Performing the search 
searchres = requests.get('https://www.google.com/search?q='+ query)
# Make sure the request works (check it)
searchres.raise_for_status() 
```

Remember when we said it's good to know the exceptions and functions of the modules we are using? By looking at the documentation for this function (https://2.python-requests.org/en/master/_modules/requests/models/#Response.raise_for_status) we find out that it has a try/except statement and we are checking a variety of error codes.

Test your code now: access a legit website and see what output you get. Then test a non-existing website. It is also good to figure out what the various error code means, i.e. beyond 404 Not Found. (Bonus points for writing tests with unittest or similar instead of manually inputting them while running our program.)


### From Search Results to Links?


Ok, our searchres is already storing an object with all the content of the first page of results. We are going to process this so that, once this works, all is left is to extend these operations to the following pages.

We can now attempt scraping the links. 
This is the other big and complex operation of our program. Thankfully the BeautifulSoup library is there to help us extract all the links.


Our template of web scraping goes as follows:

1. we need to inspect the page with the information we want to extract (search results, in our case);
2. we open the inspect view on our browser and start looking at the HTML in a quest for what we need;
3. we need to isolate the relevant element and tag;
4. we then use **BeautifulSoup** to extract what we need from the tags.

BeautifulSoup helps us creating an object that stores all the structured markup language and allows us to browse the tree structure, extracting content from the various HTML tags.

The resulting template is something like that:

*Making the soup - ch. 7.4*

```{python eval=FALSE, include=TRUE}
import requests
from bs4 import BeautifulSoup as bs

# [Build a request as before, called request]

# Create a beautifulsoup object (soup, by convention)
soup = bs(searchres.text, 'html.parser')

# Extract what we need
extraction = soup.select('[insert relevant tag]')

```

If you struggle enough you find out that, after searching quite a lot in the HTML through inspection mode (if you have problems accessing this, it's CTRL + SHIFT + I on Brave or right-click and then 'Inspect'), **.r a** should match the urls of the links.

Let's include everything into a single code snippet and run it.

*Adding bs to extract links - ch. 7.5*

```{python eval=FALSE, include=TRUE}
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
```

Are you ready to get the results?

### [] Bad Outcomes

The outcome of our printing the results is **[]**, i.e. an empty list.
This is unexpected. We inspected the HTML and the element we are looking for was there. We struggled to find it. So, what happened?

A first good idea is to print the object that stores the information of our BeautifulSoup object, i.e. what we called **soup**. The idea is to figure out what's going on in the object we are using to retrieve the information.

Given you've been toying around with *HumanDemia*'s tech training for quite long, you already did a print(soup) and are looking for the .r tag. The issue is that... the .r tag is no longer there!

That's why the list is empty. Something happens when you watch the results on your browser and when you automate the extraction of links. Obfuscation comes in!

You can start thinking about data ethics and human/machine interactions: they are your search results, you typed them in, why can't you retrieve them?

You can think about different options (change the search engine, download the page and see what happens, etc). Nonetheless, the first thing we can try to do is to retrieve all the pages with some href (i.e. a link).

We can use BeutifulSoup to isolate all the elements with an href element. We are going to look for all the 'a' HTML tag, select those with 'href' and make a list out of them.

To do this we are going to run the function find_all() on our soup object.
We then make a list of all the links.


That's a first implementation of the code (note we fixed the query term to 'Goofy', here we are testing retrieving the links and do not want to waste much time keep typing in what we want to search).


*Working our way around: getting all the href links in the page we requested*

*Goofy goofy search - ch. 7.6*

```{python eval=FALSE, include=TRUE}
# Imports
import requests
from bs4 import BeautifulSoup as bs

# Searchrequest and soup
searchreq = requests.get('https://www.google.com/search?q=Goofy')
searchreq.raise_for_status()
soup = bs(searchreq.text, 'html.parser')

# Getting links as a href
links = []
for a in soup.find_all('a', href=True):
    print(a['href'])
    links.append(a['href'])
```

If you type 'print(links)', your list is going to get printed.

That's perfect! We are getting results. Links are still there! The issue is that now we are getting *way too many of them*.

Remember, we requested the first page of the results from our search engine. Usually, it has a list of 10 results, plus some video o Wikipedia entry on the right.
Now, evaluate how many items are there on our list of links.

If you go for **len(set(links))** you'll find out there are way more than 10 unique elements. Remember that **len()** returns the length of its item, here the set of our list of links. We are turning the list of links into a set to squeeze out possible repetition of elements.

If we reflect on what we are doing, it is clear that we are catching more than our list: in fact, the 'next' button and the 'image' tab all have links we are extracting. If you use gmail and are logged in, these are all href true elements.

TL;DR: we move from zero link to way too many. What can we do now?

### Extracting more Specific Links

Let's recap what's happening. We got a task, we map it out in pseudocode and start implementing it. We choose some tools (BeautifulSoup) and we were pretty confident that a single piece of code would solve that. (If you search around "how to retrieve links from a search engine" chances are you bump into the ".r a" solution.)
But reality is quite different.

The easy solution did not work. Obfuscation came in. Here we are really programming. We need to find our way around an obstacle.

To create our corpus we have an available strategy: given our links are still there and we managed to extract them, we have to filter this excessive pool of links. There are different ways to do that:

1. *noise filter*: we can compare the various search results across different pages for the same query as well as across different queries. We are looking for what stays constant across these searches. These are the alien elements we want to get rid of. After we have identified these ones, we get our results by subtracting these to the original (excessive) pool of results;
2. *query-based filter*: we filter our (excessive) list of results by keeping only the elements that were present in the keywords of the query. This requires us to elaborate more on the query we get and requires us to make further assumptions of what's relevant in a query.

Neither solution is super excellent and accurate. But at least it is principled and it allows us to keep adding features to our program (and to build a shareable corpus).

### Filter Through Keywords

We start filtering based on keywords. Our leading assumption is that *what we searched in the query, matters for the results*. We can turn this assumption into code specifying that the terms that we searched are featured in the url of the link.

Of course there are issues: what if the term we are searching for is one of the terms that are part of the noise? (e.g. 'video', 'next page' or others).

Still, before trying to improve on that we need to start processing the query. There are at least two things to isolate and care about:

1. the query has *one word*: we are only going to use that word;
2. the query has *more than one word*: we split the case and make sure to have all the terms of the query to be available for filtering;
3. (wasn't it two things?) *standardization*: we need to ensure that the query is usable for the machine. Remember Python is case sensitive. Suppose we search for 'Goofy'. We are going to use 'Goofy' to select only Goofy-links and ignore user-policy-links, etc. If the links are in lower-goofy-format we are going to miss them using our Capitalized Goofy. 

Code-wise we get this:

*Query processing - ch. 7.6*

```{python eval=FALSE, include=TRUE}
# Previous imports etc omitted

userquery =  input('What do you want to search?')
searchreq = requests.get('https://www.google.com/search?q=' + \
    userquery)
searchreq.raise_for_status()

# Query processing: lowercase
query = userquery.lower()

# Quey processing: splitting if it has more than 1 word
if len(query.split()) > 1:
    query = query.split()
```

If you are hard testing this, feel free to remove the input part of the userquery and hard code a term. Then print the items in query and see what you get.

As a quick exercise, make a function out of it that scrapes a page given a certain query, something like **def scrapeterm(userquery)** which returns the items in the query.

Our next task is that of *building a filter based on our query*. The items we need are:

1. the request for a certain page;
2. a soup object to parse it;
3. a list of links obtained with BeautifulSoup;
4. a processed query to activate the filter;
5. a device to check that, for each item in the list of links, the terms isolated in the query are present.

We already know that this tool in point 5 is, regular expression can be pretty handy for that. This time we are only going to **re.search** if the term in the query is there or not. Go back to chapter \@ref(ch5) for a refresher on regular expression and check the docs for the re module (which is part of the standard library).^[Here we go: https://docs.python.org/3/library/re.html ]

Assuming all the items from 1 to 4 are there, a filter is basically doing what follows:

*Basic query-based filtering mechanics - ch. 7.8*

```{python eval=FALSE, include=TRUE}
# Import to have regex
import re

# We have links list from bs4
links = ['items', 'from', 'soup']

# We processed and split the query
query = ['terms', 'of', 'query']

# Scrape links for relevant terms
# Initialize a list of filtered results
filter = []
for link in set(links):
    for q in query:
        if re.search(q, link) is not None and link not in filter:
            link = link.replace('/url?q=', '')
            filter.append(link)
```


Some comments are needed here:

- we try to process as few items as possible, so we remove the duplicates from the links, if any, with set;
- we check that we have a match with the "is not None" idiom, which is discussed in PEP 8 under "Programming Recommendations"; 
- we make sure the link is not in the filter before adding it. We don't want duplicates. This condition wasn't there the first time we isolated the problem and thought about the filter;
- we need to clean the link we are appending to the list. We want a list of items that can be easily copied and pasted into the browser. Keeping the '/url?q=', if it's present, is not going to work.

(The file in the repository comes with a slightly different list and an assertion statement to check it works.)

Ok, we can now move on to the next strategy. There we start to consider moving to a different page. Once we are done with that, we'll include saving the results to file and moving our search through different pages.

### Filter Removing Common Noise

For this implementation of the idea, we are going to code a function that will filter the links. The function will act on our list of links.

Basically we want to define a sublist of links that are made of noise, i.e. reoccurring links. To build the noise list, we need a variety of noise detection expressions.

Assuming we build our list of expressions for noise detection, all we need to do is to check each link in our list on the different expressions in the noise detection list. If the test is successful (i.e. if our regex gets a match), then we add the link to noise.

The function then returns a list of the set difference between the set of all links and the set of noise. Here's the code, we then explain how we the noise detectors were selected:

*Filtering noise - ch. 7.9*

```{python eval=FALSE, include=TRUE}
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
```

A few notes about the code:

- feel free to add type annotations: 'links' is a list. That's not obvious!
- we need to escape the dots in the urls because they are going to be passed as elements of a regular expression. In regex the dot '.' is a special character and this will compromise our search. There's a way to fix this with raw strings. Fix that this way if you prefer;
- try moving the noise initialization *inside* the function and then access the list of the noise you detected from the outside. That's one (harsh) way of learning about scope.

(Yes, at *HumanDemia* they pass you some sub-optimal code and expect you to fix it. It is still academia, after all.)

Ok, now we need to explain how we constructed the noise_detection list. In pseudo code the thought behind that is the following:

1. we have a function that gets all hrefs for a certain request;
2. we run that function for the first page of search results;
3. we run that function for the second page of search results;
4. we compare what's in (2) and (3): given that search results on different pages are going to be different (there are no duplicates) what stays constant is background search engine noise;
5. we print common elements: they are going to be our noise_detectors.

Implementation-wise, let's start with what we already know.

Getting 1 is easy. We already have all the code parts: request, query process, soup links extraction. All you need to do is to make a function out of it (the argument is going to be the url which includes the query, not the query).

Also, 4 is easy. All we need is performing set intersection. This is nice and easy. Assuming A and B are set, we need to call **A.intersection(B)** and we have it. So, to accommodate also 5, we can say:

```{python eval=FALSE, include=TRUE}
intersection = A.intersection(B)
print(intersection)
```

What's still puzzling are 2 and 3, namely, how to move across the pages of results returned by a search engine.

How do we get to the next page? You expect something like:

google.com/search=?TERM/page=NUMBER

But that's not the case. Obfuscation strikes back. 
How do we get out of it?

We need again to work with the url of the search. Start browsing the different page result and read what comes out. Consider this:

https://www.google.com/search?q=Goofy&sxsrf=ACYBGNTZSgTK_0-vONXFac4v_
jWb0EiyeQ:1579169835573&ei=KzggXpDTIpK3kwXLvJPADA&start=120&sa=N&ved=
2ahUKEwjQlNuI8ofnAhWS26QKHUveBMg4WhDw0wN6BAgMEEM&biw=1280&bih=
578&dpr=1.5

Noticed something? It says it's page 13 of results.

Now have another look at the url. See the 'start=number' line? That's it:

https://www.google.com/search?q=Goofy&sxsrf=ACYBGNTZSgTK_0-vONXFac4v_
jWb0EiyeQ:1579169835573&ei=KzggXpDTIpK3kwXLvJPADA&**start=120**&sa=N&ved=
2ahUKEwjQlNuI8ofnAhWS26QKHUveBMg4WhDw0wN6BAgMEEM&biw=1280&bih=
578&dpr=1.5

Ok, you know on what you have to act to have two (or more) searches for the same term. Have fun!

Beware that this automated part is not the one-catch-all-solution. If you find that there's more that keeps popping out that you don't want in your results, feel free to add them to the noise detection list. Further, as we have already seen, there can be implementation issues (with the '.'). So, beware!

### Saving Our Queries

Ok, we can retrieve some links. Can we save them? Saving is a rather easy file operation.


Let's take the same approach we've been using so far. We start with our consolidated program. First, test the new feature, then we include it in our main script. Saving to a file is nothing but:

- create a file object;
- writing content in it;
- close the file.

We can do all that using a 'with' statement. It ensures the file is closed and allows us to rename the opened file, if needed. Tackling the saving issue from our latest implementation, we are likely to use the data we filtered. 

*A simple saving with-statement*

```{python eval=FALSE, include=TRUE}
filteredlist = ['A', 'B', 'C', 'end']
with open('Data.txt', 'a') as file:
    for item in filteredlist:
        file.write(item + '\n')
```

There's not much to say, except that we are adding a newline (\\n) after the item.


Now we have to move this saving feature into the main program. Before adding it, let's think about our use of this saving feature.

We want to build corpora out of it. This requires us to put some efforts into how we organize our folder of saved results:

1. The name of the file should reflect what we've searched. We don't want a data.txt file cluttered with different queries;
2. It would be a nice feature to include a time reference telling us the date the search was performed (we are going to import datetime for this).

The code below accomplishes all this:

1. we rename the data file using the query. Beware to use a string element, not our split query (that is a list). Now you see why it's good to be aware of our program structure;
2. we organize our data document with a general line saying we searched the term X on a specific date (we are using a today variable which calls a **datetime object** - remember to convert it to a string or you'll have a hard time writing it to a file). Such a line helps us as humans. If we were to use this information for some machine-related tasks, these are better stored as a table like query performed, link, date or similar.

In this way we get a human-friendly report about our data.

*Saving searches to file - ch. 7.10*

```{python eval=FALSE, include=TRUE}
# Overcommented for explanatory reasons

# Imports - standard library first
import datetime # Needed to deal with time
import re  
import requests
from bs4 import BeautifulSoup as bs

# Ask the user for the search and process the query
userquery = input('Enter your query')
searchreq = requests.get('https://www.google.com/search?q='\
    + userquery)
searchreq.raise_for_status()

# Query  process
query = userquery.lower()
if len(query.split()) > 1:
    query = query.split()
    
# Soup objects and all links
soup = bs(searchreq.text, 'html.parser')
links = []
for a in soup.find_all('a', href=True):
    links.append(a['href'])
       
# Initialize results
results=[]

# Date processing - get today's date
today = str(datetime.datetime.now())

# Creating the file to save links
with open('Data_for_' + userquery +'.txt', 'a') as file:
    file.write('Results for \'' + userquery + \
    '\' performed on '+ today + ':\n')
    
    # Processing links
    for link in set(links):
        # Loop on queries
        # q is what we want to search on every item in the links
        for q in query:    
            if re.search(q, link) is not None and \
            re.search('google', link) is None \
            and re.search('search', link) is None \
            and link not in results
                link = link.replace('/url?q=', '')
                results.append(link)
                file.write(link + '\n')
    file.write('\n')
```

In this code we are doing some rough filtering hard coding something to be excluded from our lists of results (i.e., removing 'search' and 'google' from the list of links).

You can improve the code by way of using the previous function. Also, the readability of the heading of the text can be improved using formatted strings instead of concatenation. Look PEP 498 to find out how to do it (https://www.python.org/dev/peps/pep-0498/), trading a '+' sign for some parenthesis can be a good choice.

Ok, now we have to deal with multiple pages of results.

### Iteration: Moving to the Next Page

We are almost there. We fought obfuscation and came up with two different strategies to retrieve links. We can save them and keep track of the time of the search.

Now we need to iterate through different pages. We already know something about the format of page results, we went through that pain while exploring what was beef and what was noise across different pages of search results.

If we include the number of pages we want to scrape, these are some of our new challenges:

- we can ask the user how many pages we need to scrape;
- we need to figure out where we are among the different pages of results;
- we have to consider the case of one-pager search results (most often with errors or super-specific searches).

These are some of the changes we can implement:

- our scrape function now takes two arguments: query and number of pages;
- our scrape function needs another loop to go through the different pages.

From our previous experiments we know that search results pages have this format with a 'start' field. So we need to look for the start.

*Introducing a page tracker loop*

```{python eval=FALSE, include=TRUE}
# Add usual import
# Add usual data structure

# Initalize counter to track the current page visited
pageloop = 0
# Specify how many pages to scrape
NUMPAGES = 4

# Make the first request

# Find the start element of the url
start = []
for link in set(links):
    # The url we need has 'start' in it
    if re.search('start', link):
    # We find it and we add it
        start.append(link)
        # We turn the list into a string and process it
        start = str(start)
        start = re.sub('\[\'','', start)
        start = re.split('start=', start)
        
# Check if we have more than one page of results
# Single page case
if start == []:
# Run the scrape function. No iteration.

else:

# Loop on all pages
for pageloop in range(0,int(NUMPAGES)*10,10):
    nextpage = 'https://www.google.com'+ start[0] + \
    'start='+ str(pageloop)
    searchpage = requests.get(nextpage)
    searchpage.raise_for_status()
    
    # Run our extractor function on the searchpage 

```

There's quite a lot happening there.

The basic idea is to keep track of the page we are at with a pageloop variable. The issue is that we need to introduce a variable counter to update the 'start part' of the search engine string.

We basically need to extract the string of search results and then be able to insert different numbers so that we can access the different pages of results.
Assuming we are able to do that, we can then split the case in which there are more pages of results and the one in which results are just on a single page.

If we have more results we need to obtain all of them (with a range function) and construct a request for each new page. On this new page we can run a function to extract the results.

You now have all the pieces of the puzzle. Feel free to experiment and assemble them to get a full working program. Consider what might happen at corner cases like when you ask to retrieve more pages of results than those available or what happens if one of the requests returns a 'not found' error.

### Helper Functions

Helper functions do what they say. Assume you start using your program and figure out there are some combinations of the basic operations you do quite often. For example, what if you want to run more than a query? Do we really have to say "get_links(arg1)", "get_links(arg2)", etc?

Here optional arguments come handy.

This is all you need to do to have a function with multiple arguments that, then, runs your main search function for each term.

*A multi query search helper function*
```{python eval=FALSE, include=TRUE}

def searchterm(query):
    # Insert the specifics for your search

    pass 
    
def multiscrapecheck(*queries):
    """
    Retrive links for multiple queries. 
    """
    for q in queries:
        searchterm(q)
```

You can now see the advantages of working in this way. Different functions take care of different aspects. What to search, saving, extracting. Etc. (Remember that *args is a parameter that returns a tuple.)

You can build your program as you prefer. What if we ask the user to specify arguments as tuples (term, number of pages to scrape) and pass them to a function? What if we want to add more inputs, like which function to take? What if we want to repeat our search every Monday?

### Adding Progress Bars: Tqdm

Our program has a very small interface. If we run a search across 10 or more pages chances are this is going to take long. Our user may start wondering what's going on.

All our programming is super low in terms of interfaces and design. We are running the program from the command line, IDE, IPython or similar. Nonetheless, we have an opportunity to add some feedback.

What if we add progress bars to have some sort of feedback? The Tqdm module (read the docs to find out more about the name - https://tqdm.github.io/) is there to help us. What the module does is that it allows us to add progress bars when we run iteration.

All we need to do is importing tqdm and change the range function of the page loop to **trange()**. We are now using a tqdm shortcut that calls tqdm on the range function, giving us our progress bar (see more on https://tqdm.github.io/docs/shortcuts/#trange).


### Corpora Builder Limitations

Assembling Corpora Builder is a useful exercise to go show how we can create useful programs for our daily academic life. Beware that limitations abound for how we realized the pieces of the program. Here is a list of limits and things to improve:

- Every term we add in the noise_detector is something we cannot retrieve in our links. 
- We are not checking the spelling of user inputs and queries.
- If we have multiple word queries, we are using all the outcomes of the split. This includes one letter word like 'a' (say in 'a taste of collapse') or two-letter words like 'an', 'or', 'of', etc. These can have terribly bad consequences of matching random links we do not want to get.

Some of these can easily be fixed (go try!), some are more complex. Again, awareness is the key.

### Iterating Further 

A second iteration can actually help us address better our methodological needs. What about:

- performing the search from multiple browsers?
- performing the search on multiple search engines?
- taking track of where a certain item was returned from the search engine (i.e. your amazing paper was the third item on the first page or was it buried in the 11th page of results?)
- what about adding a feature that, after opening the link, asks us if it fits or not in our research plan (and, in case, delete the bad link from the list of results)? We'll need to work on our corpora opener program, which follows.

## Corpora Opener: Program Overview

We finished Corpora Builder having a list of files in .txt format. Our human eyes can read it and that's great. Still, we have a problem *using* the data.

Are we going to copy and paste all the documents retrieved in the corpus to see if a link meets our needs? Not at all. *HumanDemia* is not hiring those with a Ph.D. to do that.

Let's see if we can come up with a better solution. For this corpora builder tool to open we also need a function that opens all the retrieved links.
Here is where our *needs as humans clashes with those of the machine*. 

Things we value as the date and the queried term are only a distraction for the machine. For a machine the easier way to do what we need is something like that:

- open a file;
- read the first line;
- open a browser with the first line as the url;
- read the second line;
- open a browser with the second line as the url;
- ... .

This looks quite easy, programming-wise.

It something like the following:


```{python eval=FALSE, include=TRUE}

import webbrowser
with open("urllist.txt") as f:
    for line in f.readlines():
        webbrowser.open(line)
```

(Go read the docs for readlines(): https://docs.python.org/3/library/io.html?highlight=readlines.)

If you prefer, you can open a new tab instead of a new browser.

We already have our data stored as a list of urls on different lines, don't we? Query and date were isolated in the file name, so we almost have a list of urls only, except for the first line.

We can either ignore it (the browser will probably return an error), but there are some issues. In fact, we can't open 20 or more tabs/windows.

We should think about a way to ask the user at least: *how many items to open each time* and *whether to continue with another set of items or stop*.

### Opening Only a Specific Amount of Files

We now have to modify our program so that:

1. it asks for the number of tab views it has to open;
2. it iterates through the file with the links using the determined parameter.

This requires us to add a few complexities.

The most tricky items on our desiderata are:

- be sure that exactly n links are opened on each cycle;
- avoid an out of list error when we display the links.

Here's how to do that. Comments follow.

*Corpora Opener mechanics - ch. 7.11*

```{python eval=FALSE, include=TRUE}

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
                link_countlink_count = link_count + 1
                webbrowser.open(links[link_count])
            if question == 'n':
                break

```



There's nothing too complex. We have to note that:

- we are prompting the user to answer 'y' or 'n'. (We are not checking for different inputs...)
- to check if we have opened the required number of windows (suppose: 4) we check that the remain (that's the % division) between our current link, plus 1 equals zero. In this case: 4%4 = 0. We need to increase link_count by 1 because lists in Python are zero-indexed.
- beware of the types: you can't print int in strings and can't do math with numbers-as-strings.

### Issue Opening Links

If you try opening your search results list, chances are you'll get quite a lot of 'file not found' or similar. If you see the links we retrieved in the txt file for Goofy you'll see they do not look very nice on the eye.

For example: https://it.wikipedia.org/wiki/Pippo&sa=U&ved=2ahUKEwivrPvAi8LpAhVRu54KHbn2BIwQmhMwDHoECAwQDg&usg=AOvVaw3iTam18fbOrKonOQf3UPJB
or even 
https://www.pinterest.it/lesleygc49/pippo-disney/&sa=U&ved=2ahUKEwivrPvAi8LpAhVRu54KHbn2BIwQFjAeegQICBAB&usg=AOvVaw1PWlSxqSE0mb3ExFfQEvWZ.

In my case, the first link doesn't produce any result, but the second does. Why is that? The second link succeeds because of a redirect to https://www.pinterest.it/lesleygc49/pippo-disney/. If you inspect this more, we are getting quite a lot of extra stuff after the '&'. What is we cut the first link after the '&'? Ohh, it works.

Now there's a choice to make. It seems we need to clean our urls to fix this '&' issue. We can split the link on '&', then link[0] has the good part of the url. The choice is: do you prefer to do this in the opening function (here) or back in the corpora builder program? 


### New Iteration

- *Implement user feedback*: after a link of the corpus is opened, ask the user whether it fits for our research goals or not (and, in case, delete the bad link from the list of results). This will force you to explore message boxes.


## Summary

In this chapter we started to build programs based on our needs and diving into the unknown. We optimize our pc startup, create a corpus accessing a search engine and we have found our way into proficiently using our data.

While building some things we learnt about common operations and put them in practice:

- opening webpages and programs using Python;
- keyword-based filtering;
- reading files line by line;
- saving to file;
- performing requests to the web;
- scraping and parsing webpages.

### More Resources

If you are interested in building cool things, a lot is going on. This tutorial on writing timer is pretty cool: https://medium.com/@fidel.esquivelestay/build-a-pomodoro-timer-using-python-d52509730f60.

Also, remember the "try to write something in a certain language and then rework it on a different language"? Here's a list of 100 projects for beginners... in JavaScript. Nonetheless the list and descriptions of the projects are pretty good: have a look https://jsbeginners.com/javascript-projects-for-beginners/.

If you prefer to build games, that's a nice video tutorial: https://www.youtube.com/watch?time_continue=7&v=XGf2GcyHPhc&feature=emb_logo.

I have mixed feelings about video tutorials. On the one hand you can't follow them at your pace, you have to wait for the instructor to type in the code. On the other hand, there's a lot you can learn while following someone that's coding: how are they testing the code? What strategy are they using? Further, you can receive bonus explanations about Python internals. 



### Further Work

- try to run SQlite. It's the database manager bundled in Python (it may be a bit complex to locate it, though). Add it to your automation start. Build a simple database (e.g. your books or cd collection, you papers).
- Does using the following BeautifulSoup code change something in our scraping programs?

```{python eval=FALSE, include=TRUE}
for link in soup.find_all('a'):
    print(link.get('href'))

```

-  Implement a spell checker for Corpora Builder in case the query is miss spelt. Norvig has a good one: https://norvig.com/spell-correct.html.


If you like to develop other productivity tools, here's a list of interesting things:

- build a timer;
- build tools to help you formatting in Markdown (e.g. adding or removing \#\#, adding or removing list items);
- build tools to merge and cut PDF (Hint: search for Automate the boring stuff with Python);
- build customized search engines for your needs. For example, a program that runs your searches for papers and references on your specific databases. Have a look at the **HowDoI** program to see an amazing example. You can think about this exercise as a form of Corpora Builder that runs the query on a more specific search engine (for example, jstor or your university proxy to the online library).


