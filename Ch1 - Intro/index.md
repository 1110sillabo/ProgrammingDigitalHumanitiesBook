# Prologue

## The Journey: Welcome to *HumanDemia*

You just joined *HumanDemia*, a new hi-tech campus focused on Humanities.
It is actually nothing futuristic. Do not imagine the Los Angeles of the Tyrrel Corps nor Esthar city.

It's a small campus (by US standards) with libraries containing physical copies of books you can touch and borrow.
The notable things are that *HumanDemia* members know the difference between reply, forward and answer all; they can also sort the candidate sheet by student id, alphabetically or by registration date. The strangest thing is that nobody complains about wasting time at the meeting. >Probably they lie.

As you meet the Dean over coffee, she tells you that personal projects are welcomed and that the Uni Council is thinking about integrating a little bit of extra technical competencies into both the staff's competencies and the *curricula*.

You review your classes, talks and academic obligations and you agree on a weekly plan. (In your heart you already know that you'll carry out some of the work while travelling or between meetings students during office hours, but maybe this new place will surprise you. Be it as it may, no way you are going to overwork this tech-stuff during the weekends.)

Your first weeks will be about getting used to the way they work at *HumanDemia*. *HumanDemia* claims to care about research, (open) access to research products and about the time of their researchers. So they stop spending a lot on locked-in solutions and licensing software with big corporations.

(This increased the production of the critical studies by 30% and, most importantly, it doubled their happiness: knowing you can criticize capital and corporations *without* running corporate techs' software you don't know how to fully use is a real banger.)

The Dean tells you that, in the training, you have to spend a week getting familiar with *Markdown* and *RStudio*. You also have two weeks to refresh a little bit of command-line interface (*CLI* in techy-jargon) - as she looks at you she rephrases the 'refresh' with 'learning', as she notices you don't look like you were there stroking keys in front of a PC in the late '80s and early '90s. Then there are and *Git* and *GitHub*. She tells not to worry about Git: "you'll appreciate its potential for cooperation and teamwork," she says.

As you find out GitHub is "*a version control system*", you think that these tech-persons seem to know how to preserve the products of their intellectual work. You shrug away some memories of crushed HDs or stories about "I wrote a paper on an old machine, but it crashed" or your favourite "I may send you the file, but I have no means to open it." (and the joy you caused providing a converted and accessible version of the file.)

Then, she says, you'll have a month or more to pick up some programming. *HumanDemia* faculties work mainly with Python because it is easy to use, but they'll throw you some further hints about other languages as well as a few curved balls. This sounds a little intimidating. Then you remind yourself you are a *researcher*. After all, you think, you should be able to find your way out. Plus, you've read around that tech-persons like challenges.

"Of course," she tells you, "we know that as a research you would like to learn something and put into practice into your work. Based on your application we find out you like building things and getting data. That 'LEGO' item in your interests was highly appreciated... Hence we are presenting you some Python not only for the sake of it but with design goals and implementation in mind."

This sounds promising, but you are still confused. She says not to worry, that you'll find out what to do. That's the reason they hired you. "If you feel you are working as a researcher and wasting your time for some reason, that's where Python may help".

Your mind immediately thinks emails, splitting and merging pdfs to produce a reader for your course or the struggle of getting the data for your always-in-the-making grant application on "Hate Speech on Social Networks in the Post-Trump Era" (you know it has a 200+ characters long subtitle, but you are trying to forget it).

After the Python month(s), you can take some time off your *regular* job. Then you'll spend two weeks on a variety of projects. Some will be suggested but, they say, in a couple of months you'll start *working on your own projects*. Their job will be to prevent you from starting too many things all at once and to ensure you finish your projects.

You say 'yes', doubtful and go away. Training starts next week.


## A Difficult Trade-Off (including Book Summary)

Let's make the Dean's deal more explicit. I want to write a book that gets you started and allows you to write the best programs you have in your mind to fit your (academic and intellectual) needs. Ideally you should be more productive, but what matters is that you feel fine and rewarded with what you are doing.

If you are into research, you are likely to appreciate exploring different paths, building things and trying out options, solve problems, inspire others and help others with the products of your intellectual efforts. If not, you are probably in the game for the wrong reasons (feel free to email me to start talking about it or if I've forgotten good instances of academia stuff).

It's fairly easy to provide some hints on technical literacy or to provide you with some ready-made code for you to copy. But that's neither a good teaching method nor what a researcher deserves.

In fact, the programs you write are something that you have to able to customize. The goal of the book is to get you started by having something that works and that you understand. Something you can extend to better fit your goals and needs.
There's no one-fits-all-solution. Especially when you are dealing with *coding for humanities* (humanities are vast).

The best way to sum this up is probably with this longish quote by Eric Steven Raymond (discussing hacking):

>>>"Learning to compose music has three stages. First, you have to learn the basic mechanical technique of an instrument — fingering and how to play scales. Then you have to train your ear to understand musical patterns. Finally, you must learn how to recombine musical patterns into original creations. Hacking is similar. [..]

>>>The equivalent of playing scales is writing small programs, alone. Unfortunately, playing scales (a) doesn't teach you anything about music, and (b) is boring as hell. Similarly, writing toy programs doesn't tend to teach you much about hacking, and (b) will tend to de-motivate you unless the program immediately solves a problem you care about.

>>>Most formal programming instruction gets to playing scales and stops. Thus, it tends to produce coders who are poor at collaborating with each other and have the equivalent of no ear for music — a poor feel for software design and architecture."^[See Eric Steven Raymond, *How to Learn Hacking*, http://www.catb.org/~esr/faqs/hacking-howto.html.]

Long story short, there are two conflicting needs in this book:

1. the *first* is to offer something that works and pays off as researchers. Time is limited and precious (unless you don't write your "international papers" in something that's not English and you are tenured) and you do not want a super comprehensive book of everything that's available on Python or other programming languages;
2. the *second* is to allow you to understand what you are doing (something you need to do as a researcher, you want to understand what goes on). I'm not there to provide "copy-paste this and get the result" recipes.

Given that everybody will be different, with different backgrounds, stories and with different things that will be either hard or easy to learn, it's difficult to strike a balance that is *balanced* for everybody.

Luckily, a solution (well, a mitigation of the problem) comes from the fact that we got trained in the academia and research is our passion. This allows me to skip on some of the hyper basic step by step tutorial *with images* on installing the tools or *the whole* basic syntax.^[A useful tool to get a quick overview of the syntax of something programming related is the "Learn X in Y minutes" website: https://learnxinyminutes.com/.] I trust you can use a search engine to find this stuff on your own.
I'll explain the concepts and the interesting stuff, and offer opportunities for you to give them your own spin. Still, given the talks and the experience of "talking tech in Humanities", I'll indulge on some basic steps if I've found out they can be tricky.

Sometimes that's going to be easy, others it will be more difficult (there are git commands you have to learn, data structures cannot be super-duper fun all the time, etc.). I mean, after all, you the *HumanDemia* training to undergo.^[But it will be fun or pedagogically interested. There are resources to learn git in a gamified or at least visual supported way.] It is still training. And, despite being "human", it also has some academic reminiscence - so expect your fair share of nonsense...

Also, the shared research background allows us to work on the "start with something kinda known and move into the unknown" approach. The first weeks (part I) include something a little bit more technical than using reply to all in emails that still is not programming. There we'll set our working environment.

After setting clearly the ground *here* and why we should care about coding in the humanities, the book gets practical in chapter [2](#ch2).

With *RStudio* and *Markdown* we build an environment with automated bibliography, control over the table of contents and spell-check.^[It's F7 in RStudio. Yes, get ready for some shortcuts.]

Further, GitHub integration is just around the corner, which means: cooperation with the world. That's what we cover next (chapter [3](#ch3)), and that gives us a chance to (re)discover command-line interfaces (is there anybody from MS-DOS world? or Linux? or text adventures?).

Markdown is also a cool tool to develop a nice logging system^[Feel free to elaborate a way to develop your logging system and bend the tools provided here to your needs. In a way when you start learning you are going to be your main dataset.] and an easy starter for HTML if you are interested into it, and it fosters a "learn, write, master" approach to the kind of perpetual learning you know well as a researcher.

The final step (chapter [4](#ch4)) will be to install *Python through the Anaconda distribution*. This makes our life easier and allows us to get started with Python programming.

We are ready for Part II, the hardest trade-off for the book. There's a crash course in Python and tools to allow you to transition from Python basics to gaining confidence.

Chapter [5](#ch5) is where Python kicks in. Here we stop a little bit on some of the definitions, programming mechanics and data structures. It is generally quite easy to break down the pieces of a problem, like:

1. connect to a search engine;
2. search the term you need for your research;
3. open all the link;
4. read them searching for some specific keywords and see if they meet the requirements to be part of your research.

(This is often called 'pseudocode').^[Sometime Python is referred to as "pseudocode that actually runs". So it's not going to be that complex.]

Still, creating a program that does this might not be so easy. We need to learn a language that instructs our dumb machine friend to do that.
Again, the research-based background will help to keep the crash course contained in this chapter short(ish).

Chapter [6](#ch6) has instructions, warnings and things I wish I had known. I present some of the areas that are mysterious for Python beginners. They vary from jargon and vocabulary issues (something easy to figure out) to more complex things such as understanding Python's internal mechanics and coding for others. (Code has idioms, as well as real languages.)

Given the wide avaiability of tutorials as well as ready-made code we can paste and - if we are lucky - use to get things done, we discuss a bit how to approach tutorials *as learning tools*.
The last part is about the fine art of *reading the docs*. This is vital to get confidence with software and programming.

This chapter ends part II, but you are likely to re-read it again once you are done with part III. In fact, in part III we are going through some programs. We are going to deal mainly with automation tools and search engine processing in chapter [7](#ch7). Chapter [8](#ch8) is all on extracting references and visualizing citation graphs.

## Who's this Book for

The book is intended to serve every curious reader. Basically every human being with sparse access to an internet connection and some time to focus qualifies as that, I guess.

The narration focuses on people with some academic background or doing research. As for the academic background, the book targets people from humanities as they are most likely to be the ones that have had no exposure to code in their curricula.
(Of course, there are exceptions, e.g. (computational) linguistics; media studies, etc.)

I hope the book may help the stereotyped oldish tenured track professors who can't upload the syllabus on the university's website not to bother their Ph.Ds "because you are digital natives" and it will make those making research expand their ambitions (and their dataset) relying on a bigger and broader toolbox.

Maybe as MAs or Ph.Ds you'll start considering parallel careers or who knows. Also, I wish this book can be a resource to self-thought developers (with or without a background in academia) as well.

### How Coding Helps in the Humanities

There are many ways coding helps in the humanities. Some are obvious and should not require a coding book. Suppose you say that "5 tech companies are screwing the world". It's probably a good idea to know who are these 5 (bad) guys and what they are doing. If one of them is into tech and may be operating on sensible data, chances are there's some dirty work to be done.

The same probably applies if you are into 'Data Ethics', 'cryptocurrencies' and other hype worlds 'AI' related (machine learning, deep learning, etc.). Code can help settling legal disputes. (By the way, GDPR and blockchain are pushing lawyers to be aware as developers and some universities have code for lawyers course. Kudos to them.) Suppose we pay taxes online and that there's a norm that allows us to obtain a tax deduction up to X items.

An academic dispute arises on "whether X is included or not". That should be coded into the protocol that allows you to pay the taxes. If you can read the protocol -assuming code is available - you can set the dispute. (If the debate is whether the code correctly implemented the proposal's intent then you still have legit papers to be written, code alone doesn't always help.)

Ok, so much for polemics and things we know already.

Real-life and politics reminds us how our habit change and we (sometimes) can be more effective when a bit of technology kicks in. (Still, beware of what you do with your data. As researchers you should probably know that already.)

Think about paying taxes online (if the site works), online banking, streaming videos vs. going to the Blockbuster, Coursera education and related stuff (Udemy, freecode.org). The Italian reader may even remember Berlusconi's "Tre I" or more recent Movimento 5 Stelle "everything blockchain to achieve transparency".^[According to a study, in Italy, 'technology' means "something you don't understand, to achieve something that cannot be done, but that earns you a lot of votes". Of course the study was never published because of enter-your-conspircy-theory.]

Here's a little list of the benefits of learning *enough* tech-stuff to be *dangerous*:

- better *workflow*: you'll get control of your **data** and **research output(s)**. Your students will be free to access your course material without compatibility issues, you are going to store your material to minimize data loss, you'll be able to produce open data, you are not going to be locked in into specific technologies or software (unless you chose it);
- *cooperation*: you know how to exchange pieces of information properly and how to load them. You are going to pass source codes rather than .pdf if you want people to read them on their ebook reader. You'll edit the stuff on GitHub and publish on ArXiv and stop having things behind a log wall of academia-inspired social networks. (Maybe you have all you pre-prints or papers floating around there, but in this way you save on signing agreements you are not going to respect);
- *practicalities and technical literacy*: you will know the difference between reply and reply all, you are able to sort exams lists, automate multiple-choice test corrections (enough Ph.D mocking!), upload your course materials to your website or even start one (**r blogdown** is your friend);
- *writing (coauthored) papers and editing*: save time performing various checks, managing bibliography, building to different formats. Learn version control to control your data; 
- getting the *data*: depending on your field you'll need to access data. Maybe it's just papers and books. Even there you can stop guessing "the first time word X appeared" and do corpus-based analysis. Or citations graphs. If you need data and evidence to track hate speech online you may download all Trump's tweets and refresh your analysis every hour.

Enough of this. If programming is the opportunity to build our own (small-scale) panopticon, it's all up to us to find ways to produce better research with these tools (gamification of statistics? an analysis of gender biases in Netflix top series?).

A lot of the above characterizations are a parody. (It seems at *HumanDemia* someone told them the onboarding material is better to be fun. Still, as you know, research is based on experience - and in the case above personal experience is part of that.)

### What Coding Can't Do for You

"It is important to be aware of what coding can't do for us". You nod while clicking over the next *HumanDemia* slide.

You already had a similar belief. Coding is an enhancement to your research, it saves you time and allows you to gain access to data that could take ages to be checked by hand.
Still, coding is no replacement for thought or having ideas.^[Previous drafts had "nor having ideas is a requirement for tenure" in the body of the text.] (Coding may be helpful thought-wise: it can be another engine or way to approach a problem).

Although machines can generate text or summarize articles or categories pieces of information, it is still up to you to choose the topic, formulate the hypothesis, etc.
You can write a program that checks every article of a legal code (say the GDPR) and prints a map of all the various references between the single articles. That's super nice and helpful (it appears they have such a project in the *HumanDemia* 'nerdy things' list).
It is still up to you to figure out what does it mean that a certain article is referred the most or whether such a reference is doing any work or rather is it some sort of honorable mention. This latter may be true more in papers than in legal codes: sometimes to add a reference does not amount to discuss a paper.
(Feel free to enter your case.)

You can download all of Trump's tweets and rank the people he mentions the most. But then again it is up to you to figure out and verify if there's any strategy or guidelines in what he is doing. If there's sexism or if he is encouraging to bash some of the people that criticises him. You can measure some other things connected with that. In fact, you may find out that an average unknown professor that happens to be on Twitter is then flooded with insults after some Trump's tweet.

A bit of coding allows you to show that a certain bunch of users were created all together on a social network, that they started to follow some political actor, retweeting specific contents and then aggressively engaging with dissenting voices. That's the way to go about these issues rather than "Enter a Scandalistic post-Cambridge Analytica Title".

If we want to do research (the first draft had 'serious' before research, but that was pleonastic) we need to show something more than what might be perceived as "*yet another big narration*". Especially if the analysis gets political or engages in highly polarized issues.
If we really talk about *critical* discourse, *analytic* thinking, or being *interdisciplinary* (not only in the attempt to get some grant) that's the only way to do it. Embrace programming.

As researchers, we need to offer a way into what we are doing to everybody, dissenting voices included. And everybody will be given a chance to go into the details and check herself.
Aspiration-based and wishful-thinking research belongs all to the same bucket, whether they are Fox News-based, Freud-based or Bertrand Russell-based. That's the bucket of pseudoscience (at best).




## Getting the Most Out of this Book

Let's provide some guidelines for the *HumanDemia* training. (Chapter 6 will iterate some of them and offer more coding-related discussion.)

The training has three parts:

1. we set the working environment. We install *RStudio*, refresh the command line and install *Git* and *mingw* (a port of a Unix shell) and install the Anaconda distribution (which contains Python). In the meantime we get into a more programming-like framework. We start to control our documents and paper. We choose the setting and realize a design. Further, we learn Git cooperative workflow;
2. we learn some Python essentials;
3. we use Python to build something relevant academia-wise. We build our automation tools, scrape bibliography and collect search results. Start thinking how much time you invest in opening the same programs all over again... a text editor, a few websites, etc. Now, assume you boot your pc twice a day and that it takes one and a half minutes to set up and open all your tabs.
If you did that, think about how many emails you can evade in 15 minutes.

As far as Python programming is concerned (part. II), we already know most of the contents of this section as they deal with learning hard-skills. The best way to learn something is to put this into practice, sooner or later.

How do you (learn to) write a paper? You talk with people, read, but in the end you will have to write your paper yourself. More than once actually.
How do you learn how peer review works? By trials and errors (especially if you are not a native speaker) or if you are raised somehow outside the US/UK environment.

I suggest you to try most of the code and methods yourself in a way that it helps you assimilate it. Personally, I like to read books on kindle to get the general picture of what I am doing. That's happens at night or while travelling (people at *HumanDemia* seems to know that, I'd better check what I'm sharing on socials).

When coding is concerned the more exercises I can make, the better. When you code for the first time you may do way more typos and syntax errors than you would by writing a paper in an "ordinary" language.

All in all, there is a reason for them to say "talk is cheap, show me the code". Try to start coding as soon as possible. Once the necessity is there, you'll start diggin' it more.
I'll try my best to propose something that can be useful, academic wise, or fun and interesting. But you should start expanding and flexing all the tools out there as soon as possible.

So let's try to have a list of some advice, but first set the ground with some (hopefully) shared assumptions.

### Assumptions

You are either on Windows or on Mac (instructions here will be Windows-based). You've mainly used MS Word or other branded software to write your papers and do your research.

You may have explored some tools to automate toc creation or managing references. Maybe you move further enough to write in Latex. And you even tried yourself some HTML.

You use a search engine when there's something you don't know before scream *I can't do that* and also specific databases for your work, use WhatsApp or other social media (remembering myspace is no pre-requisite). You have a daily pile of emails waiting for you. You use your uni-based website to display your research or interact with students.

Bonus points if you can print the list of the students both alphabetically and by their registration number (no jokes here, it is not an obvious skill to have; trust me).

Still, for one of many reasons, you never took a deep breath (because you thought you need one) and dive into programming. Or maybe you even tried once, but it did not work, there was no catch. I've been there. More than once (I've actually tried to learn programming 3 times before really starting).

We start from the passion for research and intellectual curiosity. We will build things (mostly) step by step. Thankfully we have a journey into *HumanDemia* to go through.


### Type these Commands In (and Use IPython)

There's a saying about theory and practice according to which theory *in theory*, should not be something different from practice. Nonetheless, *in practice*, that's not the case. Again, talk is cheap, we have to show 'em the code.

It is better to show the code you wrote and understand. There is some time needed to get around the commands and have them at your fingertips.^[There's a whole series of learning to program "the hard way" that focuses on writing a lot of code. Maybe you are that kind of learner. You were given a list of irregular verbs to learn. Reading it was pointless, repeating it didn't help. But you wrote it in your mind by way of writing it 4 times.]

The setup we are going to use offers us many ways to explore a problem or a feature by way of writing code.

Here's a little spoiler for you of IPython from chapter [4](#ch4).

IPython and its shell are great because *they prompt you to try things out*. Type and explore is a great method to learn and figure out what a command does.
Programming languages are languages, and languages need to be practiced. This means that not only you have to understand a concept but also to use it quite a lot.

Music is another language that comes in as a good comparison. It is pretty easy to learn what C major scale is: C, D, E, F, G, A, B. It is harder to play in sixteens notes at a tempo of 160bpm. You will need to play (i.e. type it, out of analogy) these notes quite a lot (and, if you play guitar or similar, you'll have different fingerings and positions to learn).

It is fairly simple to grasp the structure of a major scale (the intervallic structure is: tone, tone, semitone, tone, tone, tone, semitone). It takes some extra efforts to realize that G major is G, A, B, C, D, E, F#. It takes practice and experience to be able to find out on your instrument the major scale you need to best serve your needs on the different chords of a song.

Sorry for the long digression.
IPython offers you a lot of opportunities to start typing out. It further helps you because it offers you a tool to ask for help and know what a command is or what your object is going (just add a **?** - question mark - after the command).

I spent a lot of time in the Python interpreter compiling programs that were too long just to test and learn something new. IPython allows you to move from a type-(compile)-save-run approach to a type and see one. As soon as you find out what you need that works, you can copy your snippet into the main code.

(I know this sounds too good to be true but IPython is free. And in the Anaconda-based setup we are going to use you got it bundled in your main tool for writing code: Spyder.)

### Make it Your Own (and Grow it)

A useful tip I discovered too late - thanks to *Let's Build Instagram from Scratch
with Ruby on Rails*^[If you want to jump on Ruby (or rebuild Instragram) there it is https://www.devwalks.com/lets-build-instagram-in-rails-part-1/.] - is that, while following a tutorial, it is a good idea to change the names of the program you are building and the variable and make it your own. You are not a monkey copying stuff. Ok, retyping is probably necessary to grasp the syntax of something, still, you need to put some of your input.

So, if the code is for you only, name the parts in your own language if that's not English. Write more comments. And, most important of all, once the code runs fine try to work on upgrades.

Can you add a little embellishment? Can you export your analysis of Trump's tweet to a website that updates with every Trump's tweet? Can you make the visualization of the GDPR interactive?

Ok, these are all big topics. Start small. Are you able to identify all the small steps that are there in a tutorial? Can you add a little bit, like "do something super similar to step 5, but different?".

Suppose you are programming a tic-tac-toe game (people at *HumanDemia* has strange practices for choosing who is going to give a keynote talk). Can you make the board larger? Can you save the current board game? (Suppose tic-tac-toe spreads to different departiments and you have to discuss each move at a faculty meeting. Ok, enough of this *PerverseDemia*. Still, this picture sounds way better than the standard faculty meeting, doesn't it?)

Again, let me provide an analogy with music and foreign languages.

If you are into music and are starting out on improvisation, you know what I am talking about. Also, learning a foreign language is a similar example. (After all music, languages and programming languages are all languages).

No matter how many licks or cliches "in the style of [your favourite player]" or how many pre-build phrases ("where is the toilet?", "what's your name?") you've learnt, talking or improvising won't just be repeating this. Knowing chords and notes will help you as it helps to know the grammar. But then performing a solo or chat with others is different. How do you deal with phrasing or your accent? Etc.

*Coding is not different*. There are programming styles and lots of things that, when put in practice, go in a different way than expected.
(This book is the result of my learning experience. It is my first big RStudio project using the bookdown package and Markdown. Most of the projects were the things I needed for my academic journey.)

### Make (Deliberate) Mistakes

Controlled mistakes are good. Well, we can even call them "experiments".

*HumanDemia* kindly invites you to get used to the way a programming language works and what are the reactions you get from the machine when you got things wrong. You don't want to be Trapattoni during that famous Bayern press conference.
There's a better way to learn German auxiliary verbs.
How does that translate into programming? 

We experiment, we modify things. As you learn that to print something on the screen you need to write 'print' (how clever!) followed by a round parenthesis '(' and then you need some quotation mark inside the commas.

There's a lot you can do to experiment here. What happens if you forget a quotation mark? What if you just insert the text between brackets? And what if you add more brackets?

That's the way to go.

### Read the Docs

(Note: there is another section in chapter [6](#ch6) on the art and skill of reading the docs. But we all like appetizers.)

Here is some good news on learning to program: there are a lot of sources and resources out there (some are listed at the end of each chapter under the 'More Resources' heading). Further, each package, language or command is documented by its creator (or, at least, *it should be*).

This documentation is a form of text we need to get used to read and interact with. We know how to read papers in our professional areas. Further, chances are that, as academics, we had to assemble a bookshelf. After all, these papers and books (and desktop pcs) have to go somewhere in the real physical space.

The nerdier out there may have assembled a pc. And, when we were young, I hope we all were exposed to *LEGO*.
Be it as it may, chances are we got exposed to both papers and instruction sets. Now we need to learn how to deal with software documentation.

Papers often have more ideas (if they have it), than data or instructions. Some papers have lots of references and information (e.g. literature reviews) still it is hard to know exactly what "the majority view" or the "most recent consensus view" is. (Programming can help us track down this, as we are going to see later).

On the other hand, the instructions tell us what to do step by step. When you read the documentation of software packages the situation is quite strange.
Documentation is meant to be read by humans, but actually presents you with the commands and instructions that your machine will execute. It is like you are reading instructions about how to make someone else stick the yellow lego over the red one.

So when reading documentation you are reading instructions for the computer and you have to understand why these instructions are valuable for you. Further, these instructions are related to some concepts or tools, but these concepts are kind of presupposed. To abuse the *LEGO* analogy, sometimes reading a documentation feels like buying the latest *"build the Death Star!" pack*, opening the pack and finding only a hundred thousands of small pieces. And nothing else.

Of course you know what you want to achieve and how your program looks like (it is the Death Star, after all) and of course you have some general idea of the building blocks that you are likely to use and the main blocks that a respected Death Star should have.
Still, you thought the package had an instruction book showing you step by step what happens and how to do it.

*Documentation most of the time documents what's in the box*, but it is up to you to create a Death Star or Tower Bridge. After all, packages and modules are tools you can use as you prefer. They are not packages like "Build the Death Star" they are closer to "All nice permutations and tricks with 3 different colours 4 by 2 blocks". Your read this, then it's your turn to (try to) make something.

Major packages will have a tutorial or a quick start (or both). These parts of a documentation will help you getting started and correctly installing your tools. A tutorial will also show you a rudimental implementation of the package's potential. So if you go through the tutorial of Flask (a module that allows you to build web-based applications), you are going to set up a server.^[Like, super early in the fourth line of the quickstart: https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart.]

There are also third party tutorials and demos (i.e. Coursera or Udemy), but that's another story.
In general, the tutorial in the documentation will show you something you can do with the library. Also, GitHub can be searched for documentation, tutorials or code inspiration: it's the world bank of code, after all. Also, the blogging platform Medium has some good articles and software dedicated publications.

### Learn From the Computer Feedback

A program gives you a way different feedback from that of a Q&A session after your first explorative talks.
A computer program executes your code and it has a terminal (i.e. a window) in which it "communicates" with you. If you are lucky you are going to get the result you wanted.

If something goes wrong, you receive error messages. The kind of messages you receive and the information they give you vary a lot across different programming languages and settings, still, it is useful to learn from that.

During the *HumanDemia* training you'll face some nice errors from Git, where the interface will provide you with tips or suggestions like 'X is not a git command. Did you mean git X?'. IPython has some nice traceback errors. When compiling documents with a big RStudio project the log of the errors can be a bit terse.

A major difference from conferences concerns obvious mistakes.
When the shell gives you a precise error message there is no "yeah, I'll have to think about it" or "you know, as they say, my modus ponens is your modus tollens" or even "let's agree to disagree" (did you really ever say that?). You have to go there and fix this mistake.

Also, conferences can be nice and encouraging to first timers or, if your intentions are good, nobody is going to correct you if you say "X criticizes Y" when everybody knows it goes the other way around (and you are actually reporting Y's arguments against X).

If you call your function that computes Trump's followers 'compute_Trump_followers()' but you've called the function 'compute_trump_followers()' the machine won't work. No matter how clear your intentions were. (Yes, Python is **CaSe sEnSItiVe**).

### Ask for Help

You are not alone programming. There are many resources and tutorials out there. And there are search engines to find them (enter: **Stack Overflow**).

Besides your favourite seaching activities, be sure to add Stack Overflow to your searches. That's the place to go for programming questions. If you want to post there, be aware that sometimes answers can be quite direct.

Also, try to look for tutorials and resources on GitHub as well. GitHub hosts mostly code, but it features entire cooperative books out there (they can be updated better than printed version - check out the *Programming Bitcoin Book*, for example), repositories full of resources from programming languages or books in general (look for the EbookFoundation).

Further, if you are stuck while coding you may look for similar programming and see if that brings any *Eureka!* moment to you.

### The Importance of (Keyboard) Shortcuts

You are going to type quite a lot in different environments. If you look at the hand of proficient people, they know how to type. You can invest some quality time to be more efficient at typing.

Also, you should know your shortcuts. You are likely to know ctrl+c and ctrl+v. But do you know how to access the navigation bar of a browser? Or how to split screens or go into fullscreen mode into Acrobat Reader?^[Have you ever tried working with two monitors? Programming and editing are different experiences with two screens.]

(These will help you if you are in a country with a language intimidating enough to make you realize that you can't go to full-screen presentation mode without IT assistance.)

The best way to practice this is to do without the mouse for a while. Also, feel free to time your performances. It's not that bad to stick to the keyboard only.


### Book Organization and Extra Resources

By now you know almost everything about your *HumanDemia* training. Their instructional department seems pretty good: every chapter has a summary at the end.

There are also additional resources and links for the topics covered with book recommendations and tutorials. The further work section has exercises and other things you may consider doing.

If there are (keyboard) shortcuts worth knowing, they will be listed as a recap.

The whole book has a repository on GitHub: https://github.com/1110sillabo/ProgrammingDigitalHumanitiesBook (fun fact: adding the link to the repo required a specific commit).


## Summary

You've finished the brochure of the *HumanDemia* training. You now know what to expect and are happy you have some tools to go through all the material. Some of these tips are not as easy as they seem to be applied practically. (Experimenting, making mistakes, reading the docs, looking for shortcuts.)

You know why the kinds here are important for the academia and are welcome to start thinking about your applications. A final piece advice: *start smal*l. You'd like to have a machine spotting the 20 best papers out of the 200 last published and presented. But 'AI' and 'machine learning' are both hard to be programmed and computationally intense to be performed (hours or days, depending on the task and the software).

### More Resources

Here's a perspective on how to learn to code https://medium.com/@christianalexanderbonilla/learning-how-to-learn-how-to-program
-d3f8b9d37222 (Medium, on the whole, has quite many articles on the topic)

In case you missed the search for free programming books on GitHub here's a lot of stuff: https://github.com/EbookFoundation/free-programming-books/blob/master/free-programming-books.md.

There's quite a lot going on on how to choose a programming language for teaching. Here are some interesting articles:  https://blog.janestreet.com/how-to-choose-a-teaching-language/ and https://www.freecodecamp.org/news/what-programming-language-should-i-learn-first-19a33b0a467d/ and also https://www.drdobbs.com/architecture-and-design/software-engineering-
computer-science/217701907.

Eric Steven Raymond has another great piece about developing an hackinng mentality by way of using the *Incremental-Hacking Cycle*: here it is http://www.catb.org/~esr/faqs/hacking-howto.html.


### Further Work

Research the various stuff that's in the *HumanDemia* curricula. Try to imagine what the things are about if you don't know already. Estimate how complex things are going to be.

Make a list of the actions you perform most often in front of the screen and learn the shortcuts.

Try some: "look, mum, no mouse!" working sessions.

# Part Setting up the Environment #
