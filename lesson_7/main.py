from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Filter
import re
from lesson_7 import database as db



async def on_startup(_):
    await db.db_start()
    print("База данных загружена")




TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
        await message.answer(text='Привет я телеграмм Бот!')
        await message.delete()


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)