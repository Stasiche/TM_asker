import config
import telebot
import os
import markups as ms
import json

status = 0
student = {}
student_id = None

bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])
def star_bot(message):
    global student_id
    tmp_flag = False
    if os.path.exists('students.json'):
        with open('students.json', 'r') as f:
            tmp_flag = json.load(f).get(str(message.chat.id), None) is not None
            print(tmp_flag)
    if tmp_flag:
        student_id = message.chat.id
        return

    global status

    student_id = None
    status = 0
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row('Магистратура')
    markup.row('Бакалвариат')
    bot.send_message(message.chat.id, "Выбери степень", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def talk(message):
    global status, student_id
    if student_id is None:
        if status == 0:
            student['degree'] = message.text
            bot.send_message(message.chat.id, "Выбери курс", reply_markup=ms.get_study_year_markup(student['degree']))
            status = 1

        elif status == 1:
            student['year'] = message.text
            bot.send_message(message.chat.id, "Выбери программу", reply_markup=ms.get_program_markup(student['degree']))
            status = 2

        elif status == 2:
            student['programm'] = message.text
            student['group'] = '11111/2222'
            # bot.send_message(message.chat.id, "Выбери группу", reply_markup=ms.get_program_markup(student))
            status = 3
            with open('students.json', 'w') as f:
                json.dump({message.chat.id:student}, f)
            student_id = message.chat.id
            # bot.send_message(message.chat.id, ' ', reply_markup=telebot.types.ReplyKeyboardRemove())


# if os.path.exists('students.json'):
#     with open('students.json', 'w') as f:
#         cur_id = str(len(json.load(f)) + 1)
# else:
#     cur_id = '0'

bot.polling(none_stop=True)