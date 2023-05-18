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
async def send_result(message: types.Message):
  w = Weather(message.text)
  weather_info = w.show_city_weather()
  if type(weather_info) == dict:
    if weather_info['weather'] == 'Clear':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgUAAxkBAAEJBu9kZmhNxcfbjSN8Nkki1mENxI9obwACgQoAAuG8kQQb22sPffFyFy8E')
    elif weather_info['weather'] == 'Thunderstorm':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJButkZmgjq45pI4GUMI_BDpBIIPxMSAACLAEAAqZESAs1JufkLCR1wy8E')
    elif weather_info['weather'] == 'Drizzle':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJBulkZmgMfkL7mB-ic2XAVoMrSFQa7AACJAEAAqZESAsL5_Fz7_gGkC8E')
    elif weather_info['weather'] == 'Rain':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgUAAxkBAAEJB0FkZnDQBdEBHGcKf0VTyuhyCWcTLQACnQoAAuG8kQQQ5wWwukYO6y8E')
    elif weather_info['weather'] == 'Snow':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJBu1kZmgoZHbVna34EzaYhercwXIQBwACOAEAAqZESAvMWrzVi1b-6S8E')
    elif weather_info['weather'] == 'Mist' or weather_info['weather'] == 'Haze' or weather_info['weather'] == 'Fog':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJBvNkZmi5YtkHqWFor4BKyAwP2R2C8wACaQEAAqZESAt_3dxMvA3vCS8E')
    elif weather_info['weather'] == 'Smoke' or weather_info['weather'] == 'Ash':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJBxZkZm3r-6roGoe8aB2v5a3wSlaM_gACZwEAAqZESAuW7HRI30tNZS8E')
    elif weather_info['weather'] == 'Sand' or weather_info['weather'] == 'Dust':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJBwtkZm0vmLptf5N-pYkbUUy6ijAAARsAAjYBAAKmREgLC4izjG0lEKgvBA')
    elif weather_info['weather'] == 'Squall' or weather_info['weather'] == 'Tornado':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgUAAxkBAAEJBxlkZm4BGIr4J7VaJGaFDcldMSIc6wACoAoAAuG8kQTGGaKsxrKdiS8E')
    elif weather_info['weather'] == 'Clouds':
        await bot.send_sticker(message.from_user.id, sticker='CAACAgUAAxkBAAEJBvVkZmlN-hDboU8uc5LBWiQz3f-QgwACngoAAuG8kQToqkk3_7S6eS8E')
        
    await message.reply(text = f"Город: {weather_info['name_city']}\nПогода: {weather_info['weather']}\nКраткое описание: {weather_info['wearher_description']}\nТемпература: {weather_info['temp']}C\nВлажность: {weather_info['humidity']}%\nСкорость ветра: {weather_info['wind']} м/c")
  else:
      await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJB0tkZnzXY2Jh5EglNU7cIG1qRDCLWQACJAADwZxgDEgkWrolDSiOLwQ')
      await message.reply(text=weather_info)
      
#  await message.reply(text = f"Город: {weather_info['name_city']}\nПогода: {weather_info['weather']}\nКраткое описание: {weather_info['weather_description']}\nТемпература: {weather_info['temp']}C\nВлажность: {weather_info['humidity']}%\nСкорость ветра: {weather_info['wind']} м/c")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
