import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6205028735:AAG96yO2oGwm7vr3pwoxfFkpdswrQG3y_M4"
MSG = 'Ты готов?'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_hedler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')


    await message.reply(f'Привет, {user_full_name}')

    for i in range(10):
        time.sleep(2)

        await bot.send_message(user_id, MSG)


if __name__ == "__main__":
    executor.start_polling(dp)