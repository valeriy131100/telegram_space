import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

images_folder = os.getenv('IMAGES_FOLDER', default='images')
Path(images_folder).mkdir(parents=True, exist_ok=True)

telegram_token = os.getenv('TELEGRAM_TOKEN')
telegram_channel_name = os.getenv('TELEGRAM_CHANNEL_NAME')
s_latency = os.getenv('TELEGRAM_POSTING_LATENCY', default=str(60*60*24))
latency = int(s_latency)

nasa_token = os.getenv('NASA_TOKEN')
