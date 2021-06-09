from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey Bot is bout ot response!!'

@app.route('/botrespo',methods=['Post'])
def sms_reply():
    pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name(.*)",
        ["My name is L.A.L.U from MARS, but you can just call me panda and I'm a chatbot .",]
    ],
    [
        r"how are you(.*) ?",
        ["Badiya Bro tum batao", "I m good u say??"]
    ],
    [
        r"(.*)sorry(.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Ayush created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) live?",
        ['Mars ',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) fav (moviestar|actor|actress)?",
        ["Hero Alom"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['Sorry I am created for fun as not made on tranformer or bert....please treat me as a nltk bot :(..']
    ],
    ]

    my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
    }

#Create Chat Bot
    chat = Chat(pairs, reflections)

    msg = request.form.get('Body')
    resp = MessagingResponse()
    resp.message(chat.respond(msg))
    return str(resp)

if __name__=='__main__':
    app.run(debug=True)