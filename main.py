import telebot
import requests
import os

# توکن ربات رو از متغیر محیطی بخون
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# پیام خوش آمدگویی
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 به ربات تحلیلی Trade Mind خوش آمدید.\n"
        "آماده‌ایم تا به شما کمک کنیم تصمیم‌های معاملاتی دقیق‌تری بگیرید.\n"
        "📈 پرسود باشید..."
    )

# دریافت تحلیل با تایپ نام نماد
@bot.message_handler(func=lambda m: True)
def send_analysis(message):
    symbol = message.text.upper()
    bot.reply_to(message, f"🔍 تحلیل {symbol} در حال آماده‌سازی است...")
    try:
        # این قسمت فقط نمونه است (بعد میشه وصلش کرد به API واقعی)
        price = get_price(symbol)
        bot.send_message(message.chat.id, f"💰 قیمت فعلی {symbol}: {price}")
    except:
        bot.send_message(message.chat.id, "❌ نماد یافت نشد یا خطا در دریافت داده.")

# تابع نمونه برای گرفتن قیمت
def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    r = requests.get(url)
    data = r.json()
    return data['price']

# اجرای ربات
if __name__ == "__main__":
    bot.infinity_polling()
