import telebot
import Constant as Const

from telebot import types #Connecting Necessary Python libraries...

bot = telebot.TeleBot(Const.API_KEY) #Connecting Telegram Bot API...

#Command start Response
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('stickers/hi.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard configurations:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Анализ MEI 📒") #Analyzing Movement Efficiency Indicator (MEI) based on special Formulas
    item2 = types.KeyboardButton("Сервисы Такси 🚕") #Rating top #3 the best Taxi services in Kazakhstan based on website/API
    item3 = types.KeyboardButton("Оценка Такси 🚖") #Evaluate Taxi Services in your point of view based on Online Surveys System

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name} {0.last_name}👋\n\n🔹 Меня зовут - {1.first_name}, я помогу вам оценить эффективность ваших расходов на транспорт - <u>MEI</u>!\n🔹 Для начало работы, пожалуйста, выберите услугу!\n\n<b>❗ MEI - Movement Efficiency Indicator ❗</b>".format(message.from_user, bot.get_me()), reply_markup=markup, parse_mode='html')

#Command help Response
@bot.message_handler(commands=['help'])
def welcome(message):
    sti = open('stickers/possible.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, f"♦️ Контактные данные для связи с моим создателем: \n♣️ <b>Email:</b> supwithproject@gmail.com \n♥️ <b>Telegram:</b> @grembim \n♠️ <b>Instagram:</b> @grembim \n<b>🃏 Author:</b> Zhalgasbayev Arman (Developer)", parse_mode='html')

#Main text messages Responses
@bot.message_handler(content_types=['text'])
def func(message):
    if message.chat.type == 'private':
        if message.text == 'Анализ MEI 📒':
            bot.send_message(message.chat.id, f"1️⃣ Сколько раз в день вы пользуетесь услугами такси в будние дни?\n\n❕ <i>Пожалуйста, напишите КОЛИЧЕСТВО</i> ❕", parse_mode='html')
            bot.register_next_step_handler(message, get_taxi_work_day)
            #This command for registring the next step(question) for starting question || linked questions to get analytical data!
        elif message.text == 'Сервисы Такси 🚕':
            bot.send_message(message.chat.id, f"🚕 <b>Сравниваем сервисы такси: Yandex Go, Uber, inDriver или DiDi?</b> \n🔹 Рассказываем, какое такси дешевле, быстрее и удобнее.\n\n<b>Автор:</b> Камила Куркумбаева\n<b>Дата:</b> 2021 Июля, 29\n<b>Время Прочитания:</b> 11 минут\n\n🔗 <a href='https://the-steppe.com/gorod/sravnivaem-servisy-taksi-yandex-go-uber-indriver-ili-didi'>Steppe - прогрессивный сайт о жизни, работе и увлечениях.</a>", parse_mode='html')
            #Simple post like in telegram popular channels!
        elif message.text == 'Оценка Такси 🚖':
            sti = open('stickers/believe.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, f"🔗 <a href='https://docs.google.com/forms/d/e/1FAIpQLSd_122FzHVD6IttNvORHyEQAHB8xl52ybGtolkN_viQAzt51A/viewform?usp=sf_link'>Skadi - Оценка Taxi 🚖</a>", parse_mode='html')
            #Survey for our Taxi services based on Google Forms!
        else:
            #Default response to 
            sti = open('stickers/miss.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Прошу прощения, к сожалению я не могу понять вас!')
#Getting data for analytics using sequence of linked questions!
def get_taxi_work_day(message):
    if message.text.isdigit(): #Checker for digits in message, cuz it causes a bug if it is not clear number!
        global tax1
        tax1 = int(message.text)
        bot.send_message(message.chat.id, f"2️⃣ Сколько раз в день вы пользуетесь услугами такси в выходные дни?\n\n❕ <i>Пожалуйста, напишите КОЛИЧЕСТВО</i> ❕", parse_mode='html')
        bot.register_next_step_handler(message, get_taxi_week_day)
    else:
        sti = open('stickers/panic.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, '❗ Пожалуйста, просим вам вводить значения только в ЦИФРАХ, БЕЗ ПРОБЛЕЛОВ, ИНЫХ ЦИФР И БУКВ ❗\n\n❕ Прошу начать сначала через меню-панель ❕')

def get_taxi_week_day(message):
    if message.text.isdigit():
        global tax2
        tax2 = int(message.text)
        bot.send_message(message.chat.id, f"3️⃣ Какова средняя стоимость услуг такси, которыми вы пользуетесь?\n\n❕ <i>Пожалуйста, напишите значение в ТЕНГЕ</i> ❕", parse_mode='html')
        bot.register_next_step_handler(message, get_taxi_price)
    else:
        sti = open('stickers/panic.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, '❗ Пожалуйста, просим вам вводить значения только в ЦИФРАХ, БЕЗ ПРОБЛЕЛОВ, ИНЫХ ЦИФР И БУКВ ❗\n\n❕ Прошу начать сначала через меню-панель ❕')

def get_taxi_price(message):
    if message.text.isdigit():
        global taxiprice
        taxiprice = int(message.text)
        bot.send_message(message.chat.id, f"4️⃣ Сколько времени в среднем уходит на одну поездку в такси, учитывая время ожидания?\n\n❕ <i>Пожалуйста, напишите значение в МИНУТАХ</i> ❕", parse_mode='html')
        bot.register_next_step_handler(message, get_taxi_time)
    else:
        sti = open('stickers/panic.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, '❗ Пожалуйста, просим вам вводить значения только в ЦИФРАХ, БЕЗ ПРОБЛЕЛОВ, ИНЫХ ЦИФР И БУКВ ❗\n\n❕ Прошу начать сначала через меню-панель ❕')

def get_taxi_time(message):
    if message.text.isdigit():
        global taxitime
        taxitime = int(message.text)
        bot.send_message(message.chat.id, f"5️⃣ Сколько времени в среднем занимает одна поездка на общественном транспорте, учитывая время ожидания?\n\n❕ <i>Пожалуйста, напишите значение в МИНУТАХ</i> ❕", parse_mode='html')
        bot.register_next_step_handler(message, get_bus_time)
    else:
        sti = open('stickers/panic.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, '❗ Пожалуйста, просим вам вводить значения только в ЦИФРАХ, БЕЗ ПРОБЛЕЛОВ, ИНЫХ ЦИФР И БУКВ ❗\n\n❕ Прошу начать сначала через меню-панель ❕')

def get_bus_time(message):
    if message.text.isdigit():
        global bustime
        bustime = int(message.text)
        bot.send_message(message.chat.id, f"6️⃣ Сколько стоит билет на одну поездку на общественном транспорте в вашем городе?\n\n❕ <i>Пожалуйста, напишите значение в ТЕНГЕ</i> ❕", parse_mode='html')
        bot.register_next_step_handler(message, get_bus_price)
    else:
        sti = open('stickers/panic.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, '❗ Пожалуйста, просим вам вводить значения только в ЦИФРАХ, БЕЗ ПРОБЛЕЛОВ, ИНЫХ ЦИФР И БУКВ ❗\n\n❕ Прошу начать сначала через меню-панель ❕')

def get_bus_price(message):
    if message.text.isdigit():
        global busprice
        busprice = int(message.text)
        bot.send_message(message.chat.id, f"7️⃣ Сколько в среднем вы зарабатываете в месяц?\n\n❕ <i>Пожалуйста, напишите значение в ТЕНГЕ</i> ❕", parse_mode='html')
        bot.register_next_step_handler(message, get_salary)
    else:
        sti = open('stickers/panic.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, '❗ Пожалуйста, просим вам вводить значения только в ЦИФРАХ, БЕЗ ПРОБЛЕЛОВ, ИНЫХ ЦИФР И БУКВ ❗\n\n❕ Прошу начать сначала через меню-панель ❕')

def get_salary(message):
#Here we have not checker for digit type, cuz it is utf-8 errors in final result :(
    global salary
    salary = int(message.text)
    
#Cool sticker send:D
    sti = open('stickers/cool.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

#Inline keyboard
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Еще интересных фактов 💁‍♂️", callback_data='facts')
    item2 = types.InlineKeyboardButton("Мне нравится Skadi 🤖", callback_data='review')
    markup.add(item1, item2)
    global taxisum, ecotime
    taxisum = (tax1*5+tax2*2)*taxiprice*4
    taxipart = round((taxisum/salary)*100)
    econom = taxisum-(tax1*30+tax2*12)*busprice
    ecotime = (tax1*30+tax2*12)*bustime-(tax1*5+tax2*2)*taxitime*4
    bot.send_message(message.chat.id, f"Уважаемый(ая), {message.from_user.first_name} {message.from_user.last_name}! \n📊 Я успешно проанализировала ваши данные и оценила показатели MEI для вас. \n<b>🔹 По общей статистике в МЕСЯЦ:</b> \nВы в среднем тратите <b>{taxisum} Тенге(KZT)</b> на такси. \n🔹 Ваши средние расходы на такси составляют <b>{taxipart}%</b> от вашего среднего ежемесячного заработка. \n🔹 В целом, при использовании общественного транспорта вы бы смогли сэкономить в месяц <b>{econom} Тенге</b>, но при этом вы теряете собственное время, качество и комфорт обслуживания. \n🔹 Важно учитывать, что за один месяц используя такси вы экономите целых <b>{ecotime} минут</b> своего времени! \n\nПодводя к итогу, учитывая ваши данные и ваш ежемесячный капитал, мы рекомендуем вам пользоваться услугами такси!".format(message.from_user, bot.get_me()), reply_markup=markup, parse_mode='html')

#Inline Keys Trigger
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'facts':
                sti = open('stickers/hard.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                taxinum = (tax1*5+tax2*2)*48
                bot.send_message(call.message.chat.id, f"<b>🔹 По общей статистике в Год:</b> \nВы в среднем тратите <b>{taxisum*12} Тенге(KZT)</b> на такси. \n🔹 В среднем за год, используя такси вы экономите <b>{ecotime*12} минут</b> своего времени!\n🔹 В целом, вы совершаете заказ такси около <b>{taxinum}</b> раз!", parse_mode='html')
            elif call.data == 'review':
                sti = open('stickers/swish.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, "🔹 Вы мне тоже нравитесь 🤗 \n\n🔹 Благодарю вас за оценку 😇")

    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)