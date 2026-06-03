from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# ВСТАВЬТЕ ВАШ РЕАЛЬНЫЙ ТОКЕН СЮДА:
TOKEN = "8958477432:AAHnMQz9PFvbWwt7wDALIq0jScvam_hlZRY"

async def start(update: Update, context):
    await update.message.reply_text('🎵 Бот работает! Отправь любое сообщение.')

async def echo(update: Update, context):
    await update.message.reply_text(f'Вы написали: {update.message.text}')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Бот успешно запущен и работает!")
    app.run_polling()

if __name__ == "__main__":
    main()
