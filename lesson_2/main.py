from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

HELP_COMMAND ='''
/help - список комманд
/start - начать работу с ботом'''


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_commands(message: types.Message):
        await message.reply(text=HELP_COMMAND)
        await message.delete()

@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
        await message.answer(text='Добро пожаловать в наш телеграмм Бот')
        await message.delete()



if __name__:
    executor.start_polling(dp)