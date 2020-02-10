import json
import telebot
import config
import markups

bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=['text'])
def talk(message):
    print(message)


with open('students.json', 'r') as f:
    for key, values in json.load(f).items():
        bot.send_message(key, 'Hi!', reply_markup=markups.get_marks_markup())

bot.polling(none_stop=True)


