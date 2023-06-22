from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6181318829:AAEunNJz8JCNwOAb0UBRabRAmvkHjm74LEo"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(text=message.text) написать сообщение

@dp.message_handler()
async def echo_upper(message: types.Message):
    if message.text.count(' ')>=1:
        await message.answer(text=message.text)


if __name__:
    executor.start_polling(dp)





