from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

import string
import random





@dp.message_handler(commands=['descriptions'])
async def send_random_letter(message: types.Message):
        await message.answer(text='Данный бот умеет отправлять рандомные симфолы латинского алфавита!')
# отправляет ответ на команду

@dp.message_handler()
async def send_Yes_or_No(message: types.Message):
        if '0' in message.text:
            return await message.reply(text='YES')
        await message.reply(text='NO')
# выводит да если 0


@dp.message_handler()
async def send_random_letter(message: types.Message):
         await message.reply(random.choice(string.ascii_letters))
# выводит рандомный символ из библиотеки стринг алфавит



if __name__=='__main__':
    executor.start_polling(dp)

