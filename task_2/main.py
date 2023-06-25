from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMD = """
<b>/help</b> - <em>показывает список команд</em>
<b>/sticker</b> - <em>присылает стикер</em>
"""

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply(text=HELP_COMMD, parse_mode='HTML')


@dp.message_handler(commands=['sticker'])
async def send_stikcer(message: types.Message):
        await message.reply('Смотри какой котик 🩷')
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJeNVkmAyyboKqjkaw8-5fPX77M2YxeAACDQADG7f5CrkTCEn9cKCZLwQ')
# отправляет приветсыие и стикер

@dp.message_handler()
async def send_healt(message: types.Message):
    if message.text == '❤️':
        await message.answer('🖤')
# отправляет черное если красное пришло




if __name__=='__main__':
    executor.start_polling(dp)