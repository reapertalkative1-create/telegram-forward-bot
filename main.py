import os
import telebot
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot đang chạy 24/7 trên Render"

# ================== CẤU HÌNH (ĐÃ CẬP NHẬT) ==================
TOKEN = "8464538918:AAFgetkBqQNNuBzIfk07bccUIXBjhzZlAWU"
YOUR_CHAT_ID = 8240242915
GROUP_CHAT_ID = -5101863832

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_order(message):
    if message.chat.id == YOUR_CHAT_ID:
        text = message.text.lower() if message.text else ""
        if "Kho Báu" in text or "Phát Hiện" in text or "Chia Sẻ" in text:
            try:
                bot.forward_message(GROUP_CHAT_ID, YOUR_CHAT_ID, message.message_id)
                print("✅ Forward con hàng mới thành công")
            except:
                bot.send_message(GROUP_CHAT_ID, f"📦 Đơn hàng mới:\n{message.text}")

def run_flask():
    app.run(host='0.0.0.0', port=10000)

Thread(target=run_flask).start()

bot.infinity_polling()
