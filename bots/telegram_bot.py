from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "gguild" in text:
        await update.message.reply_text("Welcome to Gamers Guild DAO 🚀")

app = ApplicationBuilder().token("YOUR_TELEGRAM_TOKEN").build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()