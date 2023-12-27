from random import choice

intro = ('what is your name', 'who are you', 'who is this', 'are you bot', 'introduce yourself', 'tell me about yourself', 'yourself')
replyForIntro = ('Hello, I Am Howdy. I am an AI powered speaking assistant')

creator = ('who created you', 'who bilt you', 'who made you', 'who is your owner', 'who is your creator', 'who is your boss', 'who is your master')
replyForCreator = ('I was built by Imran Al Munyeem who is a Software automation engineer with over 2 years of experience')

hello = ('hello', 'hey', 'hii', 'hi', 'hai')
replyForHello = ('Hello, I Am Howdy .', "Hello there, yes, Nice To Meet You Again .")

bye = ('bye', 'goodbye', 'tata')
replyForBye = ('Bye bye.', "It Will Be Nice to Meet You again .", "Bye.", "will see you again")

appreciate = ("cool", "nice", "awesome", "amazing", "good",)
appreciateReply = ("That's my Pleasure", "Thank you", "You're welcome")

stateEnquiry = ('how are you', 'are you fine', 'are you okay', 'are you ok')
replyForStateEnquiry = ('I am fine, thanks for asking!', "I'm doing Great", "I'm Absolutely",
                        "I am alright, hope you're doing well too")

question = ("what can i do for that", "what should i do now", 'do you need a update')
replyForQuestion = ("Update me more", "Code me with machine learning algorithms", "Code me with Deep Learning algorithms")

nice = ('nice', 'good', 'thanks')
replyForNice = ("Ohh , It's Okay", "That's my pleasure ", "No worries")

functions = ['functions', 'abilities', 'what can you do', 'features', 'what can you do for me', 'what are your abilities', 'what is your ability', 'what else can you do']
replyForFunctions = (
                     'I am fullfilled with advanced automation functionalities, machine learning and deep learning algorithms'
            
                     )

jokeReplyQuery = ["I don't think this is a joke", "Sorry for this bad joke sir I got this from Google", "This is really a nice joke I love this one"]

sorryReply = ("Apologies,I'm not yet Programmed to do that", "I'm sorry, That's beyond my abilities", 'Sorry, I did not get your point')


def jarvyChatBot(Text):
    Text = str(Text).lower()
    try:
        Text = Text.replace("jarvis", "")
        Text = Text.replace("javed", "")
    except:
        Text = str(Text)
    for word in Text.split():
        if word in hello:
            reply = choice(replyForHello)
            return reply
        elif word in bye:
            reply = choice(replyForBye)
            return reply
        elif word in appreciate:
            reply = choice(appreciateReply)
            return reply
        elif word in nice:
            reply = choice(replyForNice)
            return reply

    if Text in question:
        reply = choice(replyForQuestion)
        return reply
    elif Text in intro:
        reply = choice(replyForIntro)
        return reply
    elif Text in creator:
        reply = choice(replyForCreator)
        return reply    
    elif Text in stateEnquiry:
        reply = choice(replyForStateEnquiry)
        return reply
    elif Text in functions:
        reply = choice(replyForFunctions)
        return reply
    else:
        reply = choice(sorryReply)
        return reply
