from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP = """
<b>/help</b> - <em>показывает список команд</em>
<b>/картинка</b> - <em>прислать картинку</em>
<b>/местоположение</b> - <em>местоположение</em>
"""

@dp.message_handler(commands=['help'])
async def commands_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP, parse_mode='HTML')
    await message.delete()
#отправляет сообщение в личку независимо где пользователь написал

@dp.message_handler(commands=['картинка'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://resizer.mail.ru/p/8756212a-2e3b-553f-a1cd-dc7edfb0d02d/AQAKOHoaLV1AuslOBaO8qVDvUAlkXeV9GN-atpcfFie2HG7xflNEEqw6qQEcUSrc75vE2gGp9Fw7J_Wts8J0H-c1XaY.jpg')
    await message.delete()
#отправляет картинку в чат или в личку

@dp.message_handler(commands=['местоположение'])
async def send_poin(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=65,longitude=45 )
    await message.delete()
#отправляет местоположение по заданным координатам

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)# skip_updates=True отключает обновлени если бот отключен