import os
import re
from threading import Thread
from flask import Flask
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# --- Крошечный веб-сервер для Render и будильника ---
app = Flask("")

@app.route("/")
def home():
    return "Бот жив и работает!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# --- Логика бота ---
def replacer(match):
    word = match.group(0)
    lower_word = word.lower()
    result = f"пиз{lower_word}ня"
    if word.isupper():
        return result.upper()
    elif word[0].isupper():
        return result.capitalize()
    else:
        return result.lower()

@bot.message_handler(func=lambda message: message.text is not None)
def handle_message(message):
    text = message.text
    # да / нет — обычные отдельные слова
    # не — отдельное слово И только если после него нет пробела
    pattern = r'(?<![а-яА-ЯёЁa-zA-Z])(да|нет|не(?!\s))(?![а-яА-ЯёЁa-zA-Z])'
    if re.search(pattern, text, flags=re.IGNORECASE):
        new_text = re.sub(pattern, replacer, text, flags=re.IGNORECASE)
        bot.reply_to(message, new_text)

if __name__ == "__main__":
    # Запускаем веб-сервер в фоновом потоке
    Thread(target=run_web).start()
    print("Бот успешно запущен...")
    bot.infinity_polling()
