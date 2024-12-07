# Hello World!!! Welcome to my Media Experiment 2 

# This is a Python program about Python.

# This exists in two dimensions which is how code typically can be experienced: the plain text which you can copy and paste anywhere really. And the actual function it comits once you run it inside an editor. 

#This program was coded inside visual studio code. Use of AI is strictly prohibited in this class so I think it is important I mention that despite my previous use to aid my code learning it was not used here. To follow rules but also...a challenge for myself :) Also because this project can be used as commentary on AI. 

#Important notes/prefaces: I am 4ish months into my coding journey. I love it, it excites me but it also deeply puzzles me. I wanted to challenge myself with this project but I also wanted to turn it in on time. I want to thank Rae Bruml Norton for teaching me almost everything I know code wise and my code as liberal art peers they rock. Secondly, if questions arise around running it and how let me know. I designed it so that you should be able to interact with it from your computer's terminal. If it crashes you can also contact me...However!!! crashing is an intrinsict part of code so maybe that can add to the sort of analysis we are doing, yes? 

#Ok enough me just talking here it is, enjoy: 

import markovify #this is a library. Most programming languages have these, however, Python is known for its vast and diverse range. 

print ("\nWelcome to my Media Experiment 2")

user_input = input("\n Would you like to hear about Python? (yes or no): ").strip().lower()

if user_input == "yes":
    text = open("analysis.txt").read() 
    print("\n\n\n")
    print ("\n The Medium Is The Message..\n") #i fed the machine my own analysis 
    print ("\n The Medium Is The Message..\n")
    print ("\n The Medium Is The Message..\n")
    generator = markovify.Text(text, state_size=1)
    paragraph = ""
    for i in range(80):
         paragraph += str(generator.make_short_sentence(80)) #this program is generative, each time you run it you will get a different outcome. Using the same model of text.
         paragraph += " "
    print("\n\n\n")
    print("python is " + paragraph)
    print("\n\n\n")

elif user_input == "no":
     print("This is so active audience theory of you...However, I am IBM and for this to work I need you to say yes, so stop critically thinking and making your own decisions, please say yes!!")
#messages in Python can be delivered in all kinds of ways with all kinds of audiences in mind. I can say "\n" and wether incomprehensible to a human the machine reads it as a line break. I can type user_imput as a varaible that both the machine but also I the programmer and othes programmers ccan understand. And I can write # comments like this one so that anyone even people who don't know the language can read it, but the machine can't. 


# Original written analysis: 
# Python is a high-level programming language. Meaning that it is easily readable for humans. It is far less abstract than machine code which is the only one that can be read by computers. Allowing coders to focus on the what instead of the how of a problem they are trying to solve.  On the flipside one of the limitations brought on by this is that to be read by a computer it must be passed by an interpreter. By this we also mean that it is not running the actual hardware, say the laptop you run it on. But rather, it creates a virtual environment within hardware that allows the user to easily run programs. This is a key affordance of this kind of programming; it is far more accessible in terms of understanding and physicality. Another dimension of this aspect is that it is open-source. This I can describe as almost inherent to this form of digital platform. However, it is important as it allows for community to be built around it. Its openness allows for code to be built on code. Some other limitations of this kind of language are that they are less fast, precise and efficient which depending on what operation you are trying to perform can be important. I bring up the classification of it as a high level language to say that  it is a media  technology that is built upon many, many, many layers. The Markov library I used in my program can be created by typing more extensive lengthy code. It is based on a mathematical system that was created outside of code. Python was inspired by ABC language which was inspired by BASIC which was developed from FORTRAN II which was developed by IBM. The code I am learning and writing is an abstraction of layers of programming. In many ways it’s like a technological palimpsest. I am writing this code inside an editor on top of a machine that is coded in 0’s and 1’s. And this relationship can be seen the other way around too. Programming languages are the foundation for many of the media technologies we have discussed and many of the digital platforms my peers analyzed for this project.  


# All these previously mentioned affordances and limitations are general to most high-level languages. Now let's look at how python differs in this category. A lot of information distribution and analysis of digital content happens on systems built on python. So while python isn’t for instance instagram, it is a tool/platform that largely helps power it. One of the biggest limitations is that it requires learning, access to a computer, and for larger operations a lot of other parts in order to function. In my analysis I’ve predominantly focused on how it compares to other programming languages but I want to extend that to other media forms. Coding for the average person seems to be done by predominantly white male nerds. That is not entirely a made up stereotype propagated by mass media. In 2014 data from Silicon Valley firms reflected “White employees make up 41 percent of professional jobs and 57 percent of management jobs. This is roughly a positive difference of about 16 percentage points.” (USA EEOC) An overwhelmingly white industry  that codes in a way similar to what Lorna Roth described; Dysconsciously.  In many ways its back-end invisibility and the built by many in layers aspect; has allowed for programmers to code things using python without having to really think about their impact on society at large. One of Python’s most common applications is data processing. In one of our non required texts; Race after Technology by Ruha Benjamin, it is described how data propagates racism within our society.  “In a recent audit of California's gang database, not only do Blacks and Latinxs constitute 87 percent of those listed, but many of the names turned out to be babies under the age of 1, some of whom were supposedly ‘self-described’ gang members’”. (Benjamin, 6) We as society become coded. This becomes even more prevalent when we think of AI. It’s not a new technology, but we are interacting with it in a new way. For it to function programs like python need to exist. In fact the markov library created within Python is used in natural language processing. I am replicating an AI-like function to illustrate that it will deliver what I or we encode into it. McLuhan could be problematic but his notion of the “medium is the message” truly permeates so much of today’s media landscape. 


# A generated Markovify version: 

# python is Allowing coders to exist. In many layers. The Markov library created outside of this we encode into it. One of a lot of our society. This I am replicating an interpreter. That is a high-level languages. I bring up stereotype propagated by IBM. Some other parts in order to say that it to solve. Python is built on what I want to extend that it on. Coding for code inside an abstraction of Python’s most high-level languages. This is an abstraction of digital platform. By this aspect is far more extensive lengthy code. I want to a technological palimpsest. In fact the digital platform. In many layers. The code inside an abstraction of code. In one that largely helps power it. Now let's look at how data propagates racism within hardware that to exist. It’s not running the limitations of other programming language. It is the what I or we encode into it. That is easily run programs. It is easily run it is a problem they are the built on a high-level languages. In many of digital content happens on code. Meaning that to solve. Now let's look at how it is an interpreter. Allowing coders to be important. I want to illustrate that largely helps power it. Python is the flipside one of understanding and many layers. Another dimension of AI. That is built by computers. This becomes even more extensive lengthy code. On the biggest limitations of a new way. Programming languages but I want to easily run it is open-source. So while python isn’t for code I can be seen the foundation for humans. Now let's look at how it will deliver what operation you run it on. In one of this aspect is not entirely a tool/platform that it is that to exist. This is a new technology, but I am writing this aspect is data processing. This I am writing this project. This is far more extensive lengthy code. A lot of the what operation you run programs. The code things using python need to easily run programs. It’s not entirely a new way. Allowing coders to extend that it requires learning, access to exist. However, it is that it as it compares to perform can be built around too. The Markov library I am writing this code inside an interpreter. Its openness allows for programmers to be important. Another dimension of a computer it on. Coding for instance instagram, it requires learning, access to function. And this is easily readable for humans. In my analysis I’ve predominantly white male nerds. I am replicating an editor on society at large. Another dimension of code. By this relationship can be read by mass media. And this aspect is the classification of this kind of AI. Allowing coders to solve. It’s not a high level language processing. Programming languages but we have discussed and 1’s. I bring up stereotype propagated by predominantly white male nerds. This becomes even more extensive lengthy code. It is that to solve. On the what operation you run it is a media forms. In my peers analyzed for many of AI. So while python without having to be done by mass media. Some other way around it. The Markov library I bring up stereotype propagated by IBM. This I want to solve. Some other media technology that it must be passed by a new way. Some other media forms. On the media forms. Another dimension of programming. This is important as it as a technological palimpsest. In fact the average person seems to exist. Another dimension of AI. Allowing coders to a mathematical system that to solve. A lot of our society. That is built by computers. I or we are trying to focus on python. Python is a virtual environment within hardware that largely helps power it. I or we think of this category. One of other way around too.

# Citations Original Written Analysis:
# “Introduction to Python.” 2023. University of Arkansas at Little Rock. February 3, 2023. https://chem.libretexts.org/@go/page/431544. 
# “Diversity in High Tech.” US EEOC. Accessed December 3, 2024. https://www.eeoc.gov/special-report/diversity-high-tech. 
# Lorna Roth, "Looking at Shirley, the Ultimate Norm: Colour Balance, Image Technologies, and
# Cognitive Equity”, Canadian Journal of Communication 34(1), 2009
# Ruha Benjamin “Introduction: The New Jim Code” in Race After Technology: Abolitionist Tools forthe New Jim Code, Cambridge: Polity Press, 2019.
# Marshall McLuhan, “Introduction,” “The Medium is the Message”, and “The Gadget Lover”, from Understanding Media: The Extensions of Man, MIT Press, 1994
# Citations generated Markovify version:
# Miranda Chalbaud Acosta, “ Media Experiment 2”, 2024.




