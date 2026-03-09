import logging
from aiogram import Bot, Dispatcher, executor, types

# BotFather'dan olgan tokenni ' ' belgilari orasiga qo'ying
API_TOKEN = 'TOKENINGIZNI_SHU_YERGA_YOZING'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Tanishuv botiga xush kelibsiz. \nTez orada anketalarni to'ldirishni boshlaymiz! 😊")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
