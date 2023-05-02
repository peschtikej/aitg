from aiogram import Bot, Dispatcher, executor, types
import os, dotenv
from ai import get_response

dotenv.load_dotenv()
bot=Bot(os.getenv('BOT'))
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! Я MegaChat, искусственный интеллект, созданный для того, чтобы помочь тебе в решении задач и достижении целей.\nВведите запрос:')

@dp.message_handler(content_types=['text'])
async def funcl(message: types.Message):
    textgpt=get_response(message.text)
    await bot.send_message(message.from_user.id, textgpt)

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)