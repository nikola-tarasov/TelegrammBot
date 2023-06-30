from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup, KeyboardButton


TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/vote')

kb.add(b1,b2)

@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
        await message.answer(text='Привет я телеграмм Бот!', reply_markup=kb)
        await message.delete()

@dp.message_handler(commands=['vote'])
async def start_commands(message: types.Message):

    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='❤️',callback_data='Like')
    id2 = InlineKeyboardButton(text='👎', callback_data='Dislike')
    ikb.add(ib1,id2)

    await bot.send_photo(chat_id=message.from_user.id,
                               photo='https://static-cse.canva.com/blob/847132/paulskorupskas7KLaxLbSXAunsplash2.jpg',
                               caption='Нравиться фото?',
                               reply_markup=ikb)

@dp.callback_query_handler()
async def vote_call_back(callback: types.CallbackQuery):
    if callback.data =='Like':
        await callback.answer(text='Ты лайкнул')
    await callback.answer('Ты дизлайкнул')



if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)