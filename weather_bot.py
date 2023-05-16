from aiogram import Bot, Dispatcher, executor, types
import logging
import config
from weather import Weather

API_TOKEN = config.TOKEN
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer(text="Привет!\nЯ расскажу тебе о погоде!\nПросто введи название города.")

@dp.message_handler()
async def start_message(message: types.Message):
  w = Weather(message.text)
  await message.reply(text = w.show_city_weather())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
