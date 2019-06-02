import telebot
from telebot import types

TOKEN = '867716809:AAGcvZb7K4-zeOWFpNv-nh9bqo0D0TiDCew' 

bot = telebot.TeleBot(TOKEN)

def mainMarkup():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Show the analysis of the last hour')
    itembtn2 = types.KeyboardButton('Give me the prize of Bitcoin')
    markup.add(itembtn1, itembtn2)
    return markup


@bot.message_handler(commands=['start', 'help'])
def command_help(message):
        bot.send_sticker(message.chat.id, "CAADAQADAQADHYJ7HYCiE4crvJ4kAg")
        bot.send_message(message.chat.id, "✅✅ He he hey! My name is Bitcoin Oracle and I'm so excited to help you and to be your favourite trending tool")
        bot.send_message(message.chat.id, "With this bot you can analyze all tweets in the last hours of Bitcoin. It enable to you make decisions that can take huge profits. If you want to be financially independently, Bitcoin Oracle is you best mate. 🚀🚀")
        audio = open('./assets/welcome.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        

        
        bot.send_message(message.chat.id,"Let me know, how do you want to start make money? What do you want to do?",reply_markup=mainMarkup())
        
@bot.message_handler(func=lambda message: message.text == 'Show the analysis of the last hour' and message.content_type == 'text')
def command_answer1(message):
    
    #CRIDA DE FUNCIONS NECESSARIES

    bot.send_message(message.chat.id, "Aqui mostrem estadistiques i emojis i blablabla")
    bot.send_message(message.chat.id, "So... It seems")
    pump=True
    if pump:
        bot.send_sticker(message.chat.id, "CAADBAADcAAD6EZ5AAGO_ov4mgcnRgI") 
 
    else:
        bot.send_sticker(message.chat.id, "CAADBAADbwAD6EZ5AAHJt9W7WsFcTwI")

@bot.message_handler(func=lambda message: message.text == 'Give me the prize of Bitcoin' and message.content_type == 'text')
def command_answer2(message):
    
    #CRIDA DE FUNCIONS NECESSARIES

    bot.send_message(message.chat.id, "6000. OJU! HARDCODEJAT!")
    

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    bot.send_sticker(message.chat.id, "CAADAQADDgADHYJ7HdRDi-MonN_9Ag")
    bot.send_message(message.chat.id, "I don't understand. What I'm gonna do?")

bot.polling()

while True: # Don't let the main Thread end.
    pass

