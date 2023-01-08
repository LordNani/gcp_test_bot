import config
import telebot

bot = telebot.TeleBot(token=config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(msg):
    bot.send_message(msg.chat.id, 'Hello hello, I am bot! :)')


bot.infinity_polling()