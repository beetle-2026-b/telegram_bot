import os
from threading import Thread
from flask import Flask
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask("")

@app.route("/")
def home():
    return "Бот жив и работает!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def check_blyad(message):
    text = getattr(message, "text", None) or getattr(message, "caption", None) or ""
    return "блядь" in text.lower()


@bot.message_handler(
    func=check_blyad,
    content_types=["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "animation"],
)
def handle_blyad(message):
    bot.reply_to(message, "блядь.")

if __name__ == "__main__":
    Thread(target=run_web).start()
    print("Бот успешно запущен...")
    bot.infinity_polling()
