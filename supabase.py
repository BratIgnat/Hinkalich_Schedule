import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise EnvironmentError("SUPABASE_URL или SUPABASE_KEY не заданы")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

async def insert_user(user_id: int, name: str, role: str = "ОФИЦИАНТ"):
    data = {
        "telegram_id": str(user_id),
        "name": name,
        "role": role
    }
    try:
        response = supabase.table("users").insert(data).execute()
        return response
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")
        return None
