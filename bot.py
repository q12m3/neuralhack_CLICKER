import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ["BOT_TOKEN"]
GAME_URL = "https://neuralhack.q12m3.site"
OWNER_USERNAME = "q12m3"

WELCOME_TEXT = (
    "Привет! Спасибо за регистрацию 🚀\n\n"
    "Это NEURAL HACK — демо-игра из моего портфолио.\n"
    "Если нужен такой же проект или что-то похожее — пиши мне, обсудим детали!"
)

ALREADY_WROTE_TEXT = (
    "Привет, я тебе уже написал 👆\n\n"
    "Если нужен такой же проект или что-то похожее — жми «Сообщение мне» выше и пиши, всё обсудим!"
)


def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🎮 Запуск игры", web_app=WebAppInfo(url=GAME_URL))],
            [InlineKeyboardButton("✉️ Сообщение мне", url=f"https://t.me/{OWNER_USERNAME}")],
        ]
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(WELCOME_TEXT, reply_markup=main_keyboard())


async def any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(ALREADY_WROTE_TEXT, reply_markup=main_keyboard())


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, any_message))
    app.run_polling()


if __name__ == "__main__":
    main()
