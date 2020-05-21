# Moving Forward: From Beginner to Pythonista {#ch6}

'Congrats for mastering Python syntax,' says the *HumanDemia* welcome screen. 'You are probably already playing out with your newly hardly-acquired knowledge. Enjoy this phase.'

You think they are kinda joking. But what you read next is interesting.^[Bonus points for reading this in GeoHot's accent. If the note makes no sense, use your search engine and happy learning.] "Chances are that you'll move from euphoria and god-mode to depression as the most complex things you'd like to build returns errors or foolish stuff. Or as you figure out that something that should be so conceptually simple to achieve is a pain to be implemented. Fear not, this chapter is there to mitigate this."

Ok, the table of content has something about sources of perplexities in Python, something mysterious about reading the documents and then tips to take tutorials. It looks like a piece of cake.

"I wonder where I'll be thrown the curved balls, here" you think a bit too loud.


## Introduction: Five Sources of Mystery


It's (relatively) easy to get started with Python (as you've seen already).
Still, after setting up your environment and learn the syntax, there are some hurdles and mysterious mechanics of Python that are hard to face as a beginner and that pro-coders can't recognize as such. The more you investigate and talk with people, the more it seems that either you are a programmer or a beginner: there's no in between. Further, once you level up your skills it is difficult to go back to when you failed to grasp basic concepts. (Remember when you tried to add things to a list *without* having the list initialized? And now it's *obvious* you can't do that? It's more or less that feeling.)

It seems once you enter a new mindset you can't go back to when you used to struggle. 
The difficulty in bridging the gap from "I know Syntax" to actually be able to code might be compared to knowing grammar and actually speaking or knowing that the Lydian mode has a #4 degree and actually perform a moving Lydian improvisation.

Such skills are difficult to acquire and, once you have them, it is hard to help others reach a similar fluency. Once something that took you a long time to learn, something that you practiced on a daily base until you finally have it, it's hard to remember what ignorance was like.

(I can't go back to a single monitor setup, my guitar teacher is surely aware of how the world changes the more you know where scales and arpeggios are on the guitar and how they sound, but it's not easy to guess how much it will take me to get there and feel comfortable about something).

Corey Doctorow has a nice quote to explain that with references to regular expressions, or regex or regexp: 

>>> "Knowing regexp can mean the difference between solving a problem in three steps and solving it in 3,000 steps. When you're a nerd, you forget that the problems you solve with a couple keystrokes can take other people days of tedious, error-prone work to slog through." (https://www.theguardian.com/technology/2012/dec/04/ict-teach-kids-regular-expressions)

(I guess we don't have to blame our teachers. I guess for them we are asking questions that are as hard as  "how was it when you couldn't read English?" or "how did you learn the multiplication table of 5?".)

The more you spend time coding and learning the more it seems that Yoda strikes back:



>>>Aspiring or great programmers. There is no in-between.

So let's explore this feeling and this "**ok, I know my syntax, I did some project, where do I go next?**".

We can identify the following sources of mysteries.



### Vocabulary

Python has its specific jargon, this can be mysterious when we first start studying it. This can be easily fixed by developing a vocabulary or looking for one. That's the reason books have indexes, recaps, and lists of definitions or key terms.

It is way too easy to use acronyms (PEP, pip install, API) or other Python jargon (the most intimidating is probably the *dunder* to mean double underscore). It makes us sound proficient, it is cool, it lets us save time. But before we get into this puts us off. 'Cloning' and 'forking' might be intimidating for new git users.
We can solve this issue by **building a reference dictionary or vocabulary**.

There are some already packed ones, but it can be good to develop your own specific one (or to re-arrange preexisting resources in a way that makes sense to you).



### Coding for Others

Sharing code with others is a complex process but it's part of the business.
As they say "code is most often read than run".

Entering into the mindset of coding for others (or with others in mind) is complex.
First, it requires us some confidence in what we are doing. Then it forces us to explore many other issues like:

- how to properly code for readability;
- how to follow code standards.

Isn't this all too complex? I mean, *we are already trying to learn how to code*.
Further, as soon as you develop something you feel is useful to others and you have to pass it to your non-techy friends (how can they be our friends, then?), we have to face the issues of freezing code or building apps.

(My first technical presentation suffered a lot from that. That's how I met Go and Ruby. If distribution is your main concern consider moving to JavaScript - everybody has a browser in their pcs, or something app-related).

The more you get into readability concerns, the more things we need to care about. Here are some sources of mystery related to readability and sharing code:
  
- *coding styles*: things like PEP 8 (https://www.python.org/dev/peps/pep-0008/) and other formatting recommendations. What and how we indent, how to prompt readability, CamelCase vs. snake_case, etc. There are standards out and a good Integrated Development Environment (IDE in jargon, i.e. PyCharm or Spyder) may help;
- writing **comments** or *type annotations* or assert statements to *check the sanity of our code*: those things require some time to sink in. You learn the book and would think "hey, it's obvious I can read my program. I know the syntax and I know what I'm doing. **It was such an effort to get to this print('Hello world!')**. Then you see your code in two days and... what was that?

Flash forward. This happens the more you learn: from procedures to functions, from functions to classes, from a framework to another to "hey, this trick works way better". That's why you need comments and some sort of tests.

The good part: type annotations will teach you more about data structures and writing tests can open a tester career to you.

- *testing in generals*: testing is a beast on its own. Automation and testing, code coverage, continuous development are all things you are going to learn. The first Python step is getting some grasp of the unittest module.^[Docs are here: https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest .];
- *Pythonic ways of doing things*: this is when coding styles and conventions start having consequences not only on the eyes of the reader but also on the runtime of our program.
Previous versions of this paragraph had some examples. Reviewing the book and exploring Python I realized that there are two videos by Raymond Hettinger that are actually there to make us appreciate writing great code. Here they are: https://www.youtube.com/watch?v=wf-BqAjZb8M (Beyond PEP 8 -- Best practices for beautiful intelligible code - PyCon 2015) and https://www.youtube.com/watch?v=OSGv2VnC0go (Transforming Codde into Beautiful, Idiomatic Python -- PyCon Us 2013).

Those are hard to figure out because 'Being Pythonic' is something you can achieve once you sort out some of the mysteries. It means you:

1. have an understanding of how things work;
2. can solve the task in different ways;
3. know what is it like to be Pythonic (a mystery in itself);
4. are able to evaluate which of the implementations in 2 is the most Pythonic.

This leads us to another big topic.

### Python Specifics and Internals

These things are hard to learn. Ok, probably all books tell us about **import this** and the Zen of Python. That's for sure part of the essence of Python and its "spirit", as are some other things that are beginner-friendly like the fact that whitespace is important.

The specific and internals we are talking about are those that will have an impact on performances. Or maybe we are talking about what makes the language you are studying (Python here) different from another language. The point is that, if you are moving your first steps into a language from the humanities chances are you have no idea about another language.

Assuming we have some grasps of different languages, we need to be aware and detect "code smells" (another piece of jargon). "Code smells" are pieces of code that work but are not written following the style and best practices of the language. You see that the code works, but there's something about it. If you have seen the video of Hettinger linked in the previous section, you already have an idea. That's tricky to develop the ability to detect code smells. Memes might help (*stop using i += 1 in for loops!*), but the task is still a big one.

I mean, we are already studying the features and the language. Maybe, depending on your book and sources, part of these are not presented to you as they might mess around with a more user-friendly learning curve.

Nonetheless, this work in a safe environment of an introduction or a book. Then we go out into the wild and some of these things really start to have an impact. And we have no guidance.

Here are some of the possible sources of concerns: namespace, python design (GIL, threading), class operations and design patterns, MRO. Other things like shebangs line or main calls. One way to approach these topics is to find the relevant documentation, read it, and try digesting it with small ad hoc pieces of code.

### Being Pythonic

We have seen this already but it probably deserves an entry on its own.

Pythonistas use their own language, their code is cool and, well, *Pythonic*. Still, getting what it means for code to be 'Pythonic' is hard if we are starting out with Python and if you have no exposure to other programming languages. 

In fact, a perfectly good explanation like: "*This is so Java, you see, you initialize the counter of the loop and then go into it updating. This smells Java. Python has a built-in enumerate() function to do that. Not to mention comprehensions...*" is quite hard for us to get if we have not enough experience with the compared language.

We can try to fix this learning something from other languages. And, when you are there, trying to implement something in your new language (say Java) into your old one (Python).

That's a good way to start comparing things, get a feel for Pythonic ways as well as alternative solutions and implementations. And that's a reason to have Visual Studio Code installed, you'll have access to many different languages with just a tool (through plugins). 

Still, it's hard to learn many different things at the same time and achieving depth. Be aware of that. Maybe you can use features a language is famous for to better understand the features of your main language.

Here's an example of how this may work. We know Python is dynamically typed. We've read a bit about type annotations. What happens if we move into a statically typed language and write our hello world program in Java or C? What happens to programs that are a bit more complex?

Another experiment you may want to do has the goal of demystifying Python classes. Someone says to you Java is the best language for object-oriented programming (there are dissidents at *HumanDemia*?). Java is all about classes and object blueprints.

You read a few tutorials about object-oriented programming *in Java*, build a deck of playing cards or a set of formatting standards for the class PeerReviewedJournal and then you re-build you Evang... sorry, you try to re-implement them in Python.


### Black boxes

Black boxes are another issue. Python is so good with all its modules and functions. This leads to another problem: we trust Python modules or internals to do the work for us (after all, that's what we do with machines, right? We don't question the internals of a washing machine...). We trust some code on StackOverflow or something similar.

We are doing something we know it works, but can't explain why. This is harder to solve. It requires reading the docs and having a look at the internals. But when we succeed, knowledge is built.

Nonetheless, there is something positive about Python and also about the fact that there are a lot of modules, packagings, and libraries around: most of them are built in Python. And many are open source.

Long story short: most of the black boxes you are using are black boxes only in theory. The code is out there, and you can inspect that. We know about GitHub to explore the code.^[If you spot typos please commit corrections.]

Relying on Python codes in the module, especially those of the standard library, will expose you to a clear written code that complies with Python style guides. You are readying the backbone of the language, after all. The same holds for "industry standard" libraries.

Official documentation is another tremendous learning opportunities. Python PEPs always talk to you as a complete developer, showing you a broader picture than a tutorial or even a book. They can also have some nice short programs, like the space trimming algorithm in PEP 257 on docstrings, see here https://www.python.org/dev/peps/pep-0257/.

These will give you moments of (Python) Zen. Enjoy.

## Approaching the Tutorials in a Good Way

I spent some time learning things by reading tutorials and there are a few words to be said about that. Tutorials are great but there are programming phases know as "tutorial hell" (or "infinite syntax loop") in which you feel you are trapped into learning syntax all over again, you are able to do things by way of following instructions but can't program on your own.^[The former philosophers at *HumanDemia* often go back to the Chinese room after reading this, a footnote says.]

So, as for the main book, there are some instructions in dealing with tutorials that highlight the importance of awareness and interactivity. Here we go.

Tutorials are there to get your feet wet and get you started. By no means they are everything you need to know (they are tutorial, right?) and by no means they are there to be the only way.

Here's a list of four pieces of advice to work your way through tutorials to get the most out of them:

1. **Tutorials Are Not The Only Right Way**: There are other ways to do the things in the tutorials. Maybe there are more Pythonic ways or more efficient approaches. Tutorials are there to get you started and, therefore, they should be easy (or, at least, not necessarily over complicated).
2. **Tutorials Are No Sacred Text**: Sometimes I was working on a tutorial and thought about "what if I do Y instead of X?". But then I gave up because I wanted to finish the tutorial first. That's not how it is supposed to work.
3. **Your Work with a Tutorial Doesn't End when you Finish it**: Tutorials are there to get you started. The rest is up to you. Add a feature. Rework the tutorial with different constraints (different languages, only standard library tools, etc.).
A good tutorial should have ways to tell you that it is not finished and you have an opportunity to do your part. If you feel that's a good time to re-read Eric Steven Raymond's piece on hacking and the incremental-hacking cycle, I'll spare you the time to look for your bookmark: http://www.catb.org/~esr/faqs/hacking-howto.html 
4. **Make the Tutorial Your Own**: Don't follow a tutorial passively, engage with it. At least rename the variables. Write tests, add docstrings if there are not. Add comments.

Given the things above, I've tried to modify the way I approach tutorials. (At least the tutorial that range on something we already have some grasps of, like programming).

This is a condensed list from *HumanDemia*:

1. **If You Know Something, Take Guesses**: Think of a tutorial like a guided and heavily hinted problem solving session. Before reading the solution (that is, the tutorial) at least take guesses and sketch your own solution.
2. **Use your Universal Typing Machine and IDE**: When you are working your way through a tutorial instead of having just a file opened where you follow the tutorial (remember point 4 above, try to make it your own) have two.
The first one is your main tutorial window. There you follow the tutorial and know that at the end the project will work (assuming the tutorial has reproducible code). The second file is your experiment based on the tutorial. There you add functions or try alternative ways. You have no fear of screwing things up because that's the point of this file. You have the first safe file to achieve the goal of the tutorial. (What's the Third File? If you go heavy on notes, you may need a third files to take notes, e.g. in RMarkdown).
3. **Extend It**: Congrats, you've finished the project. Now build more on it! Can you add a saving function? What if you have two players instead of one? What if the program works on more than one search engine? Can you make it faster? Can you move instructions to functions? And functions to class?



## Reading the Docs

Tutorials, as said, are just the beginning. Where to go next, often, includes documentation. You want to extend your tutorial, you know that the module you are using has the function you need to add features to your code... but you need to learn more about it. That's where you **read the docs!**

(The web is wide, but there's not a tutorial for every function you may end up using. Or, if there is, it is not as accessible as the docs.)

Further, tutorials often may point you towards to docs to explore things a bit more, try other ways, etc. So here we go with the Docs.

*Reading the Docs* is a skill we need to learn. We successfully mastered reading papers in our fields, academic writing, proofreading, and much more. Some were able to accept academic and intellectual slavery, and maybe received adequate compensation.

Be as it may, to become proficient at coding there's an extra skill to acquire: **reading the documentation**.

The first thing we need to clarify is *what are the docs we are talking about*?

The first answer is the *official* documentation of the module or library we are using. Here 'official' means: the one produced by those that created the code we are using. You already get what that means: these *docs* all do the same thing: *they (try to) explain someone else what the code and its functions and methods do*, but there are no standards.

If you want to know more about the *webbrowser* module or the *os* module or something else that is inside Python standard library, you can expect some sort of standardization in terms of layout and way in which contents are organized.

Documentation is consistent and good also in case of "major" packs: requests, pandas, BeautifulSoup, Flask. Still, expect different choices. (We can conventionally establish something like the following: a package is "major" if it has at least a relevant part of a book dedicated to it. Feel free to tweet me the failures of this definition.)

Some docs will include a tutorial or a quickstart. Some may have both. If the library is specific to something, chances are the docs start with a minimal implementation of an app that does exactly that. (That's the case with Flask).

Coming from an academic background, there are a few things that may happen.

The documentation of the standard library might look a bit *too terse*. It is basically a list of the methods and functions. It details the options and parameters available and the kind of data passed. But those are all the important things you need to know.

Also, the documentation - beyond its terseness - provides links to other modules, reasons for specific choices, and updates on what has changed over time. The documentation of the standard library is also a document in a historical sense. You also get minimal working examples. It's ok to read through the documentation of a module from start to finish, multiple times. But it's also ok to just go there to refresh a specific point, like the order of parameters of a method.

On the other hand, some kinds of documentation are *huge*. For example, if you download pandas references in pdf you may easily get more than 3.000 (thousands, yep, no typo) of pages. That's quite a lot. If you approach reading things top-down, that would be an issue. Be sure to have a purpose and try to come up with a plan about what you want to grasp and improve by way of reading the (huge) docs.

### Why Read the Docs? (A Real-life Case with Bookdown and Ebooks)

Suppose you are writing a book with bookdown. You are excited to read your book on your e-reader. For historical reasons you have a Kindle. So you build your book to an epub (**bookdown::render_book("index.Rmd", "bookdown::epub_book")**) and you already know that you have to perform some epub to mobi conversion magic, for example using Amazon's Kindlegen.

You head over to kindlegen and run it through the command line Powershell (it saves clicks over calibre, you think) and get the mobi. In mixed feelings of anxiety and reverence you open the book - your book. And you realize that there's no table of content.

Of course, you go out and do your research - imagining a long struggle with LaTeX parameters. Here's what you find:

>>> 3.3.1 EPUB
To create an EPUB book, you can use the epub_book() format. It has some options in common with rmarkdown::html_document():

```{r eval=FALSE, include=TRUE}

epub_book(fig_width = 5, fig_height = 4, dev = "png", 
  fig_caption = TRUE, number_sections = TRUE, toc = FALSE, 
  toc_depth = 3, stylesheet = NULL, cover_image = NULL, 
  metadata = NULL, chapter_level = 1, epub_version = c("epub3", 
    "epub"), md_extensions = NULL, pandoc_args = NULL, 
  template = "default")

```

Here you have all you need to know about the building options for epub. There's a toc option set to false. What if you turn this to TRUE? No struggles, it is just an option you need to find out.

The docs are even more explicit and continue like that in case you are wondering "[?!?!] they are not including a toc as a default?". Again, read the docs. When docs are good, they have reasons:

>>> The option toc is turned off because the e-book reader can often figure out a TOC automatically from the book, so it is not necessary to add a few pages for the TOC.

(As you go through, you'll also find that there's a wrapper around Kindlegen to produce mobi *directly from RStudio*, assuming you can manage your path variable.)

### What to Look for in the Docs

The example above was easy both conceptually and practically. Here is a more general list about *what to read in the docs*.

One of the first things to be aware of our inputs and outputs of a specific piece of code. Sometimes you know that there's a nice piece of code that does exactly what you want. You use this piece of code and pass data to it, and nothing happens.

That probably because we are feeding the wrong kind of input to it. We can't pass text to a function doing some fancy computation. (That's why in NLP we struggle to represent text as numbers.)

We can't pass tuples when lists are expected. As we can't modify tuple elements (tuples are immutable), if we need to update some values and we store them in a tuple, that's not going to work.

This instructs us on another important issue: if we are getting our values from some other piece of code or function, it is important to know what we get as an output: are we getting lists or dictionaries? What's the return value, if any? How do we access that?

Let's think about a practical example. Suppose you have to assign students to specific desks in a room, to give them a test. Further, you have to give them a different shuffled version of the test, depending on where they seat. How would you represent this situation?

Another important issue is to figure out what kind of object we are getting when we are using a specific module. Say we draw something with the turtle module.^[You know what's coming in this footnote. Doc. https://docs.python.org/3/library/turtle.html?highlight=turtle#module-turtle ] The turtles we use to draw our figures are the result of instantiating objects of the class Turtle. This helps us in figuring out what's going on in our code and what kinds of objects populate our projects.

Remember to *be active* while reading the docs. Types of object can be checked using the variable tracker in your IDE or using IPython type() command. You can also start doing things interactive and run your small documents-related experiments and then include the results in the main code.

When we are provided with complex classes or functions we have a list of all the arguments and options available. It is good to know that we can't pass two arguments to a function that requires one nor to call something with no values when one is expected.

There's a whole series of error messages that goes like "you called X with some values, but I was expected a different number of values". That's a different kind of error message compared to the previous "you called X and gave X an object of type T, but X wants a different type of object".

### Know your Error Messages and Exceptions

Documentation is also useful when it explains the error messages that it can return to you. Looking at the error messages you receive is the first step to identify a problem and work at a solution.

It is good to know the specific messages you can receive as well as the exceptions. We raise exceptions to prevent our program from crashing. Think about checking exceptions as control failures. Sometimes packages offer you specific classes for errors or exceptions so that we don't have to rebuild them.

### Patterns and Examples

Big packages and libraries may have a list of code recipes. These are interesting to learn if approached right.

On the one hand, they can offer us some solutions or blueprints for a solution. Beware that they are not to be trusted as black boxes. We have to figure out what the recipe does and why.

These recipes, patterns, and examples are also good as minimal working structures to expand.

On the other hand, a list of patterns and examples is a way for us to get an idea of what can be done with a certain tool as well as what kind of code it produces (remember code smells?). So suppose you read somewhere that "X is more Pythonic than Y". You can grab examples of both X and Y doing the same tasks and try to figure out if that's true.

### Docs Creation: The Impact of Automation

Big projects provide you with some automatically realized documentation. They are not cheating. Imagine we are developing a project as a team. Folk at *HumanDemia* asks some of those further away in the onboarding procedure - as you are - to start working on the code.

They want you to focus on code because you like it. You think that coding is more fun than writing about code and documenting it. They think it is more productive to have you working on code rather than documenting it.
Documentation is handled by someone with better writing skills who also has some abilities in reading code and understanding what it does.

We are not questioning this idea of labor division, for now. Imagine how this development can proceed. You are all pushing and pulling work from GitHub, and the programming team has different branches and versions. Those documenting are following the work, but the *official* version keeps changing.

After a code refactoring some of the names of the main functions are *changed* (alas!) and this causes a lot of frustration between docs-team and programming-team.

Then someone from neurobiology and psychology come to visit both team and say the words: 'docstring' and 'Sphinx'. After doing the relevant checks you remember some of the fundamentals.

**Docstrings** are used to insert documentation *inside* the code. Docstrings are a tool to mitigate the issue of writing documentation for code staying too far away from the code itself.

Given that docstrings are a pretty powerful tool, wouldn't it be nice to build the documentation of the functions and classes of the code directly from them? Enter Sphinx (https://www.sphinx-doc.org/en/master/). Sphinx is one of many services to automate the generation of documents.

If you want to document your code, you are free to explore it (as well as other related software). What is important *for this chapter* is that we learn to recognize how this automatically generated documentation looks.

This explains some of the terseness of some documentation and also provides us with clues on where to find the relevant code. Don't forget that more often than not, you can move from the documentation of the code to the actual and real code of the modules.

You are advised to read the modules you used (if they are written in Python). In that way you are going to explore the internals of your modules and you'll also start to figure out which parts of Python are written in Python and which relies on something else.

### Special Kinds of Docs

Software documentation interacts with the whole standards and rules of a language. For Python, this means that some of the Python Enhancement Proposals (PEPs) can be considered part of documentation or docs we need to know.

For example, the first Python formatting standards are on PEP 8. That's a doc we have to learn. The Zen of Python is itself a PEP (20).

Sometimes new language features, e.g. docstrings or decorators, were introduced inside peps. This makes PEP 257 (https://www.python.org/dev/peps/pep-0257/) on docstrings convention kind of "the doc for docstrings" and PEP 318 (https://www.python.org/dev/peps/pep-0318/) the one for decorators of functions and methods.

Beware that PEPs have their rules and different statuses. In fact, not all proposals get passed and actually implemented.

## Summary

This chapter provided you with the information to go out alone and use your programming skills to do what you feel you need to. Fluency in every language comes with practice and this chapter (and the one before it) is far from giving you all the exercises and practice contexts.

Nonetheless, you were given guidance on how to explore more about the Python world. You are aware of some of the main issues that may block you down your road to Pythonista: you have a first scheme with roadblocks and boxes to fill your Python knowledge. Go and fill them!

And you now that a lot of your learning time will be spent trying to figure out things from the doc.

### More Resources

Free-stuff:

- The best way to know what's in the Python standard library is to have a look at the table of contents of the docs for the standard library: https://docs.python.org/3/library/ which is pretty huge. Before trying to reinvent the wheel, have a look there.

- Vocabulary-wise, here's a nice learners' glossary on GitHub: https://github.com/catherinedevlin/python_learners_glossary (try to contribute with more, if you want);

- This is my attempt to come up with a Python glossary. A more extended list is still growing: https://medium.com/analytics-vidhya/python-acronyms-and-vocabulary-bd2cd0c53bb6

- Norvig's Infrequently Answered Python questions: https://norvig.com/python-iaq.html will show you a lot of Python internals;

- *Hitchhiker's Guide to Python Python Best Practices Guidebook* (free at https://github.com/realpython/python-guide). This was one of my first teach-yourself Python books.

- If you want to learn about web development and shape your software building abilities by learning about testing, *Test-Driven Development with Python* (Obey the testing goat!) by Harry Percival is a real banger. There are no excuses not to read it because we also have a free version: http://www.obeythetestinggoat.com/pages/book.html 


Bookwise there's quite a lot you can read:

- Dan Bader's *Python Tricks* is an excellent book that digs deeper on a variety of Python issues, from internals to data structure to best practises while coding with others. It has a lot of code snippets, but it is not a cookbook. Every piece of code is there to make you think. (I have a longer review here: )

- Julien Danjou's *Serious Python: Black-Belt Advice on Deployment, Scalability, Testing, and More* is not your intro to Python book. The book is there to bring you to another level and let you see something different from hello world.

- The book *Seven Languages in Seven Weeks* teaches you more than one language in a pragmatic way. For the curious, languages are Ruby, Io, Prolog, Scala, Erlang, Clojure, and Haskell. The languages follow different kinds of programming methods.

- Do you remember Norvig's spell-correct program from the previous chapter? If you scroll down the page with the code you can find links to the same program being written in different programming languages. Have a look: https://norvig.com/spell-correct.html.

- You already know you can even try some of this code on Visual Studio Code, don't you?

- *Think Python*. Probably that's an introduction to Python. Still, the exercises are above the average and the book fear not exposing you to Markovian chains and other machine-learning oriented stuff.

On clean code and sharing code with others we stumble on two classics: 

- Robert Cecil Martin's *Clean Code: A Handbook of Agile Software Craftsmanship* 
- Andy Hunt \& Dave Thomas's *The Pragmatic Programmer*. They use different languages (Java, mainly) but the concepts transcend the programming language. Further, you'll get exposed to a different language and use it as a tool to learn fundamental principles. The advice you get applies to Python, but you'll have to work on it to get its Pythonic application. Cool! (*Clean Code* has exercises that *The Pragmatic Programmer* hasn't.)


### Further Work

Take a look at libraries doing similar or overlapping things. Try to highlight the differences relying on the docs and what's the more Pythonic option by looking at some examples. If you lack ideas try: PyTorch and TensorFlow, Matplotlib and Seaborn, Selenium and webbrowser, Flask and Django.

You can explore some python tricks (or contribute yours) here: https://github.com/sahands/python-by-example.

If you want to start doing some work and projects try this out: http://pythonpracticeprojects.com/.

# (PART) Programming for Fun and the Academia {-}