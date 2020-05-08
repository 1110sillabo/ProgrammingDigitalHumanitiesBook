# Command Line Interface and Git(Hub): Get Ready for Machine Talk and Cooperating with the World {#ch3}

Your second installment in the *HumanDemia* onboard is designed to bring you back to the roots of human-machine interactions. Command-Line Interfaces (CLI) are a primary tool to communicate with machines. Instead of pointing, clicking or touching (graphics stuff of a GUI) you simply write down what do you want your machine to do. 

Of course you need to agree on some language, which forces you to know what the machine can recognize as a proper command. "This sounds so much like the beginning of *The Matrix*", you think.

Now, *The Matrix* is cool - but it is already dated. Still, CLI is even more old school, retro or date (your choice). *Neil Stephenson* has a terribly good book called *In the Begining was the Command Line* - the book is on the Cyberpunk library for free: http://project.cyberpunk.ru/lib/in_the_beginning_was_the_command_line/ (you *have* to read it and, by the end of this book, you should be able to have it in the format you prefer to read it).

Stephenson's title proves the point: this CLI thing is old.
This is how (quite a lot of) it started.

"*Why do the folks of* HumanDemia *bother me with that old stuff? Isn't there something more techy and in demand to learn*?," you wonder, despite appreciating being philologically right and going back to where things started.

As we're going to find out, there are CLIs in most of the hyped in demand words you may have thought about. From **GitHub**, where you'll share your marvelous applications with the world, to *Python* programming, *R* programming or *SQL* querying. You simply need this and, well, you have already saw some command-line machinery in the previous chapter when packages were installed in *R*.

**TL;DR**: file operations require some command of command-line navigation (no pun). Updating and installing packages or modules to programming language are command-line based. Further, especially in non-Windows systems, a lot of file and system operations happen in the terminal, the shell or bash... which are command-line interfaces.

Ok, let's dive in this Stephensonian thing:

1. *first*, we are going to refresh some command-line essentials;
2. *then* we'll dive into some GitHub operations.

## Command Line Essentials

Do you remember the old days of **MS-DOS** or **Windows 3.1**? If you don't, that's a short summary of what these days were like.^[If you feel nostalgic you can bring these days back with Freedos: https://www.freedos.org/. ]

Imagine a Matrix-like scenario. There's a blinking prompt in the up left corner of the screen. But it's black and white. It says **C:\\**.

Mum and dad told you have to type '**win**' to start Windows 3.1. There a magic graphic interface appeared. There was a 'File Manager' icon looking like an Ikea drawer which did what you now do under 'This PC', and there were accessories, games and applications.
Mum and dad also told you not to run '*format C:*', as it canceled all the stuff on the hard drive. And they were right.

### Navigating File System with the Command-Line

To appreciate what is it like to use a command-line interface think about operating with your computer *without using the mouse*. This is something you have already experienced in the exercises about practicing the shortcuts.

Now, think about this: suppose you want to run a program *without the mouse*. Of course you can easily navigate on an icon, press enter and run it. But what if there's no icon or if the path to the exe is far far away?

Part of the workflow in command-line system is this:

1. *reach the proper folder/directory* on your hard drive;
2. *run the commands* you need in that folder (e.g. run notepad).

The first part is all about managing paths and is most of the command line jobs you are going to perform. The second is often where the command line blends into programming or something else. In fact, you are going to use program-specific commands.

On Windows 10 there's a specific CLI called Power Shell - you can search for it with the (WinCmd + S shortcut). While you think that's gonna be easy you find yourself whispering "curved balls".

The next paragraph of the *HumanDemia* docs looks like the following.

Summon the shell and try to solve the following tasks:

- navigate to the download folder;
- list all the files in the download folder;
- go into your main working directory (i.e. where you have papers and programs) and open one of your recent works.

No mouse and no graphics feedback. You are only going to read and type in the prompt.

Ok, to complete the tasks above there are some backups for you.

The most common operations on various CLI are the following:

- *change a directory*: this is done with **cd [where to go]**. Back in the days maybe you have something like 'cd windows'. You got to 'C:\\Windows\\'. And from there if you type 'SimCity' you had a game to be played.
- *list files in a directory*: you just landed into a new folder and have no idea about its content. Type '**dir**' to find out.
- *get back one step in the path hierarchy*: suppose you are down into a very long path like **'Your Drive\\A folder\\Another folder\\A program\\A program subfolder\\Something Else\\It should be here\\But it's not in this folder\\'**.
Suppose you want to go back higher in the 'it should be here' folder. You can either type the same cd path and cut the last part. But you can use '**cd ..**'. The two dots will put you up in the hierarchy.
- *create (make) a new directory*: you are now a command-line wizard. You navigate do the path you want, know how to run the different relevant commands, but realize you need a new folder before opening a Jupyter Notebook? **mk dir** is the command for you.

Cool, you can now move around directories, list them and create new directories. That's enough to be dangerous and, from there, you can explore for more (have a look online at **shell scripts** to learn further tricks).

There are a few things worth knowing if you are moving towards the command line:

- the kind of machine you operate on matters. Windows has paths with this slash \\. Unix, Mac and Linux go with this ather slash /. This will matter if you install a Git client that works as if it was Unix. (I.e.: something we are going to make in a while.)
- different command lines tools may use different shortcuts for useful operations like copy and pasting. If you want to copy a git command into https://git-scm.com/download/win you may have to use **SHIFT + INS** instead of **CTRL + C**.
- in the command line the star character *\*  will match everything (see later on when we are going to talk about *regular expressions*). This feature will be useful in a while when you are going to commit only your Python and Markdown files, i.e. those ending with .Rmd and .py.

## Version Control with Git

Git is a *version control system*. Think about it as a form of Dropbox on steroids or some enhanced Google Drive. Forget shared spreadsheets, common folders or databases with modifications. Git will do it for you: it will save every change you make and it will allow all your team-mates to see what you did. If something gets screwed on the way, you can rollback.

You can freeze instances of your files and their state. If you and your colleagues work on something and then discover your Department webpages is horrible in its version 7.41 and need to go back to the 1.23 one you go back there and restore it.

It's like rolling back your holiday photo album, with perfect annotations. Can we get the picture of me wearing the black coat on the sea after we went for a pint? Yes, *that* level of details.


Git is also where you *cooperate* with people and make your files accessible to others. Random strangers (if you want to) can see your files and then contribute changes to them. You can review them and, if you like what you see, accept the change.

Think about people reading your papers, checking the data (if any) and being able to fix typos without the need to download the paper, send you an email, you opening the mail, fixing the typo, re-uploading the paper, etc.
Not to mention that, well, if your paper is somewhere onto a journal chances are you are not able to fix the typo.

If this sounds too complex or too good to be true, Git is nothing but a command-line interface tool. You are going to open a terminal (by now you know terminal or bash or shell are kinda equal) and type your commands there.

Fun facts:

- git shell is extremely user friendly (in terms of how friendly a CLI can be);
- git-related commands in the git shell start with 'git'.


In an organization collaborating and developing things git can't be avoided. If it is, either there's something similar in use or nightmares are gonna be there.

## Installing Git (on Windows)

To access this magic-git world we have to install it. You've been warned: "First weeks at *HumanDemia* are going to involve quite some installing tools".

To download git, head over there and pick you the version you like the most (a download should start automatically): https://git-scm.com/download/win.

As you finish installing in, as soon as you right-click into a folder, you are given to extra options:

1. git GUI here;
2. git BASH here.

You know which one to choose. The 'here' means 'in the path you are right-clicking into'.

### Git and GitHub

Before moving on we need to clear this: what's the relationship between Git and GitHub?^[IT and programming stuff are full of names looking close to each other, like Java and JavaScript, R and RStudio, etc. There's also a wonderful meme explaining the difference and/or relationship between Git and GitHub. Feel free to look for it.]

This time we are quite lucky. Git is the version control system technology. This is how you manage your files and projects. Once you have the Git client installed - what we installed in the previous section - you are ready to unleash the git powers.

**GitHub** is the social version of Git in the form of a web-based platform where you host your repositories using Git commands. Hosting your repository on an extra platform allows you to back up your files, access them from any machine, etc. On GitHub you can have both private and public repositories and, if you work as a big team, institution or organization, you may use an ad-hoc account with further tools to manage more people.

GitHub is also a *kind of social network for developers* and a library of code. Git powers your interaction with the repositories: updating files, modifying them, etc. The kind of code on GitHub varies: you can use git commands to **push** into your **repository** (hard git jargon here) all kinds of files, from Python to Java, to SQL, Ruby and also .doc files if you want. Also, most of the instructions and textual files there are written in markdown, so your previous week building *HumanDemia* Universal Typing Machine was well spent.

If you have already head over GitHub you know that there you find repositories. **Repositories** are the main containers on GitHub. You put your files there and organize them. They are your folders and allows you too have version control.

Besides creating your own folder, you can browse other people's folders, look into them and do stuff with their files. You can copy these files (*clone* in Git jargon) and you can contribute the projects (which requires you to *fork* the repository).



## Git Operations and Mechanics

Ok, now we have a git terminal installed.
We know:

- that we can call it by 'git BASH here';
- that git commands start with git.

The next step is to figure out what we need to type after the git key, to have something git-related happen.

Before moving on, setting up a GitHub account to experiment with would be cool.


### Creating a New Repository and Add Contents

It is time to start using GitHub. Here's a condensed summary. Remember that if you need further help the documents on GitHub are great, check them out (https://help.github.com/en/github).^[Good documentation is fundamental if you want an open project to have an impact. And that's great for us to have great documentation to learn from. The issue is learning how to learn from the documentation.] 

The basic operations we are interested in are the following:

1. creating a repository;
2. importing a project on GitHub with the command line;
2. cloning a repository;
3. sending content to a repository;
4. forking a repository and contributing with pull requests.

The easiest procedure to create a repository looks like that:

- go on your GitHub page, up on the right there's your profile menu. Clik on **repository**.
- create a new repository: there's a green '**New**' button that wants you to click on it.
- open it: that's self-explaining.
- **clone it**: Git-jargon to say copy (no Blade Runner here), this requires further steps;
- add files to the repository (see in a while).

### Copies on Git: the '*git clone*' Command

'**Clone**' and 'cloning' are git essentials. When you (git) clone something you are making a copy of something that is on git onto your hard disk.

The command is pretty straight forward. The operations you want to do is **clone**. You are running a command in the git shell, so you know that the magic formula to obtain what you want has to be 'git' + what you want to do. So here we want:

**git clone**.

This tells the shell to download a copy in the folder you opened git into. What's missing is the url of the repository. So if you want to download the impressive list of free programming books by the EbookFoundation you need to type the following:


**git clone**
**https://github.com/EbookFoundation/free-programming-books.git**.

This will create a folder called 'free-programming-books' with all the contents.

Summing up, to clone the repository you need to:

1. copy the https of the repository you've just created;
2. go into a directory you want the repository to appear (bonus points if you are doing this in command-line);
3. git bash into it: this is where the command-line comes in. Now we are in the Git BASH shell;
4. type "**git clone [yourrepositorynamehttps you had in step 1]**". You are now invoking a specific command - git clone - and the shell knows what to do with it. Now bash can make you a sandwich.

*Congratulations, you've cloned your repository!*

(**Spoiler time**: cloning will also play a role when you want to send changes to someone else's work. In fact, you'll need to **fork** (Git jargon, again) the repository you want to contribute to and then clone it.
Once you are done with that, you can commit your work to the repository. Once this is done you can compare and contrast what's going on: if you added files, deleted some or modified something. All your history will be saved and you can go back to the picture you like the most.)

### A Practical Cloning Example

Ok, let's have a practical example. Suppose you bought Joel Grus's *Data Science from Scratch* (which you should read).
You create a folder on your desktop to work on the contents of the book.

Bonus points if you used a 'mkdir'. There you plan to copy some examples, develop some projects, etc.

Then you realize Joel has all the code for the book in a GitHub repository and decide to get it. Here's what you have to do:

- go into the folder you created for the book, e.g. "C:\\DSscratch"
- right-click and select 'git bash there'
- clone the repository, i.e. type 'git clone' https://github.com/joelgrus/data-science-from-scratch.git (that's the link you get in Joel's book repository - notice something going on with slashes...).

### Git: Pushing New Contents into your Projects with '*git push*'

**Push** is the Git jargon to say you are contributing content to a repository. To do that you first have to tell git that a certain file needs to be tracked by git.

The relevant command is:

**git add [filename]**.


Through git add you are going to include a file to tracking and version controlling. Git will take care of all the pictures in which the file appears, to keep using the photo book analogy.

Once you have added the files you want to add to your repository, type

**git status**.

You should see why the git shell is user friendly. The command shows the status of your folder: which files of those present in the folder are tracked (green) and which are not (red).

The shell also tells you what to do to remove a file from tracking ('**git unstage**') and to add more files ('**git add**', again).


Adding is not enough. Going back to our picture analogy, you have the picture that you want to store in the repository. But maybe that's not the right one you may take another one and another one. To put the photo in place you need to do two more options.

Once you are ready and sure you've added all the relevant stuff, you can commit your additions and changes. Go:

**git commit -m "message"**.

The -m and message are there to simplify your future work. You want to clearly say what you did. Did you add a functionality? Clean the codebase? Add a picture? That's your commit message.

Only now you are ready to push it. So:

**git push**.

You'll see git sending your files to the repository. In case you are committing a file with the same name as something already in the repository, git will check for differences and merge them. Your latest committed file will rule over the one present before.

In this way, git will check for merge conflicts and, if something calls for your attention, it will ask you to choose. Remember that git can be used in teamwork. Suppose you modify something and also someone else in the team committed changes to the main project. Alas, your change and that of your colleague are conflicting.

What should you do?
Summing up, *this is how you put content on your repository* ('repo' in git talk):

- *git status*: check for differences;
- *git add*: add all the files;
- *git status*: check you've added the right stuff;
- *git commit -m*"write the commit message": this message will help you reconstruct your history of changes and development;
- *git status*: check everything is right;
- *git push*: actually pushing (and storing) the stuff you have committed.


### Adding Files Matching Certain Conditions

Adding files one by one can be boring. Imagine you have a book with 10 chapters. Do you really have to type 'git add [filename]' for 10 times? The git shell is CaSeSensitVE so there are changes you are going to make typos (*fit add* is my favourite).

Luckily, when we installed git shell we get a whole command-line interface that is Unix-based. This gives us access to powerful commands.

The first is the \* star character which means 'whatever', 'everything' or other ways that helps you to conceive 'all'. In our 10-chapters book scenario, it means that you can type:

**git add \* **

and you will add all the files.

This is a nice solution, but it can be problematic. What if you do not want to add all the stuff but only a part of it?

Maybe your folder has both .Rmd files and .pdf, .html and .docs. You want to add only the markdown sources. How can you do that? The \* comes useful. You want to add whatever ends come before the proper file extension, namely: \*.Rmd.

Once you've found this out, you can type it in your git add query:

**git add \*.Rmd**

(adds all files ending in .Rmd).

Check that it works with '**git status**' and be happy about that.

There are two further elements in a git repository worth knowing:

- **git ignore** file(s);
- **readme** file.

The first can ease up the task we did right now, the second details the scope of the repo.

### Git Ignore

If you are working on a project with many files that have a different extension and you only care about selecting a few of the files, there can be better ways than using small selecting bash commands with the \* character.

What if you could tell git to ignore certain files? (E.g. all the pdf and doc outputs of your book, all the files in the resources folder, etc.)

Git comes to the rescue with a specific file, the **gitignore** file.

A git ignore is a file that tells git not to consider certain files when you perform a git add operation. You may need this to avoid that some auxiliary files that are due to compiling or execution are added to version control, or you don't want to commit some data that you keep local. Git ignore files have their own syntax and rules, see here https://git-scm.com/docs/gitignore.

Note that if you want GitHub to render your Markdown the files need to end in **.md** and not in **.Rmd**.^[At least as of the time of my writing and committing this.]

### Git Readme

If you go on GitHub and create a repository there, it will tell you to initialize it with a Readme file. Readme files are written in markdown and GitHub renders them automatically.

You can use the file as you first commit. When people visit your repository the readme is displayed and rendered.

Use a readme file to tell people about your project. What is its development status, where to find the documentation to use it and how to contribute to your project.


### Forking and Contributing to a Project: Pull Requests

Forking combines all the operations we did up until now. When you fork you are creating a further copy on GitHub. You use your forked repository as you did with your previous ones. You can then select some of the work you did and push it from you forked branch to the main branch (i.e. the one you forked).
This is called **pull request** in git jargon.

Once you do that the owner of the forked repository will evaluate your changes and decide whether to accept your pull request or not. If this sounds all too technical and scary GitHub has more than one project to help you make your first forked contribution without fearing of messing around a complex database.

Here's the tutorial for first Git contribution via pull-request: https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools.

### Merging and Conflict Resolution

The same file may be modified in conflicting ways.

You'll notice the conflict when you type '**git status**': you'll be reported "unmerged paths". Your task is:

- identify the file;
- fix the merge conflict;
- commit the chosen version of the file that removes the conflict.

We already know how to make a commit. We can easily see what's the file with a merge commit: '**git status**' will tell us at the end.

All we need is to figure out how to find the merge issue and fix it.

All we need is a text editor and to open the relevant file.

Conflicts are displayed with the following syntax:

1. **<<<<<<<** - marks the beginning of a conflict;
2. **=======** - divides the options: the text above it is what is in your proposal, the one below it is in the other proposal;
3. **>>>>>>>** - signals the end of a conflict.

All you have to do is to pick one of the two and then remove the crutches that signaled it. Then you are ready to commit your solution.

(That's the easiest case of conflict: things can get more complex if they involve removing files, like you updated the **OLD** draft paper and your co-authored worked on the newer draft and, being the efficient co-author she is, delete the old one.

No panic, here's how to fix that: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line#removed-file-merge-conflicts, Git stores it all.)



## GitHub for the Humanities

"Wunderbar," you think. You are leveling up your Git-fu, still, you are wondering why *HumanDemia* cares about Git and GitHub. Ok, it's a cool skill to have; ok, you can remove shared calendars and other bad stuff from your academic routine. But aren't there already social networks for academics? What are we leveling up, if any?

Well, it looks like they are advocating quite a bigger change. These are their pleas for GitHub:

- everything you find on [Enter your favourite academic social network] is *behind a log wall*. People can't see, people can't read. On GitHub, you can read and browse repositories even if you are not registered on git. Logging in is required to edit and submit pull requests.

- Further, assume someone reads your stuff and sees a typo. Are they going to write you an email about that? Maybe not.
What if people reading and spotting a typo could notify you and you have the opportunity to accept their suggestion without any boring reopening of the file, correcting it, etc.?
**GitHub** makes this all possible and leightweight. Ok, forking a paper to notify a typo is arguably not GitHub standard usage. But notifying bugs and developing projects is the standard. Academia-wise, papers are projects and typos are little bugs.

- GitHub is changing and evolving. Humanities and academia are... maybe. Why can't we think of GitHub as the place to host collaborative drafts?^[ArXiV papers and papers storing databases link to GitHub. GitHub hosts Jupyter notebooks with conference presentations. It seems that we don't need a new vision or a highly innovative insight. Looking what's around and connecting the dots should be enough.]

Try this and use it in your next grant under the heading of cooperation and dissemination.

It takes a little effort and opens new opportunities. At least it brings your dropbox and stuff to the next level.

## Summary

Chapter 3 was all about command-line interfaces and Git. You installed a git client and refreshed CLI operations.

Cloning, forking, git push, and git pull are no longer a mystery for you.
Then there are other git commands.


### List of Git Commands and CLI Commands

Here are the Git commands we should be familiar with:

- git add
- git status
- git push
- git pull
- git commit -m "message to commit"



Besides these git-commands you have refreshed/learnt some of these command-line magic:


- dir
- cd
- '..'
- '.'

And learnt to use the star character (\*) to match all files having a certain ending.

### Shortcuts

As far as shortcuts are concerned:

- **WinCmd + S**: open Windows search bar (e.g.: to run the Shell)
- **SHIFT + INS**: past on Unix (i.e. CTRL + V)

Command-line commands do not qualify as shortcuts, but you may imagine them as such as they shorten the word they refer to. It is never the case you refresh them enough:

- dir
- cd
- '..'
- '.'



### More Resources

- If you feel already a bit confidente about your Git Fu and want to go practice right away **with graphical feedback** check this out: https://learngitbranching.js.org/.

- The *Learn enough* tutorials are close in spirit to what *HumanDemia* wants you t be able to do. The good news is that there's a "Learn Enough Command Line to Be Dangerous" https://www.learnenough.com/command-line-tutorial/basics

- The *Pro Git* book (https://git-scm.com/book/en/v2) is free and will teach you everything Git related. Internals are revealed and blackboxes are cracked opened.

- Nice tutorial on using GitHub and sharing code in your organization. Show it to your team, faculty and Dean: https://towardsdatascience.com/towards-open-health-analytics-our-guide-to-sharing-code-safely-on-
github-5d1e018897cb (At *HumanDemia* they are doing it already)

- The Git cheat sheet is something useful to read and bookmark: help yourself here: https://github.github.com/training-kit/downloads/github-git-cheat-sheet/.

- That's the tutorial for first Git contribution via pull-request: https://github.com/firstcontributions/first-contributions#tutorials-using-other
-tools

- The programming book for the Arcade library (yes, use Python to program videogames!) have a wonderful tutorial for some git setup and git cloning operations. Still, they use Bit Bucket instead of GitHub. https://arcade-book.readthedocs.io/en/latest/chapters/04_version_control/index.html

- Python migrated its code development process on GitHub with a specific Python Enhancement Proposal (PEP) 512:  https://www.python.org/dev/peps/pep-0512/.

### Further Work

There is quite a lot you can do to practice Git-fu:

- Create a repository (maybe a private one). Add some content there.
- Try the first contribution tutorial.
- Clone the free programming resources repository (if you haven't already): https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools).
- Create a conflict in one of your repositories and fix it. (To do that you'll need to create to branches on your own. Yep, *curved ball*!)
- Persuade a colleague and/or friend to embark on this Git thing. Tell them to buy the book. Use git as a logger for your reading group and to develop further experiments. If something good comes out of that, fork the book repository file and contribute.
- Practice graphically on https://learngitbranching.js.org/.
- We discussed walking through a file path and listing contents with **dir**. It's time to look ahead into Python and practice some reading the documentation. Have a look at the **os module** (i.e. the one about operative system) and check what **os.listdir()** and **os.walk()** do: https://docs.python.org/3/library/os.html (feel free to read the rest of the documentation, but focus on the two mentioned functions).