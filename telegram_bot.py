import telebot
bot = telebot.TeleBot("958984122:AAHZhGw_vYVuw2lkaQcYww1Ng2hJskQVkcU")
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "I'll tell you about  your timetable!" + '\n' + 'If you need any help, just press /help')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "You can ask me what classes you have on a certain day and I'll tell you!")

#setting lessons for the various slots
#monday classes
MO1= '[1100]' +' ' + 'Industrial & Organisational Psychology (Tutorial)'
MO2= '[1400]'+' ' + 'Industrial & Organisational Psychology (Lecture)'
MO3= '[1600]' +' '+ 'Community Psychology (Lecture)'

#Tuesday classes
TU1=' '
TU2= ' '
TU3= ' '

#Wed classes
WE1='[1000]' + ' '+ 'Career and Professional Perpetration III (Tutorial)'
WE2= '[1300]' +' '+ 'Crisis Intervention (Tutorial)'
WE3= '[1600]' +' '+ 'Brain and Behaviour (Tutorial)'

#Thursday classes
TH1=' '
TH2='[1300] World Issues (Tutorial)'
TH3= ' '

#Friday classes
FR1='[0800]'+ ' '+ 'Crisis Intervention (Lecture)'
FR2='[1000]'+' '+ 'Community Psychology (Tutorial)'
FR3=' '

all_lectures= [MO2, MO3, FR1]
for lecture in all_lectures:
	print(lecture)

@bot.message_handler(regexp= 'Mon')
def scheduledclasses(dayofweek):
	bot.reply_to(dayofweek, 'You have the following lessons:' + '\n'+ MO1 + '\n' + MO2+ '\n ' + MO3)

@bot.message_handler(regexp= 'Tues')
def scheduledclasses(dayofweek):
	bot.reply_to(dayofweek, 'You have the following lessons:'+ '\n'+ TU1+ '\n' + TU2+ '\n'+ TU3)

@bot.message_handler(regexp= 'Wed')
def scheduledclasses(dayofweek):
	bot.reply_to(dayofweek, 'You have the following lessons:'+ '\n'+ WE1+ '\n' + WE2+ '\n'+ WE3)

@bot.message_handler(regexp= 'Thurs')
def scheduledclasses(dayofweek):
	bot.reply_to(dayofweek, 'You have the following lessons:'+ '\n'+ TH1+ '\n' + TH2+ '\n'+ TH3)

@bot.message_handler(regexp= 'Fri')
def scheduledclasses(dayofweek):
	bot.reply_to(dayofweek, 'You have the following lessons:'+ '\n'+ FR1+ '\n' + FR2+ '\n'+ FR3)

@bot.message_handler(regexp= 'Lecture')
def lecture (whenislecture):
	bot.reply_to(whenislecture, lecture)




bot.polling()
