from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP = """
<b>/help</b> - <em>показывает список команд</em>
<b>/картинка</b> - <em>прислать картинку</em>
<b>/местоположение</b> - <em>местоположение</em>
<b>/старт</b> - <em>Начать работу с ботом</em>
"""

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) #resize_keyboard=True делает клавиатуру компактной
button_1 = KeyboardButton('/help')
button_2 = KeyboardButton('/картинка')
button_3 = KeyboardButton("/местополежение")
kb.add(button_1).add(button_2).add(button_3)

@dp.message_handler(commands=['старт'])
async def start_commands(message: types.Message):
        await message.answer(text='Добро пожаловать в наш телеграмм Бот', reply_markup=kb)
        await message.delete()

@dp.message_handler(commands=['help'])
async def commands_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP, parse_mode='HTML')#reply_markup=ReplyKeyboardRemove удаляет полностью кнопку
    await message.delete()


@dp.message_handler(commands=['картинка'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://n1s1.elle.ru/48/7b/36/487b36300c62c5f0cb905da52aa874b4/728x486_1_30b570c2f6c0da65bb56095068e05768@940x627_0xc0a839a4_18087198581488362059.jpeg')
    await message.delete()


@dp.message_handler(commands=['местоположение'])
async def send_poin(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=65,longitude=45 )
    await message.delete()



if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)# skip_updates=True отключает обновлени если бот отключен