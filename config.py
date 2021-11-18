import os
from dotenv import load_dotenv
from file_workers import create_path_if_not_exists

load_dotenv()

images_folder = os.getenv('IMAGES_FOLDER', default='images')
create_path_if_not_exists(images_folder)

telegram_token = os.getenv('TELEGRAM_TOKEN')
telegram_channel_name = os.getenv('TELEGRAM_CHANNEL_NAME')
s_latency = os.getenv('TELEGRAM_POSTING_LATENCY', default=str(60*60*24))
latency = int(s_latency)

nasa_token = os.getenv('NASA_TOKEN')
