from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6038543951:AAHR6pT7I2UbeZhJSTi4iodCohgRBIxWF3U"
TOKEN_PAY = "401643678:TEST:937c3290-4340-4e8e-bcb5-9fcd09636ce1"


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
        await bot.send_invoice(chat_id = message.chat.id,title='Покупка товара', description='Покупка товара этого',provider_token = TOKEN_PAY, currency='rub',prices=[types.LabeledPrice(label="Подписка на 1 месяц", amount=500*100)],payload="test-invoice-payload" )

# successful payment
@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    await bot.send_message(message.chat.id, f"Платеж на сумму {message.successful_payment.total_amount} прошел успешно!!!")


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=False)# skip_updates=True отключает обновлени если бот о