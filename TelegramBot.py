import telebot
from telebot import types
from Utils import retrieve_tweets
TOKEN = '867716809:AAGcvZb7K4-zeOWFpNv-nh9bqo0D0TiDCew' 

bot = telebot.TeleBot(TOKEN)
client_list=[]


def setClient(client, coin='', hour=0):
    index =checkClient(client)

    if coin !='':
        client_list[index][1]=coin
    if hour!=0:
        client_list[index][2]=hour

def resetClient(client):
    index =checkClient(client)

    client_list[index][1]=''
    client_list[index][2]=0

def coinExist(coin):
    return True

def checkClient(client):
    for index, client in enumerate(client_list):
        if client[0]==client:
            return index #Existe
    return False   #No existe




    
         

@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    
    if checkClient(message.chat.id)==False:
        client_list.append([message.chat.id,'0',0])

    bot.send_sticker(message.chat.id, "CAADAQADAQADHYJ7HYCiE4crvJ4kAg")
    bot.send_message(message.chat.id, "✅✅ He he hey! My name is Bitcoin Oracle and I'm so excited to help you and to be your favourite trending tool")
    bot.send_message(message.chat.id, "With this bot you can analyze all tweets in the last hours of Bitcoin. It enable to you make decisions that can take huge profits. If you want to be financially independently, Bitcoin Oracle is you best mate. 🚀🚀")
    audio = open('./assets/welcome.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    
    bot.send_message(message.chat.id,"Let me know, how do you want to start make money? Which coin do you want to check?")


@bot.message_handler(commands=['1h', '2h', '3h'])
def command_hour(message):
    
    hour = int(message.text.replace("h", "").replace("/", ""))

    setClient(message.chat.id,hour=hour)
    bot.send_message(message.chat.id, "Processing")
    bot.send_message(message.chat.id, "Aqui tornariem els resultats")
    
    resetClient(message.chat.id)
    bot.send_message(message.chat.id, "Which coin do you want to check next?")
    


@bot.message_handler(func=lambda message: message.text == 'Show the analysis of the last hour' and message.content_type == 'text')
def command_answer1(message):
    

    #CRIDA DE FUNCIONS NECESSARIES
    bot.send_message(message.chat.id, "Aqui mostrem estadistiques i emojis i blablabla")
    bot.send_message(message.chat.id, "So... It seems...")
    data = retrieve_tweets("bitcoin", 1, "en")

    if data['state'] == 'OK':
        # Pump
        if data['Score Average'] > 0:
            bot.send_sticker(message.chat.id, "CAADBAADcAAD6EZ5AAGO_ov4mgcnRgI")
        # Dump
        else:
            bot.send_sticker(message.chat.id, "CAADBAADbwAD6EZ5AAHJt9W7WsFcTwI")
    else:
        print('INTRODUCE AGAIN THE CRYPTOCURRENCY (EJ: Ethereum, Bitcoin, Ripple')

@bot.message_handler(func=lambda message: message.text == 'Give me the prize of Bitcoin' and message.content_type == 'text')
def command_answer2(message):
    
    #CRIDA DE FUNCIONS NECESSARIES

    bot.send_message(message.chat.id, "6000. OJU! HARDCODEJAT!")
    



@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    
    coin=message.text.lower().capitalize()
    
    if coinExist('e'):

        setClient(message.chat.id,coin=coin)


        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('/1h')
        itembtn2 = types.KeyboardButton('/2h')
        itembtn3 = types.KeyboardButton('/3h')
        markup.add(itembtn1, itembtn2, itembtn3)

        bot.send_message(message.chat.id, "How many hours?",reply_markup=markup)
   
    else:

        bot.send_sticker(message.chat.id, "CAADAQADDgADHYJ7HdRDi-MonN_9Ag")
        bot.send_message(message.chat.id, "I don't understand. What I'm gonna do?")



bot.polling()

while True: # Don't let the main Thread end.
    pass

