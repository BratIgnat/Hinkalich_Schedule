from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import logging
import os

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    await message.answer("Привет! Я бот для управления расписанием.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
