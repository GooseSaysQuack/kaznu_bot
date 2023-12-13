import telebot
from telebot import types

TOKEN = "6764304752:AAFkhdsUkInJ8tmgNqNTqisiaLc60r3x7p4"
bot = telebot.TeleBot(TOKEN)

welcome_text = '''Здравствуйте!\nВас приветствует бот, который ответит на ваши вопросы.'''


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет" or message.text.lower() == "start" or message.text.lower() == "/start":
        bot.send_message(message.chat.id, text=welcome_text, reply_markup=welcome_msg_markup)
    else:
        bot.send_message(message.chat.id, "Я Вас не понимаю, напишите «привет» ")


welcome_msg_markup = types.InlineKeyboardMarkup(row_width=1)  # кнопки под welcome_text
btn_1 = types.InlineKeyboardButton(text="Факультеты и специальности", url="https://kyrgyzstan.kaznu.kz/ru/faculties")
btn_2 = types.InlineKeyboardButton(text="Процесс поступления", callback_data="1")
btn_3 = types.InlineKeyboardButton(text="Сроки и дедлайны", callback_data="2")
btn_4 = types.InlineKeyboardButton(text="Стоимость обучения",
                                   url="https://docs.google.com/spreadsheets/d/113pM6Ryc44E"
                                       "-xzAhwTNzsokg0rGpskgivyE6yeygz30/edit?usp=sharing ("
                                       "https://docs.google.com/spreadsheets/d/113pM6Ryc44E"
                                       "-xzAhwTNzsokg0rGpskgivyE6yeygz30/edit?usp=sharing%20%5Ch)")
btn_5 = types.InlineKeyboardButton(text="Жизнь в кампусе", callback_data="3")
btn_6 = types.InlineKeyboardButton(text="Языковой вопрос", callback_data="4")
btn_7 = types.InlineKeyboardButton(text="Мероприятия в КазНУ", callback_data="5")
btn_8 = types.InlineKeyboardButton(text="Связь с университетом", callback_data="6")
btn_9 = types.InlineKeyboardButton(text="Адрес", callback_data="7")
welcome_msg_markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9)

menu_markup = InlineKeyboardMarkup = types.InlineKeyboardMarkup(row_width=1)  # кнопка возврата в меню
menu_btn = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="menu")
menu_markup.add(menu_btn)

process_markup = types.InlineKeyboardMarkup(row_width=1)  # кнопки для процесса поступления
pr_btn_1 = types.InlineKeyboardButton(text="Как поступить?", callback_data="pr_1")
pr_btn_2 = types.InlineKeyboardButton(text="Необходимые документы", callback_data="pr_2")
pr_menu_btn = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="pr_menu")
process_markup.add(pr_btn_1, pr_btn_2, pr_menu_btn)

kampus_markup = types.InlineKeyboardMarkup(row_width=1)  # кнопки для жизни в кампусе
kamp_btn_1 = types.InlineKeyboardButton(text="Есть ли студенческие общежития?", callback_data="kamp_1")
kamp_btn_2 = types.InlineKeyboardButton(text="Какие дополнительные возможности?", callback_data="kamp_2")
kamp_menu_btn = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="kamp_menu")
kampus_markup.add(kamp_btn_1, kamp_btn_2, kamp_menu_btn)

lang_markup = types.InlineKeyboardMarkup(row_width=1)  # кнопки для языкового вопроса
lang_btn_1 = types.InlineKeyboardButton(text="На каких языках проводится обучение?", callback_data="lang_1")
lang_btn_2 = types.InlineKeyboardButton(text="Существуют ли дополнительные языковые курсы?", callback_data="lang_2")
lang_menu_btn = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="lang_menu")
lang_markup.add(lang_btn_1, lang_btn_2, lang_menu_btn)

event_markup = types.InlineKeyboardMarkup(row_width=1)  # кнопки для мероприятий
ev_btn_1 = types.InlineKeyboardButton(text="Мероприятия", callback_data="event_1")
ev_btn_2 = types.InlineKeyboardButton(text="Клубы", callback_data="event_2")
ev_menu_btn = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="event_menu")
event_markup.add(ev_btn_1, ev_btn_2, ev_menu_btn)


# ОБРАБОТЧИК ВСЕЙ CALLBACK DATA
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Для welcome
    if call.data == "1":
        bot.send_message(call.message.chat.id, "Что Вы хотите узнать?", reply_markup=process_markup)
    elif call.data == "2":
        bot.send_message(call.message.chat.id, "Зимний прием 15.10.23 - 10.01.24 / Летний прием 01.06.24 - 20.08.24",
                         reply_markup=menu_markup)
    elif call.data == "3":
        bot.send_message(call.message.chat.id, "Что Вы хотите узнать?", reply_markup=kampus_markup)
    elif call.data == "4":
        bot.send_message(call.message.chat.id, "Что Вы хотите узнать?", reply_markup=lang_markup)
    elif call.data == "5":
        bot.send_message(call.message.chat.id, "Что Вы хотите узнать?", reply_markup=event_markup)
    elif call.data == "6":
        bot.send_message(call.message.chat.id,"+996 707 496 087\n+996 507 708 898\n0312 39 40 "
                                              "52\nalfarabi.kg@kaznu.edu.kz", reply_markup=menu_markup)
    elif call.data == "7":
        bot.send_message(call.message.chat.id, "г. Бишкек, улица Турусбекова, 109/2", reply_markup=menu_markup)
    # Для process
    elif call.data == "pr_1":
        bot.send_message(call.message.chat.id, "● Собрать необходимые документы\n● Подать документы\n● Пройти "
                                               "собеседование\n● Подписать договор\n● Оплатить контракт",
                         reply_markup=menu_markup)
    elif call.data == "pr_2":
        bot.send_message(call.message.chat.id, "● Копия паспорта заверенная нотариусом-1 шт.\n● Аттестат/диплом "
                                               "заверенный нотариусом-1 шт.\n● Мед. справка 086У\n● Фото 3х4 - 4 шт ("
                                               "на белом фоне)\n● Папка (скоросшиватель) - 1 шт.",
                         reply_markup=menu_markup)
    # Для kampus
    elif call.data == "kamp_1":
        bot.send_message(call.message.chat.id, "К сожаления, университет не предоставляет общежитие.",
                         reply_markup=menu_markup)
    elif call.data == "kamp_2":
        bot.send_message(call.message.chat.id, "Университет может порекомендовать хостелы, где студенты КазНУ получат "
                                               "скидки на проживание.",
                         reply_markup=menu_markup)
    # Для lang
    elif call.data == "lang_1":
        bot.send_message(call.message.chat.id, "На русском и английском языках.", reply_markup=menu_markup)
    elif call.data == "lang_2":
        bot.send_message(call.message.chat.id, "На базе филиала есть курсы английского и русского языков.", reply_markup=menu_markup)
    # Для event
    elif call.data == "event_1":
        bot.send_message(call.message.chat.id, "На регулярной основе администрация и студенты КазНУ проводят "
                                               "различные мероприятия.", reply_markup=menu_markup)
    elif call.data == "event_2":
        bot.send_message(call.message.chat.id, "● Литературный клуб\n● Музыкальный клуб\n● Танцевальный клуб\n● "
                                               "Искусство и ремесла\n● Фотографический клуб\n● "
                                               "Научно-исследовательский клуб\n● Театральный кружок\n● Спортивные "
                                               "клубы\n● Дебатный клуб\n● Экологический клуб\n● IT-клуб\n● Языковой "
                                               "клуб\n● Благотворительный клуб\n● Кино и видео клуб",
                         reply_markup=menu_markup)
    # Для всех menu
    elif call.data == "menu":
        bot.send_message(call.message.chat.id, "Здравствуйте!\nВас приветствует бот, который ответит на ваши вопросы.",
                         reply_markup=welcome_msg_markup)
    elif call.data == "pr_menu":
        bot.send_message(call.message.chat.id, "Здравствуйте!\nВас приветствует бот, который ответит на ваши вопросы.",
                         reply_markup=welcome_msg_markup)
    elif call.data == "kamp_menu":
        bot.send_message(call.message.chat.id, "Здравствуйте!\nВас приветствует бот, который ответит на ваши вопросы.",
                         reply_markup=welcome_msg_markup)
    elif call.data == "lang_menu":
        bot.send_message(call.message.chat.id, "Здравствуйте!\nВас приветствует бот, который ответит на ваши вопросы.",
                         reply_markup=welcome_msg_markup)
    elif call.data == "event_menu":
        bot.send_message(call.message.chat.id, "Здравствуйте!\nВас приветствует бот, который ответит на ваши вопросы.",
                         reply_markup=welcome_msg_markup)


bot.polling()