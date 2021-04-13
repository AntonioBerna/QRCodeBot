import qrcode
import telebot
import json

class QRCodeMaker:
    def __init__(self, text):
        self.text = " ".join(text)

    def make(self):
        return qrcode.make(self.text).get_image()


db = json.load(open("db.json"))
bot = telebot.TeleBot(db["token"])
print("Bot in esecuzione.")

@bot.message_handler(commands=["start"])
def send_start(message):
    bot.send_message(message.chat.id, text="Benvenuto in @GetQRCodeBot!")

@bot.message_handler(commands=["qrcode"])
def send_qrcode(message):
    split_message = message.text.split()
    if len(split_message) >= 2:
        qr_code = QRCodeMaker(split_message[1:])
        bot.send_message(message.chat.id, text="The QRCode was created successfully!")
        bot.send_photo(message.chat.id, qr_code.make())
    else:
        bot.send_message(message.chat.id, text="Il comando è stato utilizzato in modo errato.")

@bot.message_handler(commands=["sviluppatore"])
def send_developer(message):
    qr_code = QRCodeMaker(db["link"])
    bot.send_message(message.chat.id, text="Informazioni Sviluppatore")
    bot.send_photo(message.chat.id, qr_code.make())
    bot.send_message(message.chat.id, text="Telegram: @CleverCode")

bot.polling()