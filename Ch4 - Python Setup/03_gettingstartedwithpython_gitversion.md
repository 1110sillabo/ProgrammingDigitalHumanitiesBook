# Getting Started with Python: Anaconda, Jupyter Notebooks, Google CoLabs and Virtual Environments {#ch4}

This is the last module in your *HumanDemia* on board. After that, most of the boring stuff will be completed. The environment will be set and you'll be ready to use these new tools to build something and make your life easier.

In this chapter we are summing up what we did in the two chapters before. We need to install our Python development environment (in chapter \@ref(ch2) we used RStudio as an IDE for Markdown). Here we are going to play a game of snakes, and install Python by using the Anaconda distribution.

Through Anaconda we are going to get the following:

- access to the **Python** programming language;
- and IDE for Python: **Spyder**;
- a packet manager for Python: the Anaconda installer (*conda install*);
- another command line interface tool: the Anaconda Prompt;
- the full stack of Python scientific libraries and data analysis libraries (this is going to save us some installation pain): *Numpy*, *Pandas*, *matplotlib* and more;
- **IPython**: a nice interactive shell to program in real time that we've already mentioned;
- **Jupyter Notebooks**: shared work books of Python code - think of them as a git hubbed version of IPython sessions.

As you see, IDE tools (chapter \@ref(ch2)) and command line tools (chapter \@ref(ch3)) sum up here nicely, to give us Python.

The path for this chapter features installing Anaconda, explaining its benefits and then provide details about Google Colab, another tool to perform Python based operations, this time without the need to install any code. There are no excuses not to code.

*HumanDemia* has another curved ball waiting you at the end of the chapter: *virtual environments*. Virtual Environments are isolated containers in which you install all the tools you need to run your program in a safe way, i.e. without interacting with the rest of your system. You don't want an update to Steam to mess up your project, right?

Virtual environments are there to ensure this. That's one of the coding best practices that the sooner you learn, the better it is.

Also, it is something you are going to perform in the Anaconda Prompt. So it is a nice way to sum part I up. "Command line operations of an IDE for something Python related," you mormor "these *HumanDemia* instructional designer have their idea of balance!"


## Installing Python by Installing Anaconda: A Game of Snakes

Back in the days if you wanted to start Python you had to to a lot of researches. There were two main running versions of the language: Python 2 and Python 3. Some of the syntax was different (i.e. how to print on the screen), some of the main tools were only running on one Python version, etc.

Today you can save all this struggles. **Go and install Python 3** (unless you have a reason to still use Python 2, which should not be the case if you are starting out).
Despite the Python versions struggle being over, getting started with Python still has a counterintuitive issue. The best way to get started with Python is **not** installing Python.

Rather, **to install Python you have to search '*Anaconda*'**. As the snake-based name suggests, Anaconda is related to Python. With Anaconda you are going to install Python and more (which is good, as it saves us installation pains).

Installing Anaconda is as easy as to go to https://www.anaconda.com/distribution/ and download the relevant distribution for your computer.^[If you come from Windows as I do, you need to find out if your system is 32 or 64 bit. Right click on This Pc, select 'properties' and you'll find the answer. - If this quick fix doesn't work, here is more on the issue of determining if you are running 32 or 64 bit OS, for all main platforms: https://www.computerhope.com/issues/ch001121.htm.]

Basically while installing Anaconda you will be asked:

1. where to install it;
2. if you want Anaconda to be the default program to run Python files;
3. how to interact with PATH variables.

If there's something confusing, the answer is in the [installation documentation](https://docs.anaconda.com/anaconda/install/).^[For bonus points on Windows and path variables see [here](https://en.wikipedia.org/wiki/PATH_(variable)).]

Ok, now you should have Anaconda installed which means you have Python! *Programming is close*.

If you are impatient and want to start having a look at your IDE for Python, search for "**spyder**" in your system search box. You will then run the Spyder. (Oh, Spyder is another acronym for '**S**cientific **PY**thon **D**evelopment **E**nvi**R**onment').

If you are *not* that impatient, we'll first have a brief tour of:

- the benefits of using an IDE (like Spyder) and the other tools provided by Anaconda, namely:
- IPython;
- Jupyter Notebooks;
- the Anaconda system (package manager and command line interface)

## Using and Integrated Development Editor (IDE): The Benefits of Spyder

Spyder offers a lot of benefits. The one I've found the most useful is that **you can divide your workspace in different cells**. Each cell allows you to run Python code.

The importance of running more Python code cells is that you can have a main cell where most of the program lives and as many cells as you need to experiment. If you need to add a new feature to the main program you can test it in the cell, and then include it.^[With the default Python IDE (called IDLE, from the Monthy Python show) you either have to open more windows or comment out what you do not want to execute when you run your program.]

Plus, *Spyder supports you when you are typing* the commands. Press 'TAB' and it will offer you suggestions about what you can do with certain objects. This also **helps you learning**. Spyder knows your object is a string and will show you the available methods.

As you move your first steps into programming it is likely that make various syntax errors and helps you indent your code properly. Spyder **checks your syntax** and it can check it also against some formatting rules and styles (most notably, PEP 8 style).^[Code is meant to be read, hence the existence of formatting conventions. 'PEP' is another piece of Python-jargon which means 'Python Enhancement Proposal'. This is basically how Python evolves.]

This can be a double-edged sword. As you are about to know, **indentation matters a lot** in Python. *Tabs and spaces are different* and you have to be consistent. Spyder handles this for you, which is cool. You can focus on learning the syntax and approach your problems. But then sometimes you have to start coding in notepad or something else and formatting errors come in from everywhere.

I guess this tells us that we need to be aware and grateful for the amenities an IDE can do, but not to get enslaved by them.

Another great feature of Spyder is the variable explorer. This window tells you a lot about the entities you have in your projects: are they numbers or strings? Are they filled or empty? What's their state? Etc. The more your program gets complex, the more you are going to appreciate that tool. (Again, *having* such a tool is no excuse not to plan on the design of your program. You should be in control of what happens.)

### Running your Code in Spyder

Ok, it's too early to have a session on Python and produce a decent program. Still, given we are talking about Spyder it is good to know how you can run programs from there.

Assuming you wrote some code in Spyder there are two ways to run it:

1. *run the program*: press F5. You will be asked to save your file and then your code will be run, showing an outcome (if the code has no error);
2. *run the code inside a Spyder cell*: you can delimit Spyder cells using the following delimiter line: **\# %%**. If you are inside a cell, you need to press CTRL + ENTER.

*Example of Spyder's Cell -- ch. 4.1*

```{python eval=FALSE, include=TRUE}
# %% 

#cell starts above this line ----
#code of the cell
def main():
    print('Hello world')
    
#cell finishes below this line ---

# %%
```


### Other Popular (Python) IDEs

Spyder is by no means the only IDE for Python. There are a lot of tools about there: free, paid, Python-specific, etc. The recommandation is to explore some of the options, good comparisons are just a search engine search away.

What I like about Spyder is the opportunity to divide and conquer problems by working with cells as well as having an IPython session to work in, all in the same window. This may not work for you.

An option worth considering if you want to expand your coding abilities is Visual Studio Code (https://code.visualstudio.com/). Besides being free and easy to install its main benefit is that **it allows us to code in a huge variety of languages** (different programs requires you to add some plugins and learn to compile, if needed).

In a few clicks you are going to have access to the possibility of running code in Python and other tech-tools you may be interested in like: HTML, JavaScript or Ruby. If you want to go into app development with Java, you can. And all the flavours of C-languages are supported.^[Also, if you are working with a large number of files maybe you'll find it easier to manage them with VS Code.]

## IPython

IPython is an *interactive shell* to run Python commands. Contrary to the Python code you write in Spyder or Python editor, if you press 'enter' inside an (I)Python shell that code is immediately executed. No need to run it.

Working in the shell allows you to have faster responses. You type the commands and see if they are doing what you want. Prototyping in the shell is fast and it is also useful to stay in the shell after running a program to see what happened.
IPython is perfectly suited for this and much more.

In fact, the 'I' in IPython stands for *interactive*. Interactivity is gained by tab completion of commands (as in Spyder) and by putting you close to your code. If you don't know what's the type of a certain object you simply ask the shell and it will tell you. Just write **type(object)**.

Further, you can use a question mark '**?**' to figure out what the various functions do if you don't remember them or if you are simply curious. In that way you prototype code *and* interact with the documentation of the module you are using.

Besides that, IPython offers you special methods (sometimes called "magic methods") that you can use to measure how long does it take to run your code and much more.

## Jupyter Notebooks

Jupyter notebooks are a nice interaction of *code* and *text.* You run your code in cells or chunks, as in Spyder. Nonetheless, in a Jupyter notebook a cell can also be a text chunk (written in *Markdown*).

This allows to write tutorials in which you discuss a problem and then present the code. The code, then, can be run in the browser. So when you are following the tutorial and run the code, you see the results of code execution.

Jupyter Notebooks are perfect for portability. Still, you need to have the dependencies and modules installed on *your* machine. (With Google CoLabs, see below, this is no longer an issue.)

Jupyter Notebooks are nicely integrated in the Anaconda/Spyder workflow presented here. All you have to do to open a Jupyter Notebook with Anaconda is:

- open the **Anaconda Prompt**;
- go to the folder you want to create a notebook into (i.e. use **cd** to change directory and **mkdir** to create a new one, if needed);
- type '**jupyter notebook**'.

The notebook will be created and you'll browser will open in the notebook. (To close the notebook get back to the conda shell and press 'CTRL + C'.)

Oh, there are controversies on whether Notebooks are as super good as they look like. Search 'notebook skeptics'. 

## Command Line in Action: the Anaconda Prompt


Git was a reason to see the importance of command line interfaces. Anaconda is a further proof. While coding you'll need to install new libraries and modules (we do that for laziness: we go through installation pain to have access to functions and commands that were programmed and optimized already - there's no need to reinvent the wheel).

Anaconda comes with its own command line interface called "**Anaconda Prompt**". Just search for it in the Windows search bar and start it. You have a command line tool. As it was the case with Git, the Anaconda Prompt has a reserved word to specify you are going to use specific Anaconda commands. In this case the magic word is **conda** (all the 'common' command line commands like 'cd' or 'mkdir' are stilll valid).

Typing '**conda**' plus something allows you to run the commands and interact with your Anaconda version. The name of the tools ('jupyter notebook', 'spyder') open the corresponding tools.

The commands we need to learn allow us to: *install new Python components*, *update the Anaconda system*, activate *virtual environments* and *operate Jupyter Notebooks*. Try to guess these commands before moving on.

### Basic Anaconda Prompt Commands

Anaconda Prompt Commands are pretty straightforward:

- '**conda install**' is used to install packages, e.g. **conda install pdfminer** (sometimes there are specific flags to be added or different channels to download your packages from. Just search 'conda install [package]' and you'll find detailed instructions, e.g. https://anaconda.org/conda-forge/pdfminer);
- '**conda update**' is your choice to update the whole system;
- '**jupyter notebook**' creates a Jupyter Notebook the folder you are into (as you have already seen);
- if you want, you can type '**spyder**' in the conda shell. This will open the IDE;
- to configure virtual environments the things are a bit more complex. Here's an anticipation of the first step: 
**conda create --name [environment name]** (see later to have the full picture).



## Google CoLab or Python on the web

The last option to consider to get started with Python is **Google CoLab**.
If you want to try out Python and don't want to mess up with installations just go over to https://colab.research.google.com/ and try out Google CoLab.

Here's their explanation of the platform:

>>>What is Colaboratory?
Colaboratory, or "Colab" for short, allows you to write and execute Python in your browser, with
Zero configuration required
Free access to GPUs
Easy sharing.

Nice, isn't?

Basically you will have the architecture of Jupyter Notebooks that you can run on Google's machines. Notebooks allows you to mix Markdown language and Python code.

If this doesn't look exciting enough, the platform has many built in tutorials on data analysis and machine learning (see in the resource section).

Beware that there's a price for our installation lazyness and for accessing their computational resources: Google/Alphabet gets access to *your* code.

## Virtual Environments: Preview into Coding Best Practices

When you program, it is good to keep what you are developing in isolated compartments. You don't want a system update to crush your program, neither you want some new module you download to interact and conflict with what you have.

Given that, wouldn't it be nice to keep different programs in different places that do not interact with each other? The answer is **building virtual environments**.

Working in controlled environments is a *universal coding best practice*. No matter what language you are working in, you want software development to work in its own isolated compartment. There's a lot on coding practice (both Python specific and general) and it is good to start as soon as possible with that.

To build a virtual environment in the present Spyder/Anaconda setup we need to:

1. call the **Anaconda Prompt**;
2. type '**conda create --name [environment name]**' (you can specify what packages do you want and which versions, e.g. *conda create -n myenv python=3.6 scipy=0.15.0 howdoi, arcade*);
3. now the environment is created, but it is not active. To active the environment, type: '**conda activate [environment name]**';
4. once you have finished working in the environment, you have to deactivate it. To deactivate the environment, type: '**conda deactivate [environment name]**';
5. as you start creating environment, you may be confused as far as what environments you have created. To print a list of all you created environment type: '**conda info --envs**' or '**conda env list**';
6. to remove the created env, type '**conda remove --name [environment  name] --all**'.

Ok, we now have Python installed with Anaconda and are acquainted with Spyder. We also managed to create a virtual environment for your development.
All you we need to do to start coding is running Spyder inside our virtual environment.

This requires some further tricks. First, read this https://github.com/spyder-ide/spyder/wiki/Working-with-packages-and-environments-in-Spyder
(especially under the heading of "the modular approach").

Summing up, this is how it worked for me:

1. Activate the environment in which you'd like to work (e.g. with '**source activate myenv**' on macOS/Linux or '**activate myenv on Windows**'). Suppose you installed the arcade library into an environment call arcade. To activate it type: '**conda activate arcade**';

2. Install the *spyder-kernels package* there, with the command: '**conda install spyder-kernels=0.*; **'

3. Once you have everything up and running (i.e. you created the env and installed all you need there). **Run spyder from conda prompt with the environment activated**. To do that, type 'spyder3' or  cmd /c spyder3.exe and you'll have the dependencies loaded in your environment.



## Summary

We are ready to go. Python is there on our machine, installed through Anaconda. We have access to the Spyder IDE and we are ready to start programming.

We know how to install packages, develop in safe virtual environments and how to make our learning experience interactive (IPython, tab completion). Many of these operations provide us with opportunities to enhance our CLI-Fu.

We are ready to move to part II and actually learn programming.

### Conda Prompt Commands

Here's a summary of our new learnt conda command line commands:

- **conda update**
- **conda install [package]**
- **jupyter notebook**
- **conda create --name [environment name]**
- **conda activate [environment name]**
- **conda deactivate [environment name]**
- **conda info --envs or conda env list**
- **conda remove --name [environment  name] --all**
 
Shorcuts of the chapters are Spyder based and are two ways to run code:

- **F5**: run the whole script;
- **CTRL + ENTER**: run code inside a cell (in Spyder).

### More Resources

Let's start with some resources on interactive tools:

- Here's the IPython intro tutorial: https://ipython.readthedocs.io/en/stable/interactive/.
- Here's a tutorial on running a Jupyter notebooks with Anaconda on Windows with step by step instructions and pictures. (https://pythonforundergradengineers.com/opening-a-jupyter-notebook-on-windows.html)

Let's now move to Colab tutorials, i.e. a great way to explore the Colab tool and Python notebooks in general.

-  Intro to pandas: https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb
- tensorflow programming concepts: https://colab.research.google.com/notebooks/mlcc/tensorflow_programming_concepts.ipynb
- charting data: https://colab.research.google.com/notebooks/charts.ipynb

There's something more you want to check about code editor: **LightTable**. Open-source, real-time feedback. And more: http://lighttable.com/.

We have just scratched the surface of virtual environments, read more on the docs: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Book-wise:

- IPython and its use for data exploration and programming being aware of performances is presented in Jake VanderPlas *Python Data Science Handbook*, ch. 1.
- IPython is presented in ch. 3 of Wes McKinney *Python for Data Analysis*.



### Further Work

Installing Anaconda was the main task of this chapter. Still, there's something more you can do:

- Go on GitHub and find a couple of Jupyter Notebooks you like;
- make a notebook explaining how nice is GitHub for humanities;
- R has notebooks as well. Have a look at how they work in RStudio. (Yes, by now you know 'have a look' means 'read the docs');
- you can have virtual environments *without* Anaconda. Anaconda is there to simplify things with its shell. Find out how to work with virtual environments and packages installation outside the Anaconda environment. (*Hint*: you have to learn what the '**pip**' acronym is in the Python world and how it works).


# (PART) Conquering Python {-}
