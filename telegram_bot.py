import telebot
bot = telebot.TeleBot("958984122:AAHZhGw_vYVuw2lkaQcYww1Ng2hJskQVkcU")
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Talk to me and see how I respond! Scrawww" + '\n' + 'If you need any help, just press /help')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Help yourself")


@bot.message_handler(regexp='lecture')
def schedule(lecture):
	bot.reply_to(lecture, 'which day?')


@bot.message_handler(regexp='Monday')
def scheduledclasses(dayofweek):
	if dayofweek == 'Monday':
		bot.reply_to(dayofweek, '0900 Brain and Behaviour')
	else:
		bot.reply_to(dayofweek, "I don't know")


bot.polling()
