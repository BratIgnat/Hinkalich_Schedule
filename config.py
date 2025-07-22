import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем значения переменных
BOT_TOKEN = os.getenv("BOT_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Проверка на наличие всех необходимых переменных
if not BOT_TOKEN or not SUPABASE_URL or not SUPABASE_KEY:
    raise EnvironmentError("Одна или несколько переменных окружения не заданы")
