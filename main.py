import telebot
import random
import os
from bot_logic import eco
from bot_logic import ani



bot = telebot.TeleBot("#ВАШ ТОКЕН")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Пропиши /help для более подобной информации!')



@bot.message_handler(commands=['help'])
def send_helper(message):
    bot.reply_to(message, f'Я бот который для обьяснения подросткам важности экологии. У меня есть команды /start, /mem, /ecology, /animals!')



@bot.message_handler(commands=['mem'])
def send_mem(message):
    file_list = os.listdir("images")
    img_name = random.choice(file_list)
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)



@bot.message_handler(commands=['ecology'])
def send_ecer(message):
    bot.reply_to(message, eco())


@bot.message_handler(commands=['animals'])
def send_anim134(message):
    bot.reply_to(message, ani())



bot.polling()
