import random
from telegram import Bot
import asyncio
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = 7267064983

phrases = [
    {"fr": "Bonjour, comment ça va ?", "ar": "مرحبا، كيف حالك؟", "exp": "Bonjour = مرحبا"},
    {"fr": "Je m'appelle Mustapha.", "ar": "اسمي مصطفى.", "exp": "Je m'appelle = اسمي"},
    {"fr": "J'apprends le français.", "ar": "أنا أتعلم الفرنسية.", "exp": "J'apprends = أتعلم"},
    {"fr": "Merci beaucoup.", "ar": "شكراً جزيلاً.", "exp": "Merci = شكراً"},
    {"fr": "À demain !", "ar": "إلى الغد!", "exp": "À demain = إلى الغد"},
    {"fr": "Je suis fatigué.", "ar": "أنا متعب.", "exp": "Je suis = أنا"},
    {"fr": "Où habites-tu ?", "ar": "أين تسكن؟", "exp": "Où = أين"},
    {"fr": "Je vais bien.", "ar": "أنا بخير.", "exp": "Je vais bien = أنا بخير"},
    {"fr": "Qu'est-ce que tu fais ?", "ar": "ماذا تفعل؟", "exp": "Qu'est-ce que = ماذا"},
    {"fr": "J'aime apprendre.", "ar": "أحب التعلم.", "exp": "J'aime = أحب"}
]

def get_5_phrases():
    selected = random.sample(phrases, 5)

    message = "🇫🇷 French Daily - 5 Phrases\n\n"

    for i, p in enumerate(selected, 1):
        message += f"{i}. 🇫🇷 {p['fr']}\n"
        message += f"   🇸🇦 {p['ar']}\n"
        message += f"   🧠 {p['exp']}\n\n"

    return message

async def main():
    bot = Bot(token=TOKEN)

    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text=get_5_phrases())
            print("✅ 5 phrases sent")
        except Exception as e:
            print("❌ Error:", e)

        await asyncio.sleep(86400)  # كل 24 ساعة

asyncio.run(main())
