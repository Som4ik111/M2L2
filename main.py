import telebot
import random
import os



bot = telebot.TeleBot("7808813003:AAHwxaDYLW4NFEwu9tMo3o5TG8mgplO6gOY")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! У меня есть команды /start, /mem, /ecology, /animals')



@bot.message_handler(commands=['mem'])
def send_mem(message):
    file_list = os.listdir("images")
    img_name = random.choice(file_list)
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)



@bot.message_handler(commands=['ecology'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, Дорогой друг, ты знаешь какого важность экологии в нашей жизни? А что будет если ближайшие лет 100 люди продолжат выбрасывать пластиковые бутылки в окружающую среюу?: •  Загрязнение океанов: Пластиковые бутылки попадают в реки, а затем в океаны, где они разлагаются на микропластик. Этот микропластик загрязняет воду, оседает на дне, попадает в пищевую цепь и отравляет морских обитателей.•  Загрязнение почвы: На суше пластиковые бутылки загрязняют почву, препятствуя росту растений, нарушая водный баланс и выделяя токсичные вещества при разложении.•  Визуальное загрязнение: Пластиковые отходы портят пейзажи, снижая эстетическую ценность природы.')



@bot.message_handler(commands=['animals'])
def send_welcome(message):
    bot.reply_to(message, f'А ты знаешь, что нужно делать с животными пострадавшими от плохих условий окружающей среды созданых человеком? 1. Немедленно отвози их к ветеренару. 2. По желанию можешь забрать животное себе :), конечно если ты этого хочешь!!!')



bot.polling()