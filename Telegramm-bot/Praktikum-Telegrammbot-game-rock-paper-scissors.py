import telebot
import random
from telebot import types

bot = telebot.TeleBot('7109167270:AAGc1yiFvdwPsiPvIYlwx9QbtxScIIWdPWo')

G = ['Камень', 'Ножницы', 'Бумага']
# переменная для подсчета очков
score = 0
score_bot = 0


@bot.message_handler(commands=['start'])
def start(m, res=False):
    global score, score_bot
    # обнуляем счет
    score = 0
    score_bot = 0
    # Добавляем кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Камень')
    button2 = types.KeyboardButton('Ножницы')
    button3 = types.KeyboardButton('Бумага')
    markup.add(button1, button2, button3)
    # обрабатываем команду старт
    bot.send_message(m.chat.id, 'Нажми кнопку и начни игру ', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    global score, score_bot
    random_object = random.choice(G)

    result = 'Ничья'

    if random_object == 'Камень' and message.text == 'Ножницы':
        result = 'Вы проиграли!'
        score_bot += 1
    elif random_object == 'Бумага' and message.text == 'Ножницы':
        result = 'Вы победили!'
        score += 1
    elif random_object == 'Ножницы' and message.text == 'Ножницы':
        result = 'Ничья!'
    elif random_object == 'Камень' and message.text == 'Бумага':
        result = 'Вы победили!'
        score += 1
    elif random_object == 'Бумага' and message.text == 'Бумага':
        result = 'Ничья!'
    elif random_object == 'Ножницы' and message.text == 'Бумага':
        result = 'Вы проиграли!'
        score_bot += 1
    elif random_object == 'Камень' and message.text == 'Камень':
        result = 'Ничья!'
    elif random_object == 'Ножницы' and message.text == 'Камень':
        result = 'Вы победили!'
        score += 1
    elif random_object == 'Бумага' and message.text == 'Камень':
        result = 'Вы проиграли!'
        score_bot += 1

    bot.send_message(message.chat.id, random_object)
    bot.reply_to(message, result + " Текущий счет: " + " вы - "+str(score)+" Бот - "+str(score_bot))


# непрерывность работы бота
bot.polling(none_stop=True, interval=0)