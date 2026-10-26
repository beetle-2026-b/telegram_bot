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

TARGET_USERNAME = "kokokoch_bot"

@bot.message_handler(
    func=lambda message: message.from_user is not None and (message.from_user.username or "").lower() == TARGET_USERNAME,
    content_types=["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact", "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo", "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message", "poll", "dice", "game", "poll_answer", "animation"],
)
def handle_target(message):
    bot.reply_to(message, "блядь.")

if __name__ == "__main__":
    Thread(target=run_web).start()
    print("Бот успешно запущен...")
    bot.infinity_polling()
