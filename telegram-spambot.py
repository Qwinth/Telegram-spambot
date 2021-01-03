print('Starting spam bot')
import telebot
import random as r
import pause
user_id = 0
loop = 0
is_spamming = 0
bot = telebot.TeleBot('Bot account')
print('Spam bot started')

def spam():
    bot.send_message(user_id, r.randint(10000000, 99999999))
    pause.seconds(1)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, to start spam, enter the id of the person to whom this spam will be sent, then send the command: "/start_spam".')

@bot.message_handler(commands=['help'])
def command(message):
    bot.send_message(message.chat.id, 'To start the spam of sending the id to whom this spam will be sent, then send the command: "/start_spam". To stop spam sent command: "/stop_spam".')

@bot.message_handler(commands=['my_id'])
def command(message):
    bot.send_message(message.chat.id, 'Your telegram id: ' + str(message.from_user.id) + '.')

@bot.message_handler(commands=['bot_id'])
def command(message):
    bot.send_message(message.chat.id, 'bot ID: 1338134206.')

@bot.message_handler(commands=['target_id'])
def command(message):
    bot.send_message(message.chat.id, 'Target telegram ID: ' + str(user_id) +'.')

@bot.message_handler(commands=['reset_id'])
def command(message):
    global user_id
    user_id = 0
    bot.send_message(message.chat.id, 'Target ID reseted.')

@bot.message_handler(commands=['stop_spam'])
def command(message):
    global loop
    loop = 1

@bot.message_handler(commands=['start_spam'])
def command(message):
    global user_id
    if user_id == 0:
        bot.send_message(message.chat.id, 'Enter target ID!')
    else:
        global is_spamming
        is_spamming = is_spamming + 1
        if is_spamming == 1:
            while True:
                global loop
                if loop == 1:
                    loop = 0
                    is_spamming = 0
                    break
                else:
                    spam()
        else:
            is_spamming = 1
            bot.send_message(message.chat.id, 'The bot has already started to spam.')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if not message.text.lower() == '':
        global user_id
        user_id = message.text
        bot.send_message(message.chat.id, 'Target ID entered.')

bot.polling()
