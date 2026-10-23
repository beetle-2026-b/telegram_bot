import re
import telebot

TOKEN = "8594308908:AAFR1aqLGGg80DxsVT69BFqz64mbcju0jrg"
bot = telebot.TeleBot(TOKEN)


def replacer(match):
    word = match.group(0)
    lower_word = word.lower()

    # Формула универсальная: "пиз" + само слово (да / дадада / нет / не) + "ня"
    result = f"пиз{lower_word}ня"

    # Сохраняем регистр автора
    if word.isupper():
        return result.upper()
    elif word[0].isupper():
        return result.capitalize()
    else:
        return result.lower()


@bot.message_handler(func=lambda message: message.text is not None)
def handle_message(message):
    text = message.text

    # Ищет отдельные слова: "да" (и "дадада..."), "нет" (и "нетнет..."), "не" (и "нене...")
    pattern = r"\b(?:(?:да)+|(?:нет)+|(?:не)+)\b"

    if re.search(pattern, text, flags=re.IGNORECASE):
        new_text = re.sub(pattern, replacer, text, flags=re.IGNORECASE)
        bot.reply_to(message, new_text)


if __name__ == "__main__":
    print("Бот успешно запущен...")
    bot.infinity_polling()
