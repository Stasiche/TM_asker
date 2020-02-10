import telebot
import numpy as np

def get_study_year_markup(deg):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row('1', '2')
    if deg == 'Бакалвариат':
        markup.row('3', '4')
    return markup

def get_program_markup(deg):
    master_programms = ['Газпром', 'Международная', 'Классика', 'CDIO']
    master_programms = np.array(master_programms).reshape(-1, int(len(master_programms)))

    bach_programms = ['Биология', 'Небиология', '2222', '33333', '12221231', '41414', '994394']
    bach_programms = np.array(bach_programms).reshape(-1, int(len(bach_programms)))

    markup = telebot.types.ReplyKeyboardMarkup()
    if deg == 'Бакалвариат':
        program = bach_programms
    else:
        program = master_programms

    for i in range(program.shape[1]):
        markup.row(*program[:,i])

    return markup

def get_group_markup(deg):
    master_programms = ['Газпром', 'Международная', 'Классика', 'CDIO']
    master_programms = np.array(master_programms).reshape(-1, int(len(master_programms)))

    bach_programms = ['Биология', 'Небиология', '2222', '33333', '12221231', '41414', '994394']
    bach_programms = np.array(bach_programms).reshape(-1, int(len(bach_programms)))

    markup = telebot.types.ReplyKeyboardMarkup()
    if deg == 'Бакалвариат':
        program = bach_programms
    else:
        program = master_programms

    for i in range(program.shape[1]):
        markup.row(*program[:,i])

    return markup

def get_marks_markup():
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row('1', '5')
    markup.row('2', '3', '4')
    return markup

