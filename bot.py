import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from supabase import insert_user

# Загрузка .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise EnvironmentError("BOT_TOKEN не задан в .env")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Хэндлер команды /start
@dp.message(CommandStart())
async def handle_start(message: Message):
    await insert_user(
        user_id=message.from_user.id,
        name=message.from_user.full_name,
        role="ОФИЦИАНТ"  # Или можно добавить выбор позже
    )
    await message.answer("Привет! Я бот для управления расписанием.")

# Запуск
if __name__ == "__main__":
    print("Bot is starting...")
    dp.run_polling(bot)
