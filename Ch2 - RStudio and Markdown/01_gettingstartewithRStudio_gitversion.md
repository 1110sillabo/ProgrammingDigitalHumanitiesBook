{#ch2}
# The Universal Typing Machine: Markdown and RStudio

Your journey at *HumanDemia* starts in an unexpected way. They want to you to leave behind your wordprocessor. That's not simply leaving BrandedTextEditor for OpenTextEditor.

You are going to write through "a word processor on steroids". You'll have your main windows where you write, plus something else, like line control. "If you aim for precision, you'll love that". (You may buy into that one.)

Further, you are going to write down the specifics of your document. There. At the beginning of your document, not through some window hidden somewhere you'll forget about it. That's your first step to learn *being procedural*.

Also, your new typing machine won't do things you are not telling it to do, like resizing things, switching footnotes or other amenities. 

On your way down, you are going to learn a markup language you already know (and it's not HTML). Little by little they'll get you acquainted with an Integrated Development Environment (IDE), a shell and also the opportunity to execute code.
Oh, even if you stop there, you are going to compile to .doc, .pdf, .html, .epub **from the same file**.^[So, next time you have to write a book nobody wanted to read (and you didn't want to write) because of the new rules of academic recruitment, you know how to write it.]


## The Boring Side of Academia

"Formatting and submitting articles, thesis, reviews, etc. should not be how we spend most of our time in academia". That was on the *HumanDemia* job ad, and that's one of the reasons you've applied.

Unfortunately, in the humanities we struggle to implement peer review, not to mention having clear stylesheets and guidelines to format a paper.
Have you ever submitted the *same* article to *different* journals all in .doc format, each time dealing with crazy useless specs hard to automate?
Been there. Done that.

How many files did you have to for that *one* document sent to four different journals? Maybe you did your share of rebellion. Got into Latex and various .bib plugins.

Luckily, there's a way out to keep the best out of our favourite Mendeley and Latex experience. Further, it extends to Python, Git and other things on the *HumanDemia* onboarding.

Markdown and RStudio come to the rescue.
The best of all news is that: we *basically know Markdown already*. 

**Markdown** is a markup (notice the pun) language you need to know. It looks like the internet of the '90s and early forums. It is also the language of the new web you are about to discover: in fact, most of the readme files on **GitHub** presenting the instructions of your code are written in Markdown. 
Also, on Jupyter Notebooks or Google Colab *text fields* are written in Markdown.^[
If you have some data science ambitions, it would be cool to test the following hypothesis: *there are more freely available books out there in Markdown format than in .doc*.]


### Sidenote: Survey on Academically Boring Things

I've conducted a small survey on things in academia that worry us/slow us down and that do not align with our idea of "working in the academia" (*Thanks everyone replying to my survey in order to find out more about that*, feel free to message me with more suggestions):

- getting tenured (*well, that was not included*);
- waiting for reviewer 2;
- waiting for someone recovering from missing a deadline;
- emails;
- do exams/marking papers for courses you are not teaching;
- various ways you can be mocked off exceeding those listed here;
- figuring out a list of n journals to submit our paper;
- reformatting a paper because reviewer 2 of journal n-1 in the list rejected our paper;
- getting more data (e.g. papers) from our research;
- perform a literature review;
- attending seminars because your boss knows you are going to ask questions (because they make you feel like you're not wasting time) when you are at seminars you consider a waste of time;
- meetings;
- explaining tech stuff to those having double your age.

A little bit of coding can account for some of these (as well for other, way bigger issue, like facing impostor syndrome or dealing with perfectionism plus self-underestimation issues, i.e. something will never let you submit your work because it's either not perfect or, if of decent quality, trivial or not worth publishing.)

The Key Idea: "Do Not Sit and Wait, Automate" looks good enough on the on-boarding documents.



## Installing RStudio

*RStudio* is Integrated Development Environment (IDE for short) for R. **R** is a programming language on its own, used mainly for statistics. Maybe inter-departmental projects led you to bump into R-people.^[Joel Grus has some code-humor on R and Python for data science.] Using R you can plot data and analyze them, but we are not interested in that here. Of course, you are encouraged to explore the strengths of R.

We are using RStudio as an *enhanced text editor*. With RStudio we can easily type our Markdown text, and use all the instructions to format a document and manage the bibliography. If you have any experience with LaTeX, the visual impact of RStudio won't surprise you that much.

Plus, through RMarkdown (RStudio version of Markdown) we can access some great tools like **rvitae** (to write academic resume), **blogdown** (websites) and **bookdown**. They target academic needs and the last two packages are documents with books instead of tutorials: super academic friendly!

First things first, head over to RStudio download section: https://rstudio.com/products/rstudio/download/. Then pick the relevant version for your system. It's free (there are also paid versions offering more features).

Once you open your first RStudio session go to 'File' > 'New File' > 'R Markdown'. Enter 'title' and 'author' and move forward. You can now see your environment. Most of it is the file you are writing.

Let's briefly go through the main areas.

**1. RStudio Open Docs Tab**

This is where you navigate through your files. You may have more than one file opened at the same time, as you do in the browser.

Everything is close by and visually organized. Think about working on different chapters in different tabs, then assemble the whole thing. Now think about doing this in Word. And cry.

**2. RStudio Main Working Window**

That's right below the list of files. That's your text editor.

This is where you write your stuff. You have line numbers, which is nice if there should be some issue in typesetting your figures, but mainly it's your Word main page. If you look up in your document you see there is a preamble like LaTeX.

The preamble starts after three single lines (like this '-') and finishes again with three lines again '---'. That's the preamble of an empty document:

```{python eval=FALSE, include=TRUE}
---
title: "Untitled"
author: ""
date: "13/3/2020"
output: html_document
---
  
```


HTML output is great to make ebooks and compiles faster. If you need a pdf, just replace the output with 'pdf_document'. Use 'word_document' to stick to the boring habits or 'epub_document' to get ready to reach ereaders, Kindles, etc.
Feel free to add more than one in a raw, but beware of spacing and other issues. The preamble is delicate. You are talking to your machine and everything you type there is sensitive. Feel free to research what you are doing there and what are more commands available.


(In the next section we'll cover adding a little bit more of control to our file, like *adding a table of content* and *adding a bibliography*.)

**RStudio Console**

Right below the main window, there's the console.

You have a console, a terminal and a panel that shows the status of your R computations (you won't need that much, unless you are using R for real, doing statistics.) 

We are going to use the console to install a few packages (like *bookdown*). You don't know this yet - see next chapter - but there you have a Command Line Interface (CLI).

**4. Managing and Controlling Tools: Right Panel**

On the right you have two further windows to monitor both the overall installation of R software and packages *and* the resources of in your folder.

The Up-Right table starts with 'environment', but you are likely more interested in the 'History' tab (showing you the commands you've typed) and the Build tab - you can use it to create a book.

Down-right you have files, which acts as a file manager. This comes in handy if you are typesetting a book and need to open or delete a preview. With this, RStudio can be your (friendly) panopticon.^[Shame moment: before I discovered that, I spent a lot of time getting out of RStudio, searching folders in the resource manager and then back to RStudio.]

Honorable mentions for the 'Plots' tab (though you won't need it) and the 'Packages' tab that lets you know what's going on with all your packages.


## RStudio Settings: Darkmode and Packages

Your eyes are important. If you prefer a dark theme (environmental reasons may play a role as well), you may want to pause for a bit and maybe consider choosing a different theme or background (there's a dark background). Go to **'Tools' > 'Global Options' > 'Apparences'**.

We are ready to go and start writing some Markdown. Nonetheless, to unleash the full potential of the tools there you may need to boost RStudio with additional resources. 

I've already mentioned packages more than once. Packages are collctions of optional code that allow you to extend the functionality of RStudio. Think browser extensions like and AdBlock (unless you are already using Brave Browser).

Here we briefly touch how to install packages, so that you are free to go and add as much as you need to make your best possible work.

The console of RStudio is important. This is where you go if you want to edit your package and improve it (something similar to Python PIP install).

If you want to figure out what packages are installed you can:

1. go in the Right-down window under the 'Packages' tab and inspect it;
2. go in the R Console and type:

'**installed.package("NAME OF THE PACKAGE")**'

to check if the package is there.

To check all installed packages go for:

'**installed.package()**'.

Finally, to install a package you haven't installed, type:

'**install.package("NAME OF THE PACKAGE")**'.

(R will access a repository and download it from there. Most of the packages are hosted on something called *CRAN*.)

RConsole is friendly. It is a command-line interface (CLI) tool, we'll look closer in the next chapter, but it is friendly in telling what went wrong and sometimes it even suggests you your next move (for example: 'You want me to do X, but in order to that I need Y. Please install Y by doing Z'. - If your colleagues are all as helpful as RStudio console then you're lucky.)

Here are some further resources on R Packages and their installation: https://www.datacamp.com/community/tutorials/r-packages-guide.

## RStudio Automation for Humanities: TOCs and Bibliographies

The preamble is where you define all the settings of your document. Things like whether to print a table of contents and how to deal with section headings and numbering, which style of bibliography do you prefer as well as general layout, etc.

Here's a list of some powerful options you have to add below you output choice:

1. **toc: TRUE (or yes)** -- shows toc;
2. **toc_depth: value** -- decide how deep the toc will be;
3. **numbered_sections: TRUE** -- sections are numbered.

(Again, 'TRUE' being caps-TRUE is important. There are some possible odd things we have to learn to deal with when talking with machines.)

Guess what you need to do to avoid showing the table of content or the numbers.

As an exercise, write the preamble to that produces a document called 'RStudio is amazing and I know why' where you are the author and the day is the current day. You want to print the table of contents without numbers and you want to show sections, subsections and sub-subsections.

Ok, below is the code.

Ready?



```{python eval=FALSE, include=TRUE}
---
title: "RStudio is amazing and I know why"
author: "Enter your name"
date: "enter today's date"
output:
  html_document:
    toc: TRUE 
    toc_depth: 3
    numbered_sections: FALSE
---
```

(Yes, if you do not want something you use either FALSE or no.)

Beware about the formatting. You're better off nesting all the options and parameters.

### Managing Bibliography

In the Humanities a huge amount of time is spent (wasted?) in the **submit-wait-blame reviewer 2-change the formatting-submit elsewhere** cycle. I think the waiting part is probably the worst.

RStudio can't grant you faster responses or better reviews, but it can save you typing time, changing and checking commas and parentheses management when a journal wants you to check that "*The article follows author guidance for bibliographies*" tick. (Assuming the journal is able to translate its preferences in some sort of standard or known bibliographic style).

To add a bibliography all we need to do is to add a '**bibliography**' parameter in the preamble. That sounds logical.

Then we need to specify the formatting style: the information across the different APA, author-date, full cite, Chicago style, etc., references are always the same. What changes is the cosmetics.

The concept is super easy. 
A style file has the needed information to take the raw basic information and apply the relevant cosmetics. Editors are happy they don't have to check it, we are happy because we gain more time to think and less to dressup our double commas for the next submission. 

The file containing bibliographic data in a way that can be automatically is the  '.bib' file (*HumanDemia* thinks you are fond enough on file extensions, if not search for it). You can easily write .bib files in a text editor like the Notepad (the one that produces .txt, then you save the file as .bib) but it takes time.

It is worth knowing how .bib files are written and what they look like, so that you can tweak them efficiently if you need it. [Here's](https://www.dickimaw-books.com/latex/thesis/html/bibformat.html) an explanation of .bib files - https://www.dickimaw-books.com/latex/thesis/html/bibformat.html - they have a lot of horrible \{.

To produce the .bib file we can make our life easier and use a tool like Mendeley (https://www.mendeley.com/?interaction_required=true) or JabRef (https://www.jabref.org/) or something else. Feel free to do your research and find out what you prefer. If you are lucky some databases (e.g. philpapers.org) allow you to export bibliographies in .bib mode.

Both software mentioned above have browser plugins to allow you to retrive biliographical data from the pages you visit.
You can work out a comparison on your own.^[Mendeley has Springer involved with it. JabRef is an open source, you can see the code and solve issues on GitHub (it's Java-based). I sorted out an issue with a huge .bib file using JabRef. I then build a new bib base with Mendeley relying on the plug-in mainly, which worked decently enough. The Mendeley-Word integration worked but not that smoothly.]


Anyway, no matter what tools you are using you'll find your way to produce your .bib file. Now we have a basic understanding of .bib files. Our goal is to have a .bib file to feed to our preamble. Then, through the preamble, we will manage our bibliographic details and we are going to quote the references through our main document.


### Bibliography Template Example

Ok, let's write a working preamble. We add the bibliography field and define a style with 'csl' (short for Citation Style Language).

Here's an example:

```{python eval=FALSE, include=TRUE}
---
title: "RStudio Bib Demo Cas"
author: "Guglielmo Feis"
date: ""
output:
  pdf_document: default
bibliography: demobib.bib
csl: europeanjournal.csl
abstract: Demo showing RStudio bib management
---
```

In addition to our ordinary parameters we add the 'bibliography' field. What follows is the name of the file containing the bibliography (guess what? You'd better put that file in the same folder of your main Markdown file).

You can also specify a certain **csl**, i.e. the citation style language, feel free to read more here about how that works here: https://citationstyles.org/. Just google the csl you need. Different csl means a different look of the references through the document. You just need to find it and type in the right csl. Your bibliography will change accordingly. Say hello to extra time for writing a better paper!

To cite the entries in the bibliography you need to use the @syntax (like LaTeX, or mentions in social networks).

Suppose there's a file called 'myamazing2020paper' in your .bib file. To quote it, just type \@myamazing2020paper and the reference will show up as required. It could be a footnote displaying (Yourname, 2020) or a 'Yourname (2020)' or '(Yourname 2020)'. It all depends on the csl.

At the end you'll have a list of the files in the bibliography (be sure to add some sort of '# References' section at the end).

Beware that \@syntax is case sensitive. No typos are allowed and not even confusing 'Trump2020' with 'trump2020'.

## Markdown Basics

Time has come to learn some Markdown, i.e. to realize you know it already.

Markdown is an easy markup language (think *HTML*). We type something to get special formatting. Contrary to HTML we don't have explicit tags like '<body>' and '</body>' or '<a href>'. We are doing most of the marking with signs that are easier to reach like stars \* and the (now) over too popular hashtag \#.

Pipes (|) and hyphens (-) can be used as well, for tables.

Ok, time to go into Markdown, the basics are supersimple.

1. If you want to **add sections**, you number them with a '#'.
The more you add, the deeper you are going into the sections. So '###' is header3 in HTML or 1.1.1 if you want numbered sections. (There are further options to set this).
2. enclose a word or phrase between one star '\*' to get *Italics*;
3. enclose a word or phrase between two stars '\*\*' to get **Bold**;
4. Lists are created **adding a new line** to initialize the list and then listing items either with '-' or numbers followed by a point.




```{python eval=FALSE, include=TRUE}
Markdown lists:
  
- you need the empty line
- above
- [ ] this will give you checkboxes
```


And that's it, basically. You'll find a full cheatsheet for Markdown at the end of the chapter.^[Remember the Learn X in Y Minutes? That's the markdown part: https://learnxinyminutes.com/docs/markdown/.] 

(Oh, yes, HTML links automatically takes the reference. If you want to add clickable text to the link the syntax is '[Text you want to show on the highlighted clickable link] (url of the site you want to link to)'.)

Try to type something into Markdown. Maybe a table of contents and a few lines. To have the magic happen you need to *build* your document. In the preamble you specified the output you want your text to be rendered into.

To have such a file it is not enough to save it. Try saving it: the extension is **.Rmd** which stands for 'R Markdown'.

To go from .Rmd to your .pdf or .html or .epub you need to 'build' the document (or compile it, if you come from LaTeX world.) The easiest way to do this know is by pressing the **Knit** button. (Or **ctrl + shift + k**, if you are getting used to shortcuts.)

RStudio will take some time and produce what you need. If you are outputting to .pdf you'll realize that RStudio is working with Latex under the hood. Should you miss some packages, you'll have to install them using R console.

(It is likely you'll need to **install.package('tinytex')**, i.e. RStudio minimal functioning LaTeX. Oh, I wish getting LateX to work was as easy as getting RStudio working and installing an extra package.)

### Newlines, Pagebreaks, Cross-references, and further Text Divisions

Your text setup may need more operations. Here's something more. You can search for further options:

1. You can add *horizontal lines* in your document using six consecutive - or six consecutive '*';
2. If you want to *insert a page break* you have to consider the output you are using. If you are knitting into a pdf (using a tex), you can use the latex command **\\newpage** or **\\pagebreak**;
3. If you need to add section references or similar you need to boost your markdown. The easiest option is to install the *bookdown package*.
Once you do so, you can easily refer to sections of your work putting the name of the section between square brackets. Bookdown is also useful to have parts and chapters;^[And footnotes using this caret ('^') and square brackets format, which may appear strange on GitHub.]
4. If you want more layouts you can either choose from a variety of templates (expect LaTeX quality) or go customizing your own templates (see there if you have that need https://bookdown.org/yihui/rmarkdown/template-structure.html). 


### Creation of Tables

Markdown tables are easy to write and cool to watch. You just build the table out of | and -.
To define cells are divided by '|'. To define a table structure you need to have a set of --- under the main table call.

Like this

```{python eval=FALSE, include=TRUE}

| Column heading|
| ------------- | # :---: for centered text, ----: for right align
| col value     |
| another value | 
| etc           |

```

Note that you need at least 3 dashes separating each header cell.
The outer pipes (|) are optional but looks good. Also, the table will be made even if the pipes are not all vertically aligned. 
raw Markdown line up prettily. You can also use inline Markdown.

If you wrote a big table and want to modify it, that can be harder, especially if you have an empty table you fill little by little. If you have issues, knit the document to help yourself visualize where the modification is going to happen.

### Adding Images

If you need to add images, the Markdown syntax is close to the one for links: 

'**\![text of the image if you hover over it with the mouse, aka 'alt text'] (where to find the image)**'

Note that the *where to find the image* can be a url site or a file on your pc. In the latter case, be sure that you are inputting pathnames correctly. Practically: should you get an error, try to change '\\' with '/'.^[Unix, Mac and Windows follows different conventions to manage paths on the file systems. So if you think the biggest irrationality was that of different pins, sockets and voltage maybe you have to review some beliefs. *Maybe*.]

However, if you are using RStudio to knit your document (and not, say, displaying some text on the internet), RStudio requires you to put the images in the same folder as your main Markdown document.


### Cross Referencing

If you need to add section references or similar you need to boost your markdown. The easiest option is to install the bookdown package.

Once you do so, you can easily refer to sections of your work putting the name of the section between square brackets. See https://bookdown.org/yihui/bookdown/cross-references.html for more.

### Adding Code(s)

Another benefit or RStudio is that you can *insert* (and run) code blocks. The code can be Python code, R code (it's RStudio we are using, after all) and much more.

RStudio supports SQL, Java, C++. What's even better is that you can decide what to do with that code. You can display it and even *run it*.

In that way, if you want to include some fancy graphics that are code-based into your report, you can do that. Further, suppose you are writing a paper with some data. You change the data and all you have to do is refresh your code to have an updated plot. Forget the days of open Word, open Excel, update the chart, export it, remove the old one add the new one.

To create a code block all you have to do is typing three backticks (\`\`\`) - or use the **ctrl + alt + i** shortcut.

The default option is R, but you can change it to your engine (e.g. Python). Given a piece of code (**chunk** in RStudio jargon), you can select two properties for it:

1. **eval**: choose if you want the code to be run or not;
2. **include**: choose if you want to display the code in your document or not.

(If you write a tutorial you want to include but not to evaluate the code, but if the code is producing some fancy graphics you just want the updated graph but not code.)

Here's a tutorial like example:

**\`\`\`{python eval=FALSE, include=TRUE}**.


Be aware that a lot of the extra formatting assistance we are going to have from a dedicated Python editor won't be there when you type Python code in RStudio. This is particularly important for Python as, in that language, space matters.

Should you write some Python in RStudio *with the intention to share your code* keep that in mind (or learn it the hard way, as it happened to me while proofreading some of the code that follows from chapter 4.)



## Comparing this Setup with more Traditional Ones: The Benefits for Academics

Writing Markdown through RStudio offers academics and people working with texts and data a super advantage: **the work can be exported as .pdf, .html and .doc**.
Further, we control the form of the output, whether its a regular text or a slideshow.

Besides that, RStudio offers you further tools like control on the bibliography that you can print in different styles by changing a parameter (think **LaTeX**). Plus you get themes and layouts.



After this dense exploration you may wonder why you have to switch to that setup rather than the standard Word-powered one. There's a lot going on, I'll limit it to a few bullets.

- You can speed up the resubmit process. Change the csl and you're done. No more years spent with fixing details in Word (been there, done that).
You can do a bit of that with bib managing tools in Word but my experience with them over a 10 pages project becomes a nightmare. And it gets worst if your work is shared.
- (The above leads to a better planning for your journal trajectories. You'll appreciate editors that know their preferences and can point you to the right bib style or csl. If they don't know that they are probably an Island and not worth your time.)
- You can export to all outputs. You'll want HTML if you want to use Amazon Kindlegen and get a smooth transition to mobi format. You'd like to go from a pdf to a doc if you are unlucky and your nice latex-based Ph.D. dissertation falls prey of strange academic publishing standards (been here, hated that). Latex to Word is hard, here you have the Markdown layer that has all the features you need and is able to output in different ways.
- Given the success of GitHub and the issues with peer review and academic publishing (enter your favourite) we may envisage a day in which GitHub enters Humanities. Guess what is the language of text documents on GitHub.
- The whole thing is free. Ask your head of Department (if she knows it) how much your University spends on licenses. Translate this into semi-decent research fellows or imagine how a share of that may impact your university's output. Then please take action and let me know about it.
- Bonus point: Markdown looks more user-friendly than LaTeX if you've been a forum early adopter. It goes easy on \\ and {}.




## What's More in RStudio

We are using RStudio as a Universal Typing Machine, but it offers much more.
As we know already RStudio is way more than a cool markdown text editor. Besides its markdown capabilities and its R-based features RStudio also offers the following features you may want to check:

- **shiny app**: a nice tool to develop apps that show data on the web. To quote from their website "Shiny is an R package that makes it easy to build interactive web apps straight from R. You can host standalone apps on a webpage or embed them in R Markdown documents or build dashboards. You can also extend your Shiny apps with CSS themes, html widgets, and JavaScript actions".
- **learn R and develop in R**: R is a whole programming language on it own that was (and maybe is) very powerful and suited for statistics. (R also has a whole document documenting some of its issues as a programming language, see the ['The R Inferno' document](https://www.burns-stat.com/pages/Tutor/R_inferno.pdf) at https://www.burns-stat.com/pages/Tutor/R_inferno.pdf.)
- **use RStudio as a text editor for other programming languages**: RStudio allows you to include code boxes from other languages (Python, SQL, JS, C++). This is great if you want to show your code and discuss it. You can also run your code in other languages, but you have to consider whether to use different tools for different programming languages.

## RStudio Workflow: Learn, Write, Get It!

RStudio prompts a nice workflow in which you can write your notes and then move them into different documents. You can have code inside them, so it works perfectly to learn to code.

Feel free to take notes of this book on that system. You can even use RStudio to type in and run some Python code.

## Books with Markdown: the Bookdown Package

The Bookdown package is there to boost your abilities in writing and delivering research products. If you feel restricted by documents, the package has everything you need to make your book come true. Further, getting the bookdown package to work is a useful exercise to review what we know about RStudio.

### Installing Bookdown

The first step is to get the package. That's easy. You know both the name of the package and the command to install a new package. See you in the next step!

### Setting Up a Bookdown-book

Working in bookdown will change our setup a little bit. The bookdown packages allows you to write dedicated .Rmd chapters and then compile them.

This requires us to set up properly:

1. instead of single files, create an Rproject: 'File -> New Project';
2. bookdown starts compiling the book from a file called 'index.Rmd'. All the other files ending with .Rmd in the folder of the index are then rendered and included;
3. organize the folder and the naming accordingly;
4. if you need extra .Rmd files, like a list of checks, a bin of leftovers be sure to include in a dedicated folder. Otherwise they'll get into your main file.

For the bookdown file to work, you need other little twists.

Instead of knitting you can try Right-Up building options. Still, that works best is to compile your book from the console with the following command:

**bookdown::render_book("index.Rmd", "bookdown::pdf_book")**.

The other big change is that *only the index file will have the preamble*.

All the other documents, i.e. the chapters, are going to start directly with '\# chapter's title'. And, in a chapter, you are allowed only one level one '\#'.

If you need to insert parts, the syntax is the following:

'**\# (PART) Part's name \{-\}**'.

The part name has to be inserted at the end of the chapter that comes *before* the part.

### Bookdown Mechanics

When you run the command to render the book you specify the index file and the format you want. *Bookdown will merge and render your dedicated output*.

Should something go wrong, you'll get either instructions in the console or a specific log file as a .txt file. What RStudio does is creating a '_main.Rmd' file and try to compile it. If there are issues and line references, they refer to the main.Rmd. That's why there's an error at line 2023 despite your chapter being 456 lines long.

Before recompiling you have to delete the temporary '_main.Rmd'. That's where the Right-Down 'Files' view comes in handy.

Bookdown is well documented (see more resources).



## Summary 


The preamble is where most of our magic typewriting happens.

We need to feed it a .bib file and a .csl style file.
The .bib can be built with Mendeley or JabRef (or by hand).

Markdown is easy. If you need to build a whole book, you can use Bookdown. If you need a website, try blogdown.

Now you should orientate yourself in an RStudio session, write in Markdown and create simple preambles.


### List of RStudio Shortcuts

Shortcuts can save a lot of time. With RStudio you are likely to be doing some operations quite a lot, so here are the relevant shortcuts:

- open a new file: 'ALT + F' (then navigate on new file and choose what you need);
- navigate across markdown files: 'CTRL + ALT + left/right arrow';
- knit the document: 'CTRL + ALT + K'.
- next RStudio tab ctrl + tab;
- previous RStudio tab crtl + shift + tab;
- knit: ctrl + shift + k;
- insert code block: ctrl + alt + i 
- zoom in: CTRL + + (sometimes you may accidentally hit + instead of \* when you try to add italics);
- zoome out: CTRL + - (when the above happens, this will bring you back to ordinary conditions).

### More Resources 

Here a few links for more bib-related stuff: 

- More Info on Bib Styles: https://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html
- More Info on Citations Styles: https://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html#citation_syntax

Moving to Markdown:

- Here's the promised MarkDown cheatsheet: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Yihui book's on Bookdown is probably your best introduction to Markdown and bookdown: https://bookdown.org/yihui/bookdown/cross-references.html. You can even check the Github version of the boo and contribute to it.
- https://monashbioinformaticsplatform.github.io/2017-11-16-open-science-training/topics/rmarkdown.html
- https://rmarkdown.rstudio.com/lesson-1.html


### Further Work

Here are some idea to practice the things we mentioned here:

- set up a book template;
- look into the bookdown documentation;
- go into RVitae Package;
- RStudio exports to epub. Still, Amazon Kindle uses a different format, .mobi. If you want to produce a mobi file you can use both .html or .epub outputs and feed them to Amazon Kindlegen software. It just takes a command-line command to do that (compare this to a Calibre workflow). Do some research on Kindlegen. Produce one or more RStudio-based .epub or HTML and get ready for launching the Kindlegen-based command line interface from the next chapter;
- move to the next step and explore making Blogs and Websites with Blogdown.
