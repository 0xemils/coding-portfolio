import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('../rain_watcher')
load_dotenv(os.path.join(project_folder, '.env'))

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")
