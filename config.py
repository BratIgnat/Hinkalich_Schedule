import os

BOT_TOKEN = os.getenv("7735459605:AAFUBeYIL7diOTEkZqCdz2xC06QkCOPNlv0")
SUPABASE_URL = os.getenv("https://fiuebssdgqiqxmnrlgej.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZpdWVic3NkZ3FpcXhtbnJsZ2VqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwMTYzMTksImV4cCI6MjA2ODU5MjMxOX0.KbgUrxvepoH76dIpiAVs6-QQcvxHcb6RkU3ifP5IaBQ")

if not all([BOT_TOKEN, SUPABASE_URL, SUPABASE_KEY]):
    raise EnvironmentError("Одна или несколько переменных окружения не заданы")
