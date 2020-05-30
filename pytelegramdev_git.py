import telebot, os

token = str(os.environ.get('BOT_TOKEN'))
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '!\n\nЯ бот, который поможет тебе в программировании своих собственных Телеграм-ботов!\n\nВот список моих команд:\n\n/json\n/info\n/posts\n\nА еще ты можешь отправить мне любой файл, чтобы получить информацию о нем!\n\nУдачной разработки!')

@bot.message_handler(commands=['json'])
def json(message):
    bot.send_message(message.chat.id, message)
# Вбъцгтфюср!
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, '👨‍💻' + message.from_user.first_name + ' ' + message.from_user.last_name + '\n' + '📢' + '@' + message.from_user.username + '\n'+ '🎟' + str(message.from_user.id) + '\n' + '💬' + str(message.chat.id)) 

@bot.message_handler(commands=['posts'])
def posts(message):
    bot.send_message(message.chat.id, 'Наш канал: @ENTER_ERROR\n1 пост: https://telegra.ph/Kurs-po-sozdaniyu-Telegram-botov-ot-John-Doe-CHast-1-05-09\n2 пост: https://telegra.ph/Kurs-po-sozdaniyu-Telegram-botov-ot-John-Doe-CHast-2-05-09\nЗ пост:https://telegra.ph/Kurs-po-sozdaniyu-Telegram-botov-ot-John-Doe-CHast-3-05-10\n4 пост: https://telegra.ph/Kurs-po-sozdaniyu-Telegram-botov-ot-John-Doe-CHast-4-05-14')

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, message.photo)

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.send_message(message.chat.id, message.sticker)

@bot.message_handler(content_types=['video'])
def video(message):
    bot.send_message(message.chat.id, message.video)

@bot.message_handler(content_types=['audio'])
def audio(message):
    bot.send_message(message.chat.id, message.audio)
# АТВЫКЫ ЭБЦБФБЧ ДЮБФБ "Ичътго ёуыю Угёет" @Mieri_1 ы вбюёйы дфбь вгыъ, вбебгбвыдо!)
@bot.message_handler(content_types=['document'])
def document(message):
    bot.send_message(message.chat.id, message.document)

bot.polling()
