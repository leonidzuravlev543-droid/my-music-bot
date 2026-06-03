from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8958477432:AAHnMQz9PFvbWwt7wDALIq0jScvam_hlZRY"  # ВСТАВЬТЕ ТОКЕН ОТ BOTFATHER

async def start(update: Update, context):
    await update.message.reply_text('🎵 Бот работает! Отправь название песни')

async def echo(update: Update, context):
    await update.message.reply_text(f'Ищу: {update.message.text}')

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Бот запущен!")
app.run_polling()
