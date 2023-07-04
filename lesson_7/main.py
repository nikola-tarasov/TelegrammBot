from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton

from lesson_7 import database as db



async def on_startup(_):
    await db.db_start()
    print("База данных загружена")




TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Каталог')
b2 = KeyboardButton(text='Корзина')
b3 = KeyboardButton(text='прочее')
kb.add(b1).add(b2).add(b3)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Кроссовки', url='https://mail.ru/')
ib2 = InlineKeyboardButton(text='Футболка', callback_data='t-shirts')
ikb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
        await message.answer(text='Бот!',reply_markup=kb)
        await message.delete()


@dp.message_handler(text = 'Каталог')
async def katalog_cmd(message: types.Message):
     await message.answer(text='Товаров нет',
                   reply_markup=ikb)

@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 't-shirts':
        await bot.send_message(chat_id = callback_query.from_user.id,text='Вы выбрали 0')
    else:
        await message.reaply('Error')



if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)