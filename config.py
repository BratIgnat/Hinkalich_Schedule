from dotenv import load_dotenv
load_dotenv()  # это загрузит .env в переменные окружения

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not all([BOT_TOKEN, SUPABASE_URL, SUPABASE_KEY]):
    raise EnvironmentError("Одна или несколько переменных окружения не заданы")
