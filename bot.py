import telebot

BOT_TOKEN = "8448713962:AAHnMZ2trmaigVS2lbnpnBfGyHXY4WbArRY"
ADMIN_ID = "7081153845"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🌄 TOG' SHABBODASI botiga xush kelibsiz! ✅")

@bot.message_handler(commands=['menu'])
def menu(message):
    text = "🍴 Bizning menyu:\n\n"
    text += "1. Shashlik - 25000 so'm\n"
    text += "2. Lavash - 20000 so'm\n"
    text += "3. Cola - 10000 so'm\n"
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def echo(message):
    if str(message.chat.id) == ADMIN_ID:
        bot.reply_to(message, f"👑 Admin: {message.text}")
    else:
        bot.reply_to(message, f"Siz yozdingiz: {message.text}")

print("🤖 Bot ishga tushdi...")
bot.polling()
