from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button_1', url='https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=11')
ib2 = InlineKeyboardButton(text='Button_2', url='https://www.youtube.com/watch?v=Y4_7OLiLRBg')

ikb.add(ib1,ib2)

@dp.message_handler(commands=['старт'])
async def start_commands(message: types.Message):
        await message.answer(text='Привет я телеграмм Бот!', reply_markup=ikb)
        await message.delete()







if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)