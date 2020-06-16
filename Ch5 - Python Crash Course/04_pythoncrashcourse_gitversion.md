{#ch5}
# Python Crash Courses

"Programming languages are **languages**," says the *HumanDemia* teaching material. "They also have dialects and programming styles. They are alive and have communities". 

Here we start with a crash-course on Python, highlighting some of the things we are going to cover in Part III, dedicated to programming things that may have an academic import. The next chapter covers dialects and styles, Python features that can be and feel hard to learn, and how to get the most out of our Python-learning journey.

As you already know, *HumanDemia* suggests you to type the code yourself. If you really want to copy and paste some of it, I understand that. Still, *beware of the quirkiness of pdf*. Even if you copy and paste the code the spacing is likely to be lost - and, as you are going to find out, spacing is vital in Python.^[If you want a copy and paste approach, clone the GitHub repo of the book.]

Also, to make sure the code fits in the pdf page and e-reader screen, I have to use multiple strings quite often. There two ways to continue a string to the next line and I have used the one with '\\' more than I wanted to. Nonetheless, I thought that made the string continuation easier to be recognized in some cases and so I used it.


## Look How Easy it Is to Write Python

Let's go super experimental and harsh here. Take a look at that.

Can you read some of that? Can you guess what the various parts of the code do?

*Crash impact with Python (Pt. 1) - Ch. 5.1*

```{python eval=FALSE, inclue=TRUE}

import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) \
    or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)
```

Here are some things to note:

- Python reads a lot like English;
- it does not look too much "programmy": there are no curly brackets;
- there are some patterns we can identify: def word(anotherword)**:** - the column is important!
- things look nice and ordered. Space seems important.
- we can recognize some commands: return, open, import.

Ok, we are going to read some of it together. The first thing we learn about Python is that comments are included with the hashtag symbol \#. Yep, comments in Python are different from Markdown *syntactically*; *conceptually* they are still comments.

So we are going to read this together adding some comments to guess what the code does.

*Crash Commented Python*

```{python eval=FALSE, inclue=TRUE}

#we import something
import re #that's mysterious

#that's a counter
from collections import Counter

#we def(ine)? something related to words
#we are getting something in return that deals with findall
def words(text): return re.findall(r'\w+', text.lower())

#we are doing something to the 'text', there's this
#lower() on it. It has to do with format or capitalization?

#now we have allcaps. That should mean something

#we open a txt file named 'big', probably
#open('big.txt').read() probably reads the file
WORDS = Counter(words(open('big.txt').read()))

#WORDS probably contains some form of Counter operation
#performed on the big txt file we've read

#from here we have other definitions
# There's text between " " that tells something about that
def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N
#here we are getting a probability of a word.
#we take the word out of WORDS and divide it by N.
#Above we know that N is equal to the sum of
#WORDS.values... no idea about the internals but sounds ok


def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

#here learn we are dealing with spellings. To correct a word
#we return the 'max' of candidates for the word based on
# the key P, i.e. the probability we have just defined.
#but, wait, where are these candidates? Move on...

#...here they are
def candidates(word): 
    "Generate possible spelling corrections for word."
    #that's what candidates def does...
    return (known([word]) or known(edits1(word)) \
    or known(edits2(word)) or [word])
#ok, this return statement looks programmy
#we can spot 4 alternatives listed with 'or'
#we are mentioning known words and known edits of the words
#chances are these will follow...

#here we go
def known(words): 
#oh, known(words) are alternative words we know in the WORDS
#thing above we generated opening the big txt file.
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

#we are returning a set probably (set)
#the parenthesis looks scary but reads like English:
#we get a set of w, for (each) w in words (i.e. the thing we
#created with findall if the w is also in capitalized WORDS)
    
```

Cool! We were able to learn a lot and the program was far from an easy 'Hello World' program. Give yourself a pat on the back.

The program has two further "defs" and that's it. **Edits1(word)** looks scary, but it says to us that it includes "All edits that are one edit away from 'word'". (*Spoiler*: that is called a **docstring** in Python-jargon). **Edits2** iterates the concept (two edits away) and then has another funny parenthesis.

Here's the missing code. Try to read it.

*Crash impact with Python (pt. 2) - Ch. 5.2*

```{python eval=FALSE, inclue=TRUE}

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    \
    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               \
    for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] \
    for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           \
    for L, R in splits if R for c in letters]
    inserts    = [L + c + R               \
    for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
```

Ok, we haven't even started with the rules of Python syntax and we were *already* able to grasp quite a lot of a far from obvious program. There's a reason why Python is sometimes referred to as "pseudo-code that actually runs".

If you are curious about what the program was, that was Peter Norvig's spell checker. Here's the full code and explanation: https://norvig.com/spell-correct.html. Feel free to have a look.^[Norvig works at Google and, among many other things, he has a book called *Paradigms of Artificial Intelligence Programming* you can read for free here: https://github.com/norvig/paip-lisp, yes, GitHub is that cool.]

"That's a nice example!", you find yourself thinking. Ok, it was non-obvious but it resonates. "It seems people at *HumanDemia* want me to critically reflect on the tools I use in my daily work at quite a different level," you think. Next time RStudio doesn't catch a typo we will be able to reason about it from a different perspective.

Oh, if this little program about spell checking is making you feel uncomfortable, fear not. We are not going to do "crazy math" or "AI stuff". This little experiment is meant to show that the "gap" (if any) between Humanities and programming is way thinner than you thought. You were able to read code that does something useful like checking spelling and suggesting what you intended to write but spelt wrong.
That's something amazing.

Yes, there were some obscure things. (If you fancy spoilers: '**re**' is a module to use *regular expressions*. For now, think of them as detective search tools. Regular expressions are the cause of the **r'\\w+** which scream insiders' jargon.

Also, the "funny parentheses" are *comprehensions* which are one of Python unique features we are going to see in a while.)

Last thing. Mentioning Norvig and his book is no accident. Try to read some code examples from the book (same author: Norvig, but a different language: LISP). Here's one example: https://github.com/norvig/paip-lisp/blob/master/lisp/compile1.lisp. It looks less easy, at least).

Ok, fear not and move on! Let's learn more about Python.

**Section Credits**

This experiment was inspired by a similar "dive into the language without knowing it" you can find in the *Head First Java* book by Bert Bates and Kathy Sierra. 


## Python in General: A Readable Design

As you have already seen, Python is easy to read. It is "almost like English" and it is not *that* intimidating. In fact, you can probably type most of the code you've seen. There were no '\{'  or '\}' or other signs you need to struggle and figure out how to type. From that point of view LaTeX, is harder than Python and also HTML has a lot of opening and closing tags.

Coding-wise, it is often said that "code is most often read than run", Python builds on this. In other languages weird signs (like \{ and \}) or end of the line signs (like ';') are used to delimit the end of a line or an instruction.

Python *uses space and formatting* to achieve that. This should be something friendly for academics. This also means that *space matters*. This leads to specific code-formatting strategies you need to care about.

When you indent code you are delimiting block of codes. The standard practice is to use 4 spaces for the first level. Add four more to the second level, etc. If you use TABs, they can mess out your code. 

If you are using an editor, as Spyder, you can configure it so that tabs equals four spaces. Feel free to spend some time in Spyder exploring preferences in the tools. 

"Ok," you think checking the first box "these *HumanDemia* practical programming stuff is not that complex".

To really have a grasp of how code is displayed and what's *Python standard coding practice* check out PEP 8 (https://www.python.org/dev/peps/pep-0008/). PEP means Python Enhancement Proposal are official pieces of documentations guiding Python developers community and/or presenting new language features.

If you come from academia there are chances you may *overestimate* the 'official'. Go and read the document. The tone is informal but on point. It shows good and bad examples with code. You are reading commented Python code and absorbing does and don'ts.

Now that we know something about how parts are divided, let's have a look at the general structure of a Python program.

## General Structure of a Python Program

A Python program has a general structure that goes like this most of the times:

1. entry line that starts with '**#!**' this is called *shebang* or *hashbang.* This message is there for your shell and tells it how to use the program. If you see this in the first programs you read, that's likely to be mysterious;
2. lines of comments (single comments with #, multiline comments between """ comment here """). These contain a license - if it's not provided elsewhere in the files of the whole application - or an overview of what your program does. Now comes the  most common lines;
3. **import lines**. Python is cool and has a lot of batteries included or extra batteries. You call what you need with the 'import' function. This were the starting lines of Norvig's spellchecker importing the **re** module and **Counter**;
4. the instructions of the program. Functions, classes, etc. Norvig's speller was all about def(), i.e. function;
5. a 'main' routine, i.e. what you want your program to do using your functions. Think about the main call as a recipe;
6. a way to call the recipe, i.e. the main() function that goes like this:

*Main call*

```{python eval=FALSE, include=TRUE}

if __name__ == '__main__':
    main()
```

This last line also allows a Python program to check if it is run from the command line or it is imported by a Python program as a module (i.e. with the 'import' command list in (3)). Also, this line shows a way in which Python does look *programmy*: the use of underscores is peculiar and important for the language. In Python the double underscore pattern is referred to as **dunder** (i.e. *do*uble *under*score).

The list is by no means compulsory. What matters to us now are 3 and 4. Should you go around checking programs on GitHub or reading tutorials, you have an idea of the general picture. 

On Github and Jupyter notebooks you won't see many shebangs. The same holds for licenses.

Now that we have a general outline of a Python program we can explore importing and writing the main instructions. This allows us to get deeper also in the puzzling main-name line.



## Import: Load all the Tools you Need

Before you start building something you need to have all the tools at your disposal. Coding is no different. Once you have installed your tools and chosen and IDE or text editor, it's time to pick the right tools to construct the logical architecture of our program. The first lines are there to import our tools of the craft.

We import modules. Modules are code containers that have some code we need. Go back again to Norvig's program. We need to count words. There is no need for us to code a device to count things inside a certain collection: we can import 'Counter' from a specific module called 'collections'.

The syntax for the import is quite simple, I'll show it directly in code with examples.


*Import syntax*

```{python eval=FALSE, include=TRUE}
# importing a whole module: 
# import [module's name]
import os #os handles operative systems tasks, file handling

#importing something specific from a module:
# from [module] import [something]

from collections import Counter
from bs4 import BeautifulSoup #a parsing library

#importing something with aliases, to save on typing
#or avoid conflicts with name

# import [something] as [alias]

import pandas as pd #data processing library
```

To use a module you've imported you need to have it installed. If that's not the case you'll receive an error message. The compiler tells you that the module can't be found.

To install a library you **conda install** it from the Anaconda prompt (or you **pip install** from a windows shell - this was already covered in chapter \@ref(ch4).) 

**Beware**: sometimes you may receive errors like "module X is not installed" when you *know for sure* you conda installed it. What happens is probably that you are working with virtual environments and:

1. you are working in the wrong virtual environment;
2. you are in the correct environment with all the relevant modules but you haven't activated it. 

"How do I know which library does what?" I hear you crying. Short answer is "experience". Practically, you can start learning Python's standard library. The standard library has a bunch of core functionalities.

Before looking outside the standard library you can look into it. Do you remember when we talked about the importance of reading the docs? That was one of the reasons. Anyway, at the end of the chapter you can find a list of commonly used libraries, both standard and non-standard.

We still have to deal with *importing your Python programs* but we need to know more about Python to do that.

## Functions: Let your Program Do Something for You

Ok, let's start coding. Open Spyder and reach IPython. We follow the cliché of "Hello world" programs. Machines are nice and they always cheer you.

So, go in IPython and type:

*Hello world - ch. 5.3*
```{python eval=FALSE, include=TRUE}
print("Hello world!")
```

Imagine what happens and see the results. I guess everything goes as predicted. 

Now move to the next step by *messing around*. Try removing some '(' or adding ';'. Remove quotations or change them to a single quotation. Keep experimenting in IPython so that you don't have to run the whole program to just see the results of a single instruction.

Ok, now think about writing "hello world" as function. Instead of printing "hello world" via a direct print we call a function that will do the printing. Our previous experiment already gave us the syntax: it's **def** keyword. And don't forget the colon. 

The file 5.3 of hello worlds have that version. The main call is missing, try to add it. Also, can you write a function that says 'Hi!' to the name we pass to it? (Think about the Edit1(word) functions...).

Cool. Ok, now for something different. Search for the documentation of Python's print function. Folks at *HumanDemia* expect you to be quick at that.

Reading the docs is a skill you have to learn, like reading a paper or giving a talk. Start using the info in the docs to get a grasp of some of the errors you have received while experimenting. (Bonus points for searching informations about the error Tracebacks.)

Ok, the print function is pretty boring and, most of the time, you are going to define your own functions. Actually, the print *function* is historically controversial for Python and printing to screen is far from that easy and boring in other languages... but coming from Humanities you are *already* good at history and comparative stuff. Let's go back to functions.

Functions take zero or more argument(s) and are defined with the following syntax:

1. **def** keyword: tells Python you are defying a function;
2. name of the function;
3. (): contains the arguments of the function, if empty it means there's none;
4. ':' tells Python the function starts;
5. newline;
6. indent (4 spaces);
7. instructions of the function (could be more than one line);
8. **return** keyword: tell the function what to return;
9. content to be returned.

The last two items are optional. Think about a function. You've seen one before in disguise.

Here's function example:

*A badly named function*

```{python eval=FALSE, include=TRUE}
def main():
    print('Hello world')
```

(Can you rename the 'main' function in a better way?)

If you press enter in IPython or run the program in the IDE (shortcut to run the program F5, of CTRL + ENTER if you have created a code cell, i.e. have a line that goes like that: # %%) nothing happens.

To have your function running, you need to *call it* (think Blondie). To call a function, you call its name and its arguments (here, none). Hence to receive: 'Hello World' you need to call main().

Like this:

*Calling a better named function*

```{python eval=FALSE, include=TRUE}
#define the function
def say_hello():
    print('Hello world')

#calling the function    
say_hello()
```


If you now call main() you are going to execute its content. In this case the content is a print statement.

Let's see a function with some argument and a return statement. This function includes **docstrings**, contents between triple quotes that describe what a function does. We have seen them already in Norvig's code.

(Docstrings have their own PEP, number 257 - https://www.python.org/dev/peps/pep-0257/. If you read PEP 8, you'll see they are referenced there. Also, by including docstrings into a function (or method, class, module) we are populating the dunder doc of that object.^[Remember? Dunder is the double underscore pattern, so \_\_doc\_\_ is 'dunder doc'. By saying that we are populating the dunder it means that we are storing the docstrings information somewhere they can be used. Suppose we have a tool that creates software documentation. This tools will look for the information in dunder doc and organize them. Remember using IPython to *know more* about functions and pieces of code? Often you are getting info stored as docstrings.])

*Proper named function with docstrings and return - ch. 5.4*

```{python eval=FALSE, include=TRUE}
#function example with one argument and return

def capitalize(word):
    """
    The function takes a word in and it
    returns you the word, but capitalized.
    """
    # that above is a docstring. It tells what a function does and 
    # can be used to document our code
    # Norvig's code had them, only in single string mode "".
    capitalized_word = word.capitalize()
    return capitalized_word
```

Copy this function - mind the space - and see what happens if you call **capitalize('I want this bigger')**? Again, play around with the stuff. What happens if you pass an argument without quotes? What if you pass more arguments?

The function above introduced us to *docstrings*. Docstrings are pieces of text written to tell users about what certain pieces of code do. They are enclosed between triple double quotes, as we know already. A docstring is ignored by the compiler, so you can use it as a multiline comment as well.^[Still they will populate dunder doc if they happen inside functions, classes and methods.] (The next chapter will show you more about docstrings and documentation.)

The function above also makes use of a **method**, i.e. the **.capitalize()** part of the program. There's quite a lot to be done with functions, but that already allows us to do some work.

Beside that, before moving on with more complex functions, we need more LEGO pieces to play with.


## Data Structure: Everything Has its Natural Place

Python is a general purpose programming language. You can build a spell checker on it or a website, perform mathematical computations or use Python to visualize data. There's a lot you can do with it.

To do all these different things, you have to cleverly use different data structures. 'Data structures' are exactly what you expect: ways to store and contain data. Different types of data require different data structures.

Data structures differ not only for the kind of data they have as the section's title suggests. It is fairly easy to expect that we have a way to store text data and a way to store numbers...

...Well, *of course* you can spot corner cases: we are from creative Humanities, we ask the questions about possibilities. What about the number 'pi' (of pi-day)? What about 'She scored 98% at the test'? And is 'A' in 'We got A for our team assignment' a word or a number?

When dealing with data structures we have to care at least about three (plus one) things:

1. *the kind of data they can store*: if we put text in number-containers we are going to get into troubles;
2. *the methods and functions associated with that data type*: we can do different things with different data types. (We'll find out in a while.) For example, we expect to be able to divide two (or more) numbers, but dividing pieces of texts sounds bad;
3. *the kind of data structure we are dealing with*: data structure can be mutable or immutable, for example. Suppose you want to check the number of emails you receive during the day. You find a way to access your inbox every ten minutes and download the number of incoming emails and update your counter. If your counter is an immutable data type you are going to have no update whatsoever after the first data retrieval or an error saying "hey, can't update or modify a data structure that is immutable";
4. (actually +1) *how the data type is implemented*: if you care about performance - and sooner or later you may have to worry about that - it is important to know how your data structures are implemented. This looks tricky (that's why it's +1) and is due to the fact that there are different programming languages that can be faster or slower at executing the same task. Python, as you may find out, is not that fast. Still nothing forbids you to use Python to build complex tools and calculations that use faster programming languages or implementation to achieve better performances. That's the case with **numpy** the library that powers most of the scientific Python libraries offering faster implementation for arrays (and more).

There's no need to know all the internals of data structures (at least for now). But it's good to know a little bit of them, just so that we are not going to cry when things do not go as *we* expected because we provided the wrong datatypes to our functions. (Guess what tells you what kind of data a function expects and what it returns? Yes, the docs!)

With that said, we are going to cover a little bit of data structures, their methods and how to access the elements we put into a data structure.


### String Literals

*Strings store text*. You've probably guessed that. And you know we've used strings already when we've printed "Hello world!". To tell Python that there is a string, we need to include the content of the string between quotations, either single 'string here' or double "string here".

We can easily assign strings to a variable: to assign something to a variable we use the '=' sign. The '=' sign does not mean that X equals "Hello, there", but rather that "Hello, there" (the angel from my nightmare)  is assigned to X.

If it helps, read the '=' statement **right to left**: what comes to the *right* is assigned to what's on the *left*. To say that something is equal to something else, like '2+2 equals 5' we have to use the '=' sign twice, so '2+2 == 5'.

A useful formula to remember that difference is that **assigning is not equality**.

The syntax for strings goes as follows:

*String syntax*

```{python eval=FALSE, include=TRUE}

#string creation with single quote
variable = 'content of the string'

#string creation with double quotes
variable2 = "content of the string"

#you can add numbers to strings, if you want
variable3 = "3" #a number as a string

# do you think that ' "3" == 3 ' is a True statement? 

#string can continue on two lines
stringvar = "this strings goes on to another \
    line" #the \ does the trick but beware not
    #to include further code after it
    
#another way to continue strings, using brackets
stringvar = (
    "first part of the string goes there"
    "and that is the second part "
    )

```

There's an important thing to notice. To produce strings we are using ', which is a character we are going to use, for example, if we say "Hi! I'm fine, and you?".

How do we tell our machine friend that some characters are used in the text and some are used to create strings?

Welcome to **escape characters**. If we are using something that is a reserved item of a programming language, as ' here, and you want to use it with its non-reserved meaning, you have to escape it.
To escape a character you have to add the *escape character* of your programming language, which for Python is '\\' (as for RStudio).

When you prompt the user to give you pieces of information and inputs you get them as strings. Remember that, because sometimes you are asking for numbers and you get them as string inputs. (See above the questions on string number three being equal to number 3.)

Open an IPython session and write what follows (to ask for inputs we use **input** keyword):

*Asking the user for input* 

```{python eval=FALSE, include=TRUE}
fav_number = input('What is your favourite number?')
print(fav_number)
```

Use IPython to *check the datatype of fav_number*, i.e. use the function **type()** on fav_number. You'll see it is a string. It is easy to convert a string to an integer (there's more than one data type for numbers): use **int()**.
(To go have something converted to a string, use **str()**.)

Ok, re-read the paragraph above and come out with some exercise or conversion scenario to put this into practice. Operating a calendar may require conversions: you enter numbers for the dates as inputs.^[Time objects are quite complex, if you plan to work on task scheduling and optimizer be sure to read the datetime module.]

If you have a register of mid-term assignments and students you may have numbers (for deadline and, depending on the scoring system, grades) and strings (student names). Additionally, you may have students' IDs and course names. 

Ok... 
There's quite a lot we can do with strings:

- we can concatenate two or more strings with the plus (+) sign.

*Strings concatenation examples*

```{python eval=FALSE, include=TRUE}
#concatenation example
name = 'John'
surname = 'Snow'
fullid = name + surname
print(fullid)

#concatenation with space
full_space_id = name + ' ' + surname # ' ' is the space
print(full_space_id)

#concatenation with newline
full_linespace_name = name + '\n ' + surname # \n is for nl
print(full_linespace_name)

```

- we can slice our string, i.e. select a part of it. To do that we use square brackets to include the indexes we want to slice, separated by a column.

That's the formula:

**string[slice_begin:slice_end]**

The first index is *included*, the last *is not*. 
To apply the formula you need to know that a string first letter has **index 0**, not 1. Get used to that. (The reason for that is that strings are arrays of characters and arrays in Python are 0-indexed.)

Also, you can have negative indexes like -1. Negative indexes are counted **from the end** of the string, so -1 indicates the *last* letter of the string.

Ok, let's get practicing:


*String slicing examples*

```{python eval=FALSE, include=TRUE}

test_string = "A quite long string for practice"

#If you want A:
test_string[0:1] #from zero included to one excluded

#If you want 'practice':
test_string[-9:-1] #(we count from the end, and  move backward)

#If you want 'quite':
test_string[2:7].

#Remember spaces are included in the count.
#The first space is
test_string[1:2]
```


You can also access single letters: just point the place the latter occupies between square brackets. Remember it's zero indexed. (So, in the above example 'A' is test_string[0]).


Strings have a variety of methods. Methods are functions you can call on certain objects, like strings in this case. To access methods we use something called '**dot notation**' (or dot-syntax). Dot-syntax is common to different data structures.

In some abstract form the idea is that we first specify the object we want to deal with, like a string. Then, after a dot we invoke the method (that gets applied to the object that comes before the dot). So:

**object that has a certain method** + **. (dot)** + **method name()**.

(This is different from *functions* in which the object we want the function to be applied to is provided *inside* the brackets. Go and review the previous 'capitalized' function to see a combination of functions and methods.)

Here's a more verbose take on dot notation. To access the methods you take the name of your object, add a . and then call the method. The method is a function, so it has a couple of brackets () at the end that are empty if the function takes no parameter but may have them. For example the **.replace** method takes two parameters: first what you want to replace and then what you want to replace it with. So string.replace("C", "D") will chance all capitalized Cs in the string with capitalized Ds.

Ok, let's provide some examples. Suppose you want a function to shout on webchat, hence it will return all caps.

We know how to define functions. Let's build this up with comments:

*Shouting objects with dot notation*

```{python eval=FALSE, include=TRUE}
def shout(phrase): #phrase is going to be a string
   return #here we call the string method to capitalize

#capitalize test, make sure we can capitalize
test = "Be all capitals"
print(test.upper()) #.upper() is the all caps method

#get back to the function

def shout(phrase):
    return phrase.upper() #a return will give it back
    #us the phrase printed

#try to shout 'Looser!'

shout('Looser!') #correct

#try what happens without passing a string
shout(looser)
#try also keeping the def
    
#compare with

def shout_to_be_called(phrase):
    phrase.upper()
    
#what happens if you type in the interpreter
#shout_to_be_called('Help me please!')?
#how can you make it appear on the screen?

```

This simulates a way to work towards a solution. With bigger projects you can automate some tests. For example, if we want to be sure that the upper() method is making everything capitalized we can write a statement checking that the result of shout('Loooser!') equals our expected result, i.e. LOOOSER!.

This can be done with the '**assert**' statement. The docs are here (assert, plus more kinds of Python statements some of which we touched and some we haven't, at least for now): https://docs.python.org/3/reference/simple_stmts.html. If this whole idea of having checks (and balances) and controls in your program - feel free to build an analogy with a constitution or the organization of powers in a State - then testing is for you. And it's great that you like it.^[I prompt you to explore testing more: the module you are looking for is unittest: https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest and there it is.]

There are way more strings methods that do the following:

- **split()** ("specify an element to delimit the splitting"): suppose you have a sentence like "There are two apples" and you want to isolate the words. You are going to split on the space. So: sentence.split(" "). Beware that split returns data as a list (see in a while);
- **replace()** ("element to be replace", "replacement"). Suppose you want to change 'cat' into 'mat'. Assuming string = "cat", you call string.replace("c", "m"). Go and experience in the interpreter or IPython;
- **lower()** (opposite of upper, returns string in lower case).

There are many more methods for you to search. It won't be difficult. Come out with examples for most of the methods you have to be sure you can use them. Then think about how to use them to make something.

One last thing: strings are immutable. You can't go inside the first letter of

ExampleString = 'Case'

and assign it to 'B' to have ExampleString = 'Base'.

Try

ExampleString[0] = 'B' and see. (Use the replace method to achieve that.^[How can we succeed with the replace method if strings are immutable? That's the kind of great questions that prompts your ever-learning attitude and grasping of the internals of Python. Docs for replace have your answer. And then you'll want to find out more about copy])

Nonetheless, lists, our next data structure *are* mutable.

### Lists

Lists are widespread data structure. They can hold as many things as you like, of different kinds (you can mix strings, numbers, etc). Oh, list is a reserved word so you can't name your list 'list'. We convert something into a list with **list()**, as we did with **str()** or **int()**.

Lists are initialized with square brackets, like this: \[\]. Objects that are in the list are separated by a comma. List can contain lists as objects.

*List examples*

```{python eval=FALSE, include=TRUE}
A = [] #is an empty list. 
A_list_with_numbers = [1, 2, 4, 5]
MixedList = [1, 'two', 3]
TextToString = ["once", "opon a time", "there", "was", "a verb"]
NestList = ["This list", ["has a nested list", 1, 2, 3], \
    "that contains 3 numbers"]
```

The array-like syntax to access letters of a string is valid for strings as well, but this time you are going to access the **item** in that place.

*Accessing list items*

```{python eval=FALSE, include=TRUE}
A_list_with_numbers = [1, 2, 4, 5]
print(A_list_with_numbers[0]) #prints 1

TextToString = ["once", "upon a time", "there", "was", "a verb"]
print(TextToString[1]) #prints "upon a time"
```

List are mutable, i.e. you can use array-like indexing list[index] to change the list.

*Changing items in a list*

```{python eval=FALSE, include=TRUE}
chage_2_to_3 = [1, 2, 4, 5]
print(chage_2_to_3) #prints [1, 2, 4, 5]

chage_2_to_3[1] = 3 #remember: zero-indexed!
print(chage_2_to_3) #prints [1, 3, 4, 5]
```

Most of the time we use list to store things we need.

Suppose we have a list of words and we want to select those that are longer than 3 characters. To evaluate the length of something we use **len()**. Depending on the objects it will tell us different things: items in a list, characters in a string, etc.

To add an item to the list we need to call:

**name_of_the_list.append(name_of_appened_it)**.

Yes, that's a list method. And, yes, it uses dot-syntax.

To check if an item is longer than 3 characters we have to check:

*Conditional statement with a deliberate error (spot it)*

```{python eval=FALSE, include=TRUE}
if len(item) > 3:
    result_list.append(item) #here we add the item to
    #a list called result_list

```

If you try to run this code it will throw you an error. Can you guess why?

Read it again.

Yes, the list.

Python has no idea what this result_list is. It was never mentioned.

Try to fix the code and tell it that there is a list called result_list.

If you are stuck after writing 'result_list = ' remember we need to tell Python it's a list. "But what's in there?" you ask... Well, nothing, *for now*. So you *initialize it as an empty list* with two square brackets.

Before giving you the whole code I'll mention briefly how to go through the items of a list, anticipating a bit of *flow control* (we did that already mentioning the if statement... you see? there's nothing complex in isolation. Issues arise combining our LEGO programming blocks into something bigger).

Basically you want this to happen. **For** every item in the list, *do* something. English guides Python syntax: we need a for loop. Here's the whole program.

*Iterating a list with a for loop, printing items bigger than 3 - Ch 5.5*

```{python eval=FALSE, include=TRUE}
#the list we want to test
test_list = ['no', 'yesss', 'tooshort', 'arg', 'nop', 'nope']
#initialize the result list
result_list = [] #[] empty list

#start iteration on the test_list
for item in test_list: #item is conventional. Use what you like.
#check the item
    if len(item) > 3:
        result_list.append(item)

print(result_list)    

#curved balls
#what is len(result_list)? and len(test_list)?
#what about len(test_list[2])?
```

You can make a list of out something with the **list()** command. For example if you **list("turn this sentence into a list")** you are going to get a list of 6 words.

Commands like this (and **str()** and **int()**) that creates a type of object of a certain type are called *constructors*. You can use constructors to turn data of a certain type into another one.

Lists have many methods and there's quite a lot we can do with that. Many functions return lists. For example: regular expression re.findall() returns a list of matches. We have seen this in Norvig's program and we are going to use it later.

Also, the **range(start:finish)** returns a list of values from start (included) to the number before finish. (It's the same *logic* of the string method **slice**.)

Before moving to dictionaries guess what the following does (get the answers from an IPython session):

- range(7);
- range(3:7);
- range(10)+1.
- range(10,100,20) 

Curved ball. What's the third parameter in range(10, 100, 20)?


### Dictionaries

Dictionaries are another *mutable* data structure. They are similar to list but give you more control over the items. Dictionaries stores its items as pairs of *keys* and *values*.

Think about them as an address book, you have "name" (key) and "value" (phone number). We use keys to retrieve the corresponding values, so we have to provide immutable data types as keys.

Dictionaries are initialized with programmy-brackets (curly ones). Keys and values are separated by a column. Dictionary items are comma-separated.

*Dictionary like phone book*

```{python eval=FALSE, include=TRUE}
phone_book = {
              "Alice": "123", #number as string
              "Bob": 231, #this number is an int
              "Carl": "312"
              }
```

Iterating on dictionaries is more complex as we now have to consider *both keys and values*. Nonetheless, dictionaries allow us to add some further structure to our data due to the key-value pair. Further, dictionary items maintain the order at which they are inserted into the dictionary as of Python 3.7.^[There are reasons to call 'conda update'.]

Why do we need dictionaries? Can't we use lists all time? Well, lists keep track of the order, but there's no structure into it. If you list [person, number, person, number, person, number] *you* can see a structure in the list but the list data structure offers you no structure to store it. (Ok, you may do tricks to print only persons and only numbers... can you spot a way? Nonetheless, lists are mutable and it takes a little to make an indexing mistake or drop an item and mess the structure we tried to add to the list.)

Remember when we talked about the balance between being exhaustive and concise to the point in the introduction? Data structures are one of the many trade-offs. 

Dictionaries are a lot of fun and can be useful. Maybe you want to practice a foreign language while commuting or attending boring meetings. You would like an app that throws you some words to test if you know the meaning. Basically you are going to have the vocabulary as a (Python) dictionary of keys (lemma) and values (definition).

You are then asked if you know the word or not (you can even add a 'not so sure'). Depending on the answer, you may want to see the definition of the word (or maybe to add a button with "show definition"). Have fun programming this! (You can use the NTLK module to access a thesaurus of words as a database.)

If you think this is too easy, you can save your performances and get asked questions depending on how you did in previous tests. (Maybe you want to build more dictionaries for the kinds of answers where you store  the word and the times you get it right / wrong / not sure).

Below we are you some methods to:

1. check that a key is in the dictionary;
2. print dictionary's **key(s)**;
3. print dictionary's **value(s)**;
4. print dictionary's key, value **pairs**;
7. (later on, once we introduce comprehensions, we'll see how to *swap* keys and values).

Again, we are using **address_book** dictionary as our dummy helper. And, once more, we are anticipating for loops (see flow control in a little while).

*Dictionary operations - ch. 5.6*

```{python eval=FALSE, include=TRUE}

address_book = {
              "Alice": "123", #number as string
              "Bob": 231, #this number is an int
              "Carl": "312"
              }

# get the value for a certain key 
# (and return the default, if provided.)
address_book.get("Alice")
address_book.get("Ann") #returns 0, no Ann in our dict

#Print all values in the dictionary, one by one:

for x in address_book: #x takes the key
    print(address_book[x]) #dict[key] returns you the value


#You can use  values() function to return values of a dictionary:

for x in address_book.values():
#now x is whatever is founf in values() - i.e. values already
    print(x)
  
#Loop through both keys and values
#use the items() function that tell which items we have
#in a dictionary, i.e. keys values:

for x, y in address_book.items():
    print(x, y)
  
# you can replace x and y with what they stand for
# i.e. key, value

for key, value in address_book.items():
    print(key, value)


```

### Other Data Types and Data Structures: Integer and Float; Boolean, Tuples, Sets

There other data types and other data structures you need to be able to identify. Again, this is no introduction to the whole topic.

Numbers - as Data Types - are represented as Integer (e.g., 1, 7, 42) and Float (e.g., 0.28431). You can do the usual math on them the way you imagine. But there's also floor division that returns you what's left. Instead of the standard slash '/' for division where 4/2=2, you use '%'. So 4%2=0 and 5%2 = 1.

Floor division is useful to check if a control parameter is odd or even. Or to check if we have finished a cycle. Suppose you have *papers to group*. You want to build stacks of a certain number of papers (user choose it). You want to count how many stacks of X papers you have. A way to do that is to go through the (say 21) papers and every time you can divide the current paper number with a floor of zero (suppose we want stacks of 7) we add 1 to the stack counter.

So we are going 1 to 21. At 7 we get 7%7=0, so stack = 1. At 14 we again have 14%7=0 and stack goes to 2. At 21 we get to 3. (If you want to code that remember the machine starts counting at 0 and that a = 1 means we have *assigned* number 1 to variable 'a'. To check for equivalence we need two '=='.)

While talking about data types, there are also Boolean values. As you can imagine these are True and False. Explore what is truthy and falsy in Python. (You can evaluate expressions like 'X is True'). Do that with IPython or the interpreter.

Moving to data structure we are likely to use *tuples*. They are *immutable* and are created as follows:

- listing comma-separated values: Tuple = 1, 2, 3;
- using parentheses: Tuple2 = ("a", "b", 2, 4). Note tuples can hold different kinds of objects;
- if you want to make a "lonely tuple", i.e. a tuple with a single object, you need to put a parenthesis after it: LoneTup = ("help!",).

Why is that? Write a tuple, like tup = (1, 2). And print it (or just call tup in the interpreter). Now, try to write a = (1) and print a...

Have you seen it? Ask for confirmation. What's the type of a? Yes, int.
Ok, now try reassigning a = (1,). Print a. See the difference? Check for type, now you have the tuple.

Next in line, we have *sets*. Sets are *mutable* collections of items, unordered, not indexed and *without repetitions*. If you need immutable sets for any reason, be sure to check out *frozensets*.

Sets are created with curly brackets, as follows:

Set = {'element1', '2', 'three'}

We can do all the elementary-school set operations we did with Venn-diagrams.

Sets are cool to remove redundancy. Try to write a set with multiple elements, i.e. something like test_set = {1, 1, 1, 2}. Print the test_set. See that? You have a set of len() = 2, i.e. just the two different elements (1 and 2).

Ok, let's try to put some sets in action. Suppose you want to count the common words of two different texts. Assuming the two texts comes as big strings, say, 'Text1' and 'Text2', that's a viable strategy given what we know:

1. *split* the first string - Text1 - into words (i.e. where the whitespace is);
2. *make a set* out of this split;
1. *split* the second string - Text2- into words (i.e. where the whitespace is);
2. *make a set* out the split of the second string;
3. calculate *set union*.

Nice, right?

If you try this experiment you are going to find it has some quirks:

1. when you print sets (set union is a set) items do not follow the order of the sentence. Remember: sets are *unordered*. Print the same set multiple times, you'll have different ordered outputs;
2. if you split using spaces and the text had punctuation, punctuation signs become part of the words;
3. the same word capitalized and not capitalized is not the same word for your machine. **CapITalizaTion MaTTeRs**.

Luckily, you can fix this: strings have a lower() method, remember? That solves (3). Also, strings have a replace() method, so you can replace punctuation signs with... nothing: in that way you are removing them.

Ok, well done, here's the official Python documentation to the built-in data types. It's though but it's better than a cheat sheet: https://docs.python.org/3.8/library/stdtypes.html. (We are saving classes for later.)


## Flow Control

Flow control is where we structure our code. A program is a small(ish) world in which we check various status and, for each status, we have instructions to deal with it. If something happens and we have no idea how to deal with it, the program crushes. (Crushing is a safety feature: a secure and safe crush is better than some unexpected super compromising behavior.)

Checking for every case in our program might seem quite a lot of work, but we are lucky: we can try things and raise exceptions. So we can say "if this happens and we get something unknown, print a message, save that and close everything".

Ok, let's start thinking about *flow control from what we know*. Think about our text editor (RStudio) or our browsing the internet experience. How does the computer know which key I am going to press? How does the browser know where I am going to move the mouse?

Of course the pc is spying on us, but not in the sense how some tenured old persons (maybe those than can't sort the list of students alphabetically) say.

A way a text editor can check what we are doing it having a loop going on for as long as the program is opened that checks for keyboard inputs (among many other things). The browser checks your mouse position, a videogame has a game loop that goes on as long as the game is opened.
This is a **while** loop. If you need a while loop to go on forever, add a condition that is always true (True is an option, 1 > 0 another - philosophers debate analyticity, but analytics statements - if any exist - can help us here).

Conditionals are also good: we want to check if something is the case, if that works something happens. Otherwise (else), we'll account for that.

Then we have other task-specific issues. Like: checking all items in a list and capitalize them. Those are for loops.

And try-except things, like: try to open a webpage, except you get an error saying the page can't be accessed. (We'll use that while retrieving search engine results.)

Ok, so match for an overview. Let's dive in.

### For Loops: Iteration and Unpacking

We have already seen for-loops. For loops are used to iterate on collections and perform an action for all the elements affected by the loop.

The syntax is the following (items in **bold** mark reserved keywords and necessary syntax in terms of columns, newline, and spaces):

1. **for**;
2. indicate a variable for items we want and we are going to manipulate;
3. **in**;
4. name of the container of the items: it can be a list, a dictionary or even a function that returns them, example: the range() functions, which return numbers in a range;
5. **:** (this semicolon is really important, it signals the beginning of the loop block);
6. after a colon you have a **newline**;
7. added level of **indentation**;
8. operations on the items you mentioned in point (2).

Here are some examples:

*For loops examples - ch. 5.7*

```{python eval=FALSE, include=TRUE}

items = ['first item', 'second item', 'third item', 'n item']

for i in items:
    print(i) #i matches the previous i

#same output, different names

for item in items:
    print(item) #the name you use to iterate an object doesn't
    #matter
    
for number in range(20):
    print(number+1) #returns numbers from 1 to 20
    
```

### If you Want to Evaluate Conditionals, Add If

Conditional loops are used to evaluate a condition and branch your code into cases. We have seen it already when we checked if some objects had a specific length.


The syntax is the following (items in **bold** mark reserved keywords and necessary syntax in terms of columns, newline, and spaces):

1. **if**;
2. indicate the item you want to test;
3. provide a condition to be tested;
5. **:** (this colon is important, it marks the beginning of the code of the statement - other languages use parenthesis for that);
6. after a colon you have a **newline**;
7. added level of **indentation**;
8. operations on the item you mentioned in point (2) you want to happen;
8. (what follows here is optional)
9. **newline**;
10. **deindent**;
11. **else**
12. **:**
9. **newline**;
10. **indent**;
11. what should happen if the condition fails.

This is a superverbose way to say: "if a, then x, else y".

You can also use **elif** to *test multiple conditions being true and then execute your code as soon as one fire*.

Note: you can have *only one else condition* (think about it in terms of if a... else (if a is not the case) something else). But you can have multiple elifs. Think about moving a player with the keyboard: the player moves if you press left or if you press right or if you press up... the first key you press makes the player move.

Ok, enough talk. Here are some examples:

*If statements examples - ch. 5.8*

```{python eval=FALSE, include=TRUE}
#check if a number is above threshold

number = int(input('Insert a high enough number'))
#note the int conversion

if number > 10:
    print('Ok, your number is big enough')

#same case, but adding an 'else' which reveals the threshold


number = int(input('Insert a high enough number'))
#note the int conversion

if number > 10:
    print('Ok, your number is big enough')
else:
    print('Sorry, it has to be more than 10')
    
#using elif
#another silly game elif make tiers of ambition possible
number = int(input('Measure your ambition. Enter a number'))

if number <0:
    print('How modest')
elif 0 < number < 10:
    print('Not too much')
elif 11 < number < 100:
    print('Wooo')
elif 101 < number < 9000:
    print('Gulp')
elif number > 9000:
    print('Over 9000!')
#did we cover all the outcomes? Nope!
else:
    print('case not considered')

```

Did you spot which cases were not covered in the last example? In you are in doubt try it out in the interpreter.

### Make Things Last for a While with While (and Remember to Break them)

While loops are used to make it the case that, as long as a condition holds, some operations happen. Suppose you are programming a (poor) spy. The spy only tracks the movements of the target while the target is awake.

As we said, in most of the cases we want to set up on-going enduring activities. That's why we opt for '**while True**' conditions: this will keep on going. In these cases we have to be sure to quit the loop by inserting a 'break' condition. We test this condition with an 'if' statement and this allows us to stay away from infinite loops (which are not good for our pc).

The syntax is the following (items in **bold** mark reserved keywords and necessary syntax in terms of columns, newline and spaces):

1. **while**;
2. indicate a condition that triggers the loop;
5. **:** (the colon is important, it marks the beginning of the code block that pertains to the loop)
6. after a colon you have a **newline**;
7. added level of **indentation**;
7. declare what you want to happen in the condition in point (2) holds;
8. (adding a break statement)
9. **if** [condition] **:** (we already know the syntax of if);
10. (newline indent) **break**

Here are some examples:

*Examples of while loops - ch. 5.9*

```{python eval=FALSE, include=TRUE}

a = 1
b = 10
while a < b:
    print(a) #will go on forever 


a = 1
b = 10
while a < b:
    print(a)
    a = a +1 #now it will stop
    #bonus: calculate the iterations before this stops
    
while True:
    #asks you things forever
    answer = input('Are you happy?')
    #unless you are forced into optimism
    if answer == 'yes':
        break
```


### Prevent Crashes with Try/Except

Sometimes a program is syntactically fine, but unexpected things may occur. For example: we are passing the wrong data type to a function, we end up dividing by zero or we try to access a website that does not exist.

As we already know, when errors happen we want to know exactly what's going on, so that we can promptly fix the code. Most of the errors are re-occurring - think about accessing a webpage that, for some reason, is not displaying - and, for this reason, Python comes with a list of built-in exceptions.

The list has different kinds of possible errors and tells us what happened and when the error is printed. It is good to have a look at that list. Also, it helps when we receive traceback errors: https://docs.python.org/3/library/exceptions.html#bltin-exceptions.

Now that we know about this list of exceptions, we can use it to our advantage. We can now structure our code such that it tries to do something and, given we know we may encounter some error (like the 404 page not found), we are ready to handle an exception. In that way we are able to detect some errors and provide better feedback on what went wrong.

Let's use ValueError as an example. (From the docs: *Raised when an operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError*.) We use ValueError to handle the case in which we ask to enter a number and we receive something else, like a string... With int(string) we have the correct type, because our string (suppose 'hello!' or 'three') is converted to int. Still, 'hello' is the wrong value for an int.

*Try/Except block, nested into a while loop (with break)*

```{python eval=FALSE, include=TRUE}
while True:
     try:
         x = int(input("Please enter a number: "))
         break
     except ValueError:
         print("We said number! Not letters naming a number.")
```


(Later on in our programs we'll touch this by using the raise_for_status() method of the requests library that will check if our webpages exist or not. Requests is using a HTTPError from the urllib, which is part of the standard library -https://docs.python.org/3.2/library/urllib.error.html).

All this flow control (plus passing arguments to function and calling methods) can be learnt visually. Sometimes mapping down the flow of our program is helpful. You can do it by hand, as it's a great exercise. Or you can use tools, such as this: http://www.pythontutor.com/.

## Classes and Comprehensions: More Pythonic Things

It is time to step into two slightly advanced things. The first is classes. Classes are the blueprints of our objects.

Up until now we learnt a bit about data structures and flow controls. With functions we are able to group together pieces of code and make them reusable.

Using a function we can easily compute the area of a rectangle given the sides, rather than having a whole program that asks for one side, ask for the other one, and then computes the area.

To give you a more real-life example, suppose you are working on social media and politics and need to get followers on Instagram for a certain account. It is likely that you are going to first target the account and then do something like: connect to the webpage of the account, make a request for the page, play around with HTML, isolate the follower count you need, get the number. (We are going to do something similar with search engine results later in Part III.)

As soon as you are successful you wonder: what if I can abstract a bit more and make a function out of this program? In that way I can build a list of accounts I want to track for my research and then iterate over them with a for loop. For every account in the list, run the social media tracking function.

As you do that, you'll feel relieved and excited. Your code and efforts start to pay off and, with a few refactoring, you can widely extend your dataset.

Ok, now imagine you want to do more with your data. Maybe you want to store weekly social media data, visualize the follower trends and maybe compare an account to a reference account. You keep adding function definition after function definition... you review flow control to have a better organization of the workflow, but that's not enough.

Wouldn't it be nice to have a further layer of abstraction such that different functions can be grouped together and performed on inside the same big container?
Something similar to what happened with strings and their methods.

After all, if we can replace, strip, lower, etc strings there should be a way to visualize, compare, extract data for an account... and you are right! Classes allow you to do that.

The second thing are *comprehensions*. Norvig had them in his script. Comprehensions are not related with language tests, they are a specific Python feature that allows you to build lists, dictionaries, or set by way of iterating on certain objects. Suppose you want to find out who are the followers of the followers of a certain account.

You want to say something "apply the extract_followers function for all users in account_followers". That's a comprehension statement in a nutshell. Basically we are shortening a for loop. Such a thing is sometimes referred to as "syntactic sugar", a nicer and easier syntactic way to achieve the same result of a more verbose coding practice. Also, comprehensions are considered very *Pythonic*, in fact, they are a specific Python language trademark.

Ok, let's dive in.

### Classes: BluePrints for More

Classes are another way of structuring our data. Think about them as blueprints. You define general instructions in class, then you instantiate them to have the actual objects. If this speaks Plato or Types/token debates, you're welcome.

Programming wise you can think about classes as a way to build a deck of cards.

The card class has some properties: value (Ace to King), color (red or black) and rank suit (Spade, Heart, Clubs, Diamonds).

If you've heard about object oriented programming or have friends working with Java, that's what we are talking about (well, kind of, if you spend some time reading the docs about *Python* classes: https://docs.python.org/3/tutorial/classes.html).

Classes are defined with a served word which, you can guess, is **class**. *Conventionally* class names are Capitalized. This is helpful. When you are using libraries and someone else's code and you import capitalized items chances are that they are Classes. (You have seen that ValueError from our try/except example is capitalized and, if you go through the docs, you find out that exceptions are Classes).

This is a convention, so there is no 100% guarantee it will apply to all the code that you read. Nonetheless, it is precious information because you know that classes come packed with their methods, in form of definitions.
So now we move to creating a Class and adding some methods.

Ok, let's get back to the social media account analyzer sketched above.

The first thing is to initialize our class, which is a complex way to say we have to specify the attributes we want our objects to have. Here there are two odd looking items:

1. classes are initialized with a "dunder init" function (i.e., with this double underscore init: \_\_init\_\_). The double underscores are somehow intimidating;
2. when we initialize a class, we need to tell the class what we are talking about the class itself. So we are passing **self** as an argument to init. This looks less nice than the example we have seen before.

Anyway, here's a class.

*Initializing a class*

```{python eval=FALSE, include=TRUE}
class SocialMediaAccount:

    #initialization
    def __init__(self, name, category):
        self.name = name
        self.category = category

```

When we are calling an instance of a SocialMediaAccount the init function is going to construct SocialMediaAccount that has will take as a name the name we type ('Bolt') and as a category the category we specify ('Athlete').

Basically with the init method we are passing the arguments to the class instance itself. If now we want to create an object for the singer Imogen Heap, we just need to have call the constructor with the different parameters: SocialMediaAccount('Imogen Heap', 'singer').

Remember that, to construct these objects we need to instantiate class objects we need to assign them. So, if you want to have the two accounts you can do like that.

*Constructing objects out of classes - ch. 5.10*

```{python eval=FALSE, include=TRUE}
class SocialMediaAccount:

    #initialization
    def __init__(self, name, category):
        self.name = name
        self.category = category
        

#initialize the Trump object
account_trump = SocialMediaAccount('Trump', 'politician')

#initialize the Imogen object
account_imogen = SocialMediaAccount('Imogen Heap', 'singer')

#test that account_imogen.name shoows 'Imogen Heap'

```


This is cool, but is not going to help. Now we can add methods to a class (instance method). So we can add a method that, given an Instagram url or name, it delivers us the followers. We rewrite our class as follows.

*Adding an instance method to a class*

```{python eval=FALSE, include=TRUE}
class SocialMediaAccount:

    #initialization
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    def insta_follower(self, url):
        #insert processing function
        #we are not providing this here
        return instagramfollowers
        

#initialize the Trump object
account_trump = SocialMediaAccount('Trump', 'politician')
#call the method that gives us the follower
account_trump.insta_follower('http://instatrump')

```

I am sorry not to give the whole Trump Analytics kit, but we were interested in seeing an approach to classes. I thought it was better than having a tutorial with barking dogs or playing cards.^[The latter is quite a good exercise. If you want to explore more about objects and classes have a look at Java and the Head first book mentioned a while ago at the beginning of the chapter. Also try to read some of *Design Patterns: Elements of Reusable Object-Oriented Software* by Gamma, E., Helm, R., Johnson, R. e Vlissides, J. (known collectively as the 'Gang of Four'). While the book is Java-based it will show you what you can do with classes *in real life*.]

Getting back to the analytics projects, there is something worth discussing to persuade you to go into the project. First, data structure-wise, our class has a pair of values: do you remember a data structure that does its best in saving key value pairs?

Still, if we develop the project, we may end up adding methods that target different urls for different social media. Why track only Instagram when we have Twitter as well?

This is an issue. Different social media requires different functions, which is fine. Nonetheless, different social media are hosted at different urls. Some users have the same alias across platforms, some don't. So we need to find a way to store a list of social urls. A dictionary with dictionaries? Something else? That's up to you.

Or, to simplify the functions, we may encode all these data in the init of the class. If we are lucky, we can store only the 'social_id', if that's consistent. When we call the twitter function there would be no need to add an url. We can find out to construct it with some form 'Twitter' + 'social_id'.

Otherwise we store all the social urls. Below is a mock implementation of this latter scenario.

*Class-based mock Social Media Analyzer*

```{python eval=FALSE, include=TRUE}
class SocialMediaAccount:

    #initialization
    def __init__(self, name, category, instaurl, twitterurl):
        self.name = name
        self.category = category
        self.instaurl = instaurl
        self.twitterurl = twitterurl
        
    def insta_follower(self):
        #insert processing function
        #we are not providing this here
        instagramfollowers = extract(instaurl)
        return instagramfollowers
    
    def tw_follower(self):
        #insert processing function
        #we are not providing this here
        twfollowers = extract(twitterurl)
        return twfollowers
        

#initialize the Trump object
account_trump = SocialMediaAccount('Trump', 'politician', \
'instaTrump', 'twitterTrump')
#call the method that gives us the follower
account_trump.insta_follower() #no need to specify the url
#that's already in the class
account_trump.tw_follower() #no need to specify the url
#that's already in the class

```

```{python eval=FALSE, include=TRUE}
```

```{python eval=FALSE, include=TRUE}
```



### Comprehension

Python allows us to write comprehension. On the one hand, comprehensions are great, compact and Pythonic. On the other hand, comprehensions can look a bit esoteric at first.

We can think about comprehensions as ways to shorten a for loop. We can generate a list of output that is the result of performing some operations on a set of items (e.g. items in a list).

A general template for this is:

*Well-known for loop (written in a non-Pythonic way)*

```{python eval=FALSE, include=TRUE}

items = ['first item', 'second item', 'third item', 'n item']

#initialize output
output = []

for item in items:
  operation = item + item
  output.append(operation)

```

You can squeeze all this in this one-liner using comprehensions (bold is for the comprehension):

*A list comprehension*

```{python eval=FALSE, include=TRUE}
#comprehension begins with [] telling it produces a list
#that's list comprehension
#first we say what we want as an outcome, i.e. specify the
#process to be followed
#then we define for which items
output = [item + item for item in items]
```

(What should you add to the code above to be able to run it and see the output displayed?)

The pattern for the comprehensions is that of **output = operation you want to perform for items that are in a certain container**.
The code above is equivalent to the more explicit for loop.

We can rephrase this a bit further. In fact, item + item is not the best example of an operation to perform on items. Suppose you have a dedicated function you want to run on some arguments. The comprehension looks like the following:

*(List) comprehension passing arguments to function - ch. 5.11*

```{python eval=FALSE, include=TRUE}
def yourfunction(x):
  print(x)
  print(x*x)
  
output = [yourfunction(item) for item in items]
```

This is equivalent to the way longer:

*Function and for loop (not-Pythonic)*

```{python eval=FALSE, include=TRUE}
def yourfunction(x):
  print(x)
  print(x*x)

output = []
for item in items:
  output.append(yourfunction(item))

```

The best way to get proficient with comprehension is by practicing them.
You are welcomed to turn previously used for loops into comprehensions.

Now try to write comprehensions and for loops for the following cases:

- check that all the elements you scraped from a website matches a certain pattern;
- check all the lines of a text and ensure that there are no cases of double spaces, if a double space occurs, correct it to a single space;

You can extend comprehensions to sets, by turning the square brackets of a list into curly brackets.

You can also use comprehensions in dictionaries and sets. Explore these yourself, maybe squeezing some of the above dictionary-related tools into comprehensions.

### More Comprehensions

Comprehensions extends to sets and dictionaries. For dictionaries we need curly brackets and a colon. We define our pair of **key: value** and then use the comprehension syntax *for key, value in container_of_keys_and_values*.

The best example is this nice comprehension to swap keys and values which I've kept you waiting for way too long.

*Swapping dictionaries comprehension*

```{python eval=FALSE, include=TRUE}
a_dict = {'a': 1, 'b': 2, 'c': 3}
{value:key for key, value in a_dict.items()}

#prints {1: 'a', 2: 'b', 3: 'c'}
```




## Functions Revisited: \*Args Times!

There are more things we can do with functions like using passing one function into another one. This looks a lot like first you solve (1+2) in the parenthesis and then multiply by 3, as in this old elementary school expression: (1+2)*3.

The difference is that this time we can define all sorts of functions, we are not restricted to maths and fractions. (And we have to keep track of data types and data structured so that all the functions can be plumbed together producing the result we have in mind.)

So we go back to our shout function but this time we pass it a function to a different function, namely one that repeats the input.

*Passing functions - ch. 5.12*

```{python eval=FALSE, include=TRUE}

def shout(word):
    return word.upper()

def repeat(word):
    return word + ' ' + word

#want to 'Say what?' screaming twice?
if __name__ == '__main__':
    print(repeat(shout('Say what?')))
```

Ok, we can successfully take something that is produced by a function and input it somewhere else. Cool.

What if we need some default value, i.e. something to be used as a value should you not assign anything to the function?

We can do this by adding the default value we want after the argument of the function, adding = 'default value'. Let's apply a default argument to our shout function.

*Default values in action*

```{python eval=FALSE, include=TRUE}

def shout(word = 'this capitalizes stuff'):
    return word.upper()
    
shout() #returns THIS CAPITALIIZES STUFF
shout('let it all out!') #returns LET IT ALL OUT!
    
```

What if we want to pass more than one value to our repeat function? Welcome \*args.

We can define functions that take an arbitrary number of arg(ument)s. The issue is that \*args provides us with arguments **as a tuple** (that's why we have to cover them). We then need to find ways to unpack the arguments in this tuple.

Suppose you want to repeat more than one word at a time.
This will throw an error: we can't concatenate tuples!

*Error is coming...*

```{python eval=FALSE, include=TRUE}
def repeat(*words):
    return words + ' ' + words #if you type word you
    #have error of unknown variable
    #we want the word in words, but 'word' is not
    #in our current code.
```

To fix this we want to extract single words from the items in the tuple. A list comprehension comes to rescue us. It provides us string items (the items in the list) and it allows us to unpack the tuple.

Basically we are saying "repeat each word that is supplied in the \*words field". There it is below.

*Unpacking with comprehensions*

```{python eval=FALSE, include=TRUE}

def repeat(*words):
    return [word + ' ' + word for word in words]

```

We can give our functions even more stuff. Sometimes you have functions with options or default messages.

For your Python explorative pleasures we have to say there are also \*\*kwargs, i.e. **k**ey**w**ords **arg**ument**s**. Kwargs accept positional or named arguments which, given what we know from the data structures section above, we can identify as dictionaries.


## What's In a Name: Naming Conventions and Styles

Ok, our tour into Python is almost over, at least to get us started. We have already seen quite a lot on the way: from spell checkers to basic tools for textual analysis. We've also sketched classes to analyze social media!

It is time to enumerate some naming conventions and style guidelines, listing things that we said explicitly or saw in action in the example.

Names tells you a lot in programming: 

- **ClassesHaveCapitalLetters**: when naming classes, we use capitalization to signal that;
- **CONSTANTS_ARE_ALL_CAPS**: sometimes programs have a parameter. Suppose you have a fixed view of items per page, that's a constant value in the whole program. Or suppose you are using lifes at the start of a game or gravity, speed, max number of opened windows, etc. When you encode constants, they go all capitalized, so that you can easily spot them;
- you can't use reserved words in your naming variables: no 'in', 'is', 'for', 'list' or other. You can escape problems with 'list' going for 'list_'. But maybe it is better to use a more informative name for your list;
- spaces are not allowed in variable names: this leads us to choose between CamelCase vs. snake_case. This depends on the codebase.
- leading underscores (like '\_this') are conventionally for throw-away variables: suppose you are in need to have a dummy variable to use just once. You need it to perform a calculation or to filter some data. Put an underscore in front of it and name it. Conventionally who reads your code will know that the '\_x' is not going to last for long.


## Saving and Running a Python Program: .py and .pyw

We know how to run our code in the editor, but what about saving our precious experiments?

You've probably already saved some code from Spyder as .py, i.e. the standard python extension. It is good to know that there's also the .pyw ending. The difference is that, in the case of .pyw we are running the file without opening the interpreter. (Which makes it perfect if you want to run a program or a tool in the background, as a *daemon*, as they say in geek speak.)

In fact, if you try to double click on a .py file, your system will try to execute the code and *not* to open it in the editor. (If you want to edit a .py file you right-click it and open with python's IDLE or open it in your editor of choice).

When you run a Python file, an interpreter session is opened as well for you to get feedback on what happened. This helps if your program is outputting something or if an error occurs. In fact, in the interpreter you'll see the error's traceback. Learn to read traceback errors, they are the quickest way to fix the code.

If you want to package your file for a friend to use it, you need to research a bit on the topic of *freezing code*. On windows, you would like to have a .exe file for your friends to click on. And your wonderful PDF magic tool will be there for them to use.

Unfortunately, that's not the case. The easier solution is that you:

- lure your friends into Python. Then they'll have access to your tool on Anaconda or similar;
- find a web-based environment to have your tool available. Try Colab or Jupyter Notebooks (which needs Python installed nonetheless);
- tell them about this book :).

## Working with Files

Ok, we know quite a bit of Python. We now need to move onto files. File operations are necessary to open files in order to read data from them, saving data to files, etc. We can't have self writing papers if we cannot create or read (text) files!

### File Types: Text and Data


In Python we can deal with Python as text objects or as bytes objects. We most of the time use the "ordinary" text files, but we'll also use binaries when dealing with pdf later.

These two types are easily distinguished:

- **text file**: ordinary file, you can open them with any text editor;
- **binary files**: specific data files, with a specific encoding (.xls, .pdf - even if they have text, .bmp, .jpeg, .mp3).

When dealing with file modes, Python defaults to text files. If you want to work in binary mode you have to specify that adding an **-b** flag at the end.

### File Modes: What Do you Want to Do with Files?

You may want to do different things with your file, both text files and binary files. Depending on what you want to do you choose the appropriate mode by specifying a flag.

The **file modes** are the following:

- 'r': Read mode. This is how you access the information. You have to think about it as *read only*. You can't alter the content. If you want read mode for binaries, the flag is 'rb';
- 'w': write mode. This is how you can modify a file. Modify includes **creating** it. This may be counter intuitive. Try thinking about this as "writing a file for the first time". Also, when we write a file we are starting all over again. So if you have two lines to write on a file and you call the file in write mode to write line 1, then you call again the file and write line 2 *you'll see only line 2*. Calling write mode for the second time will let you restart the writing process. To work in write mode with binaries use 'wb'. If you want to keep writing on the same file (think "turning the pages of a book, rather than restarting on the first page every time"), we need the append mode;
- 'a': append mode. This is what you need to append (i.e. *add*) information at the end of a file (think "keep turning the pages of the book, instead of buying a new one and read page one again. Then repeating this whole buy-read page one business"). This is what you should use to add content to a file line after line. Again, to work with binaries change the flag to 'ab';
- 'r+': Read and Write mode. This allows you to read from a file *and* write to it. Writing works as 'w', so erasing the old content. To have this work in binary mode, we keep adding the -'b' flag at the end: 'r+b';
- 'a+': Append and Read mode. This allows you to read from the file *and* append to it. To work with binary files use 'a+b';
- 'x': creation mode. This is used to create a file and only for that (should you need that specific option). The binary version is 'xb'.
 
### Opening and Writing to File

To open a file we need to assign it to some object and then call **open('filename', 'filemode')**.

Files have to be closed when you are done with them (think of this as clicking the X on a program window). This helps in managing resources. We close files with the close() method.

Putting this all together:

*Open and close a file (file dentist)*

```{python eval=FALSE, include=TRUE}
#open file, be sure it's in the working directory
file_object = open('yourfile.txt', 'r')
#close the file
file_object.close()

```

This looks tedious. There's a lot of things we have to do while programming and we *may* forget to close the file at the right time. But we can ensure that it is done for us by the computer. We need to use a *with* statement.

By using with statements we can assign certain operations a specific name as an alias and perform operations on that. As we exit the with statement, that acts as a container for the operations, all files are closed.

Here is how to read from a file - you guess it, with **read()** using a with statement:

*Reading a file with a with statement*

```{python eval=FALSE, include=TRUE}
#open file, be sure it's in the working directory

with open('yourfile.txt', 'r') as dataobject:
    a = dataobject.read()
    #do something with that
    
#ok, move to something else

```

Cool, we can open and read files efficiently. But how do we create a new file?

Either we use the x mode or, whenever we open a file with w or a mode a file is created. So, to create a file called 'result.txt' we can do the following:

*Creating a new file*

```{python eval=FALSE, include=TRUE}
#open file, be sure it's in the working directory

newfile = open('result.txt', 'a')
#or

newfile = open('result.txt', 'w')
#or

with open('result.txt', 'a') as file:
    #do something with that file
    

```

Ok, now it is time to write some lines into the file. This works a lot like appending content to a list: we first ensure our list/file is there, then we specify what to add to the file/list.

In case of a file there is an extra condition to verify: the file needs to be opened and we need to open the file in a way that allows us to write on it.

Let's demonstrate how to create a with our 'dataresults' using a with statement and writing some lines of results.

*Create a file and write in it - ch. 5.13*

```{python eval=FALSE, include=TRUE}
#create the file
with open('dataresults.txt', 'a') as file:
    file.write('These are the results of our experiment')
    file.write('\n') #add new line
    file.write('Account X has N followers on social Z')
    file.write('\n')
```

This is just a template. You can add the newline at the end of the line and not as a dedicated write statement. Also, you can have the X, N and Z as arguments that you pass to a certain function. In that way have your function or class to be able to write its own data.^[With statements have their own pep: https://www.python.org/dev/peps/pep-0343/. ]

### Matching Files with a Certain Ending, System Paths, and Working Directory

There's another operation that you may want to do.

Chances are that, when running programs, you are going to iterate on folders and do things to specific files. The good news is that the **os module** (you guessed it: operative system) allows you to run most of command lines operation like dir in Python.

Suppose you want to merge all your pdfs in a certain folder. You need to find out all the pdfs there. That's easy. You need all the files in the directory ending with pdf.

You can check file endings with the .endswith() method. All you are missing how to perform the equivalent of CLI 'dir' command. The os module has what you need. The method is: **os.listdir()**.

From the docs we learn that the function *Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries '.' and '..' even if they are present in the directory.*

Suppose you want to collect all the pdfs in a folder. You just need to find them and append them to a list called mypdfs (for example). Then you can run operations on them.

The files you want to operate with must be available to your Python session. If you operate on files and call functions like open('myfile.txt', 'r') Python assumes the file is available in the current working directory. If the file is not in the current directory, you get an error. To find out what your current working directory is we can use the os module again. The method is: **os.getcwd()**.

You can change your working directory with **os.chdir('path/of/new/directory')**.

If you want to operate on file outside the current directory you can access them providing the full path, taking due care of proper formatting of your string. Here are the docs to be a path manipulation master: https://docs.python.org/3/library/os.path.html.


## Regular Expressions


Regular expressions (or 'regex' or even 'regexp') are a powerful tool to search and modify text. The idea is pretty simple: with a regular expression you assemble some specific LEGO bricks that stand for different elements (characters, digits, punctuation, repetitions) to form a pattern. Then you use this patter against an input and retrieve the matches.

You are given multiple options on where and how to match: at the beginning of a line, parsing each word, inside a word, etc. You can retrieve segments of what you match using *capturing groups*, which we'll use in a while, and choose to perform specific operations with your matches, like changing all the matched '\\' to '/' or the other way around.

In a [famous piece advocating regex knowledge](https://www.theguardian.com/technology/2012/dec/04/ict-teach-kids-regular-expressions), **Corey Doctorow** writes: 

>>>"Regular expressions are part of the fundamental makeup of modern software. They are present, in some form or another, in every modern operating system. Word processors, search-engines, blogging programs … though it's been decades since software for everyday people was designed with the assumption that users would know regexps, they still lurk in practically every environment we use".

We'll perform our regex workout in *Python* and we'll e*xtract bibliographic data from academic papers*. If you are eager to get started skip the following short historic section.

### Regex Notable Features

Regular expressions were conceived by Kleene - yes, that Kleene you know from logic^[This one https://en.wikipedia.org/wiki/Stephen_Cole_Kleene.] - early in '50 when he described regular languages.[See https://en.wikipedia.org/wiki/Regular_language for a quick intro.] Later on, they were implemented Unix text processing utilities. All advanced nerdy text editors (Vim, Vi, Grep, sed, AWK, and co) have them.

Doctorow's piece inviting the school system to teach regex to the kids (read that here: https://www.theguardian.com/technology/2012/dec/04/ict-teach-kids-regular-expressions) has already been mentioned. What wasn't mentioned is one of the best paragraphs to motivate some research in Digital Humanities and building technical literacy:

>>> "Much of the world you interact with, from cash machines to your bank's website to the website where you sign on for disability benefits to the alarm clock that wakes you in the morning to the phone that tracks your location, social network, and personal thoughts, are underpinned by software. At the very least, a cursory understanding of the working of software will help you judge the reliability, quality, and utility of the software in your life".


### Matching Expressions

Regular Expressions are a small(ish) language on their own. You have short symbols that stand for something else. We use this regex LEGO to build a pattern. Then we are going to match the pattern against a given text. (There are different flavors and different implementation of them, as it's often the case).

Regular expressions are at first hard on the eyes, but all you need [is just a little patience, as Axel said](https://www.youtube.com/watch?v=ErvgV4P6Fzc). Most of the LEGO bricks start with a \\ followed by something.

Most of our LEGO bricks are two characters set. Here are some of the most used:

- do you want to match any *digit*, i.e. a number going from 0 to 9? Use **\\d**
- do you want to define a *customized class of ranges* to be matched? Use square brackets and put the range limits inside, separated by a dash (-). For example: if you want to match numbers from 1 to 7 go for **[1-7]**. If you want to match any digit and don't like the \\d syntax we have used above, go for [0-9]
- if you want to match any character, use the dot **.**
- if you want to match one or more occurrences of a certain pattern use the star **\* **
- if you want a certain component to be optional, add a **?** after the component. This is a quantifier meaning "zero or one occurrence"
- if you want to match a space, use **\\s**
- parentheses '**(**' *are a symbol of the language*, in fact, they define *capturing group* - see later. If you want to match a parenthesis you have to use regex escape character, i.e. \\
- if you want to match whatever is not a white-space you can use **\\S** (in that way you will catch Capitalized and lower letter, digits and punctuation)
- if you want to match a word character use **\\w** (word characters include letters Capitalized and not capitalized *and* digits *and* the underscore character)

## Learn by Doing for the Humanities: Matching Bibliographical Patterns

Our task is that of identifying the bibliographic data in a paper. We assume the paper is given as text input. Our task is to develop regexes for the different styles of bibliography, in particular:

- Author (Date);
- (Author, Date);
- (Author Date);
- fulldata: which, more or less, has the following form: "Author separator title separator publication separator date".

We want to be able to match these different styles and we aim at a standardization of these inputs. For each of these we'll extract Author and Date. We'll need capturing groups for that.

### Capturing Groups

We want to standardize the references we find in different styles to something simpler and common, like Author Date. No fancy parentheses or similar. This standardization can then be used to make some analysis on most quoted or influencing paper or whatever you want.

We need to detach some information so that we can compare the bibliographies across different journals employing different styles.

To produce that standardization we can use **capturing groups**. They are groups that allow us to retrieve just a part of what we matched (here: Author and Date). To add a capturing group to a regular expression all we need is to delimit the group by using brackets. In Python, the groups are accessed as items in a list.

Suppose we have a regular expression like **regexbookchicago** that captures books under the Chicago style. If we single out two capturing groups from that, we can access them as list[0] and list[1] a code example may help.

*Regex and capturing groups template*

```{python eval=FALSE, include=TRUE}
import re
#mock regex matching chicago style
regexbookchicago = '(authorpart) title (date part)'
text = 'Some text with Chicago style references'
#store a list of lists of all our matches
match_pattern_to_text = re.findall(regexbookchicago, text)
for match in match_pattern_to_text:
    print('Match found: ', match_pattern_to_text[0] + ' ',
    match_pattern_to_text[1])
```



### Matching Author (date)

Let's start with matching Author (date). Our basic task is to build regex-LEGO bricks to match Author and date. A date is pretty easy, it's just a block of 4 digits (we are ignoring referencing stuff 3 digits, like Giustiniano 529; or dealing with 2003a or similar).

A date is nothing but something like this:

*Date as regex*

```{python eval=FALSE, include=TRUE}
import re
dateregex = '\d\d\d\d'
```

We develop this adding a sample test that features textual elements. We are going to match dates in this test and then print the result.

*Regex data test - ch. 5.14*

```{python eval=FALSE, include=TRUE}
import re

dateregex = '\d\d\d\d'
sampletext = ('The biggest contribution to the field is due to '
    'Master (2001) and its impac cannot be denied')
match = re.findall(dateregex,sampletext)
print(match)
```

Run this and see we are catching '2001'.

Now we need to add author with is nothing but a surname, i.e. a Capitalized letter followed by some non capitalized letters. To catch the author we basically want a capital letter in the range [A-Z] followed by any number of letters in [a-z] range.

A first implementation would be:

author1 = '[A-Z][a-z]*'

Note that this is not the same as

author2 = '[a-zA-Z]\*'.

In fact author1 requires a Capitalized letter in at the beginning of the match; author2 does not. It will match continuos strings of capitalized and non capitalized letters, included tHisOneHere. (Note that author2 if written as '[A-Za-z]\*' may result into errors on some compilers online.)

You can also implement the author as

author3 = '\\S\*' solving the capitalization issue. Beware that here you will also get all the words into the text punctuation included.

To exclude the punctuation go for:

author4 = '\\w\*'.

The code template below allows you to play around and understand the various ways to catch the author. Substitute the different author expressions above into the authorregex variable and try to match Master **only**.

*A regex matching more than we wanted to - ch. 5.15*

```{python eval=FALSE, include=TRUE}
import re

authorregex = 'INSERT ONE OF THE AUTHOR REGEXES ABOVE'
sampletext = ('The biggest contribution is Master (2001).'
    'Its impact cannot be denied, on pain of miSbeHaving.')
match = re.findall(authorregex,sampletext)
print(match)
```

As you could see, we are overmatching our text. Depending on the expression used we are going to get whatever starts with a capitalization ('The', 'Its') and more.

**Don't panic, we are on the right track**. We need to connect the two elements we have identified. What's linking them together in a unique way?

First, parentheses are around the date, so we have to add them to the date (remember to escape them). Then, there's the space in between.
The resulting code is below. I've opted for '[A-Z][a-z]*' to match the Author as it is easier to see what we are asking to match.

*Matching author date regex*

```{python eval=FALSE, include=TRUE}
import re
authordateregex = '[A-Z][a-z]*\s\(\d\d\d\d\)'
sampletext = ('The biggest contribution is Master (2001).'
    'Its impact cannot be denied, on pain of miSbeHaving.')
match = re.findall(authordateregex,sampletext)
print(match)
```

Run this and be happy, we are getting the 'Master (2001)'.

Now it's time to isolate the elements with capturing groups. We want to isolate author and date, without the parenthesis. See if you can match the two groups adding parentheses.

Here's where to put them:

*Regexes and capturing groups - ch. 5.16*

```{python eval=FALSE, include=TRUE}
import re
capturingauthordate = '([A-Z][a-z]*)\s\((\d\d\d\d)\)'
sampletext = ('The biggest contribution is Master (2001).'
    'Its impact cannot be denied, on pain of miSbeHaving.')
capturingmatch = re.findall(capturingauthordate,sampletext)
for item in capturingmatch:
    print(item[0] + ' ' + item[1])
```



### Matching (Author date) and (Author, date)

Things start getting nasty here. First, we have to choose if you want the same regex to perform both matches or not. It seems that the second expression (Author, date) is nothing but the first (Author date) with an added comma. That's a tasty opportunity to use optional matching (zero or one quantifier above, i.e. '?').

Still, if we go down that path we had to be aware that not all the equivalent author options we saw above are still valid. In fact, if we match the author with '\\S' we are going to catch the comma after author in (Author, date) as part of the author name. So it will be in the author capturing group.

The nice part about this expression is that whatever we need to capture is between the parenthesis, so there's no need to match the two parts and then find a way to join them.

Here's the code to match the expression, with the optional parenthesis.
Our new regex is called *capturingparenthesis* and the sample text now includes (Author date) and (Author, date).

*Multi matching with optional comma*

```{python eval=FALSE, include=TRUE}
import re
capturingparenthesis = '\(([A-Z][a-z]*),?\s(\d\d\d\d)\)'
sampletext = ('The biggest contribution to the field is due to '
    '(Master 2001). Nonetheless, (Slave, 2002) is probably a more '
    'accessible version of these ideas.')
capturingmatch = re.findall(capturingparenthesis,sampletext)

for item in capturingmatch:
    print(item[0] + ' ' + item[1])
```



### Fulldata

Fulldata is the worst part of our mission. Not only the style varies across the different items (article, journals, etc.); often you won't get a bibliography at the end to have a simplified tool to check for accuracy.

The bad feature for us is that the information we care about are far away from each other. Author is somewhere at the beginning but the date is at the end, surrounded by a ridiculous amount of stuff like title, editors of volumes, issues of the journal, journal names, etc. Every element adds more complexity to our guessing and singling out a scheme.

Think hard and try to find a solution. Here's an attempt:

*Regex for fulldata, an attempt*

```{python eval=FALSE, include=TRUE}

import re
fulldatatextsample = ('Murphy, "Was Hobbes a Legal Positivist?," 
    'Ethics (1995)')
regexfulldata= '([A-Z][a-z]*),\s"[A-Za-z\s?,"]*\((\d\d\d\d)\)'

```


What is doing the heavy lifting here is the following term:

**"[A-Za-z\\s?,"]**



In fact, we know how to catch the name and the year, the hard part is that of getting the re modular part of the title. The title of the work is going to include letters (both capitalized and not capitalized) and spaces, as a title is often composed of more words. We also need to catch special delimiter, like double-quotes.

Note that this will catch also the name of the journal. In fact, we don't know how many words are going to be in the title. The rest of the implementation of the script is the same as before, so you can use it 

### Limitations, Open Issues and Regex Building Tips

There are several issues with our first attempts. In fact, right now we can't get titles that include parenthesis. We can't include numbers.
A better attempt would be to parse the fulldata string as:

1. author;
2. title;
3. journal/book/whatever;
4. year.

We need to use proper separator matching the style of the journal.


We only scratched the surface but nonetheless showed that we have a powerful tool here. Some of the limitations are:

- we are not capturing a, b, c in the date: how can we handle that?
- we are not considering two parts surnames like von Fintel, von Wright, van der Torre, De Re, De Seh, etc. And what about De Las Casas? (You may say that's not an issue as we are going to get the last surname)
- sometimes we have multiple quotations from the same author, like Master (2001, 2002, 2003, 2004) (No, that's not a sample of Federer's Wimbledon series). How can we cope with that?
- Author (date) is cool, but it can get worse. Our implementation fails to get Master (2001, 2002) as well as Master (2001: 112-121). Is there a way around that?
- What about coauthored papers? We are to work on 'Author & Author' and also 'Author et al.'.



I find it useful to build the regular expression piece by piece. So, in this case, I try to isolate the author and the date. This helps to see how your regex may fail, like matching any capitalized word in addition to the Surname of the Author. If something more complex is needed, like in the case of better implementing the fulldata case, you can try going the other way around: first, you match most of the string and then try to reduce what you matched.


## Summary

We've seen quite a lot of things here. This is probably the most dense chapter so far. It covered both basics and ways to use them. Most of the interesting ways to use the basics were merely described and not implemented. Come back here and try to realize these programs after you have more experience (e.g., after going through part III).

We also start working on more applied research-based stuff exploring regular expressions.

### Programming Concepts, Methods and Functions Recap

We have gone through the following functions and methods. Make sure they make sense to you:

- input()
- type()
- int()
- str()
- set
- string_slice[beginning_included:end_notincluded:step]
- string.upper()
- string.lower()
- string.capitalize()
- string.split("separator")
- string.replace("selection","replacement")
- len()
- list.append("item to add")
- list()
- range(beginning_included:end_notincluded:step)
- dictionary.get()
- dictionary.values()
- dictionary.items()
- floor division %
- try ... except
- if (elif) (else)
- for in
- while
- comprehensions
- defining functions and classes (what are init and self?)
- os.getcwd()
- os.listdir()
- os.path

### Re module (useful regex Commands)


- re.match() beginning of the string
- re.search() any position in the string
- re.findall() all matches in the whole document (non-overlapping matches)
- re.finditer(): all matches in the whole document (overlaps included)
- re.sub(): replace goes regex

needs a comparison between findall and finditer



### More Resources


Of course you want to know more about code specifications. Python Enhancement Proposal 8 (PEP 8 in jargon - https://www.python.org/dev/peps/pep-0008/) is where the format standards are defined. 


Resources on Python abound. Let's start from free resources:

- python's official tutorial is great https://docs.python.org/3/tutorial/. Be sure to check out parts 10 and 11 on the standard library. Part 12 about virtual environment (you've seen them already) and also part 9 on classes if you want more details on them;

- IPython's tutorial is great as well https://ipython.readthedocs.io/en/stable/interactive/ but a bit less beginner-friendly. It is closer to a documentation page than a step by step tutorial. Check the introducing IPython section, the "IPython as a system shell" section (now you know command lines) and the "IPython Tips & Tricks" as well as the "Built-in magic commands". Come back to this quite often.

- If you feel I let you down with dictionaries, here's a nice visual introduction https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/

- Here's a training on dictionaries and the various retrieving techniques we previously only mentioned. In the training you analyze craft beers. *HumanDemia* says *cheers*! https://www.dataquest.io/blog/python-dictionary-tutorial/

- The LearnXinYminutes website is great to skim over / learn / review essentials. Here's what we've seen and more on Python: https://learnxinyminutes.com/docs/python/.

- A more comprehensive treatment of errors can be found in the Python docs: https://docs.python.org/3/tutorial/errors.html

- If you need some motivation and/or perspective on what we are doing, this piece on profession and trade, have a look here: https://medium.com/@christianalexanderbonilla/theprogramming-toolkit-wheres-my-screwdriver-rb-8913473eab4.

Time to move to books:

- Mark Pilgrim's *Dive into Python 3* is free: https://diveintopython3.problemsolving.io/. (Harry J.W. Percival - an author you'll see mentioned in the next chapter, obey the testing goat! - mentions this, together with *Invent Your Own Computer Games with Python* by Al Seigwart and *Learn Python the Hard Way* as the book he used to learn Python).


Moving to paid ones:

- Joel Grus's *Data Science from Scratch. First Principles with Python* chs. 4 and 9 have, respectively, a super concise and practical Python crash course and then a crash course on file operations. The rest of the book is also great. (Joel starts with the Zen of Python and venvs, then whitespaces, functions and data structures.)
- Al Seigwart's *Automate the Boring Stuff with Python* is a super gently introduction to Python basics *while* helping you construct your Python programs that have a purpose and, hopefully, will save you some time.
- Wes McKinney's *Python for Data Analysis* ch. 3 has a nice introduction to IPython.

### Further Work

There's quite a lot we can do here:

- remember the print() function you looked for in quest for its documentation? What's standard for you learning Python form Python 3.x wasn't standard in Python 2.x. Unfold this story.

- every .py file can be imported as a module, *included your own programs*. Try to look for more. (Hint: 'namespace' is a concept that can get you there.)

**Dictionaries**

40 dictionary related exercises (with clickable solutions): https://www.w3resource.com/python-exercises/dictionary/


**Regex Programs and Exercises**

- [ ] add a / to \\ and the other way around converter;
- [ ] develop date to match also 2003a or similar;
- [ ] write your program to capture internal references in a text. These references could be cross-references to sections or chapters in a book or references to articles and laws in a legal corpus or even more.

A hard one: **From a Feature to an App?**

Now you have the basic concepts, if you want to build an app out of this, consider the following *user stories*, i.e. tech industry way to mean 'features of the program/app'.

If this sounds weird remember that the things you do as a programmer are supposed to have people using it and interacting with it.
When was the last time you thought about who was going to interact with your paper, project, or talk slides as an Academic in the Humanities?

User stories:

- user is able to input text;
- user selects the biblio styles that are relevant for the paper;
- the output is stored somewhere.


