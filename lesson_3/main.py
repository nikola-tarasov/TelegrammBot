from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_starttup(_):
    print('Бот запущен!')

@dp.message_handler(commands=['start'])
async def send_random_letter(message: types.Message):
        await message.answer(text='<em>Привет Добро пожаловать в наш бот!!!</em>', parse_mode='HTML')
# отправляет ответ на команду


@dp.message_handler(commands=['sticker'])
async def send_stikcer(message: types.Message):
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJeHNkl-6HH1CaxN_0SR4RRRY3BfOe1wACkgEAAiteUwsoLuDk2dFm4C8E')
        await message.delete()
# отправляет стикер

@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text + "💌")

# отправляет в ответном запросе смайл

if __name__=='__main__':
    executor.start_polling(dp, on_startup=on_starttup)