import os
from dotenv import load_dotenv
from bot import run_bot
from fetch_nasa import fetch_nasa_epic, fetch_nasa_apods
from fetch_spacex import fetch_spacex_last_launch

if __name__ == '__main__':
    load_dotenv()
    images_folder = os.getenv('IMAGES_FOLDER', 'images')

    fetch_spacex_last_launch(images_folder)

    nasa_token = os.getenv('NASA_TOKEN')
    fetch_nasa_apods(nasa_token, 40, images_folder)
    fetch_nasa_epic(nasa_token, 5, images_folder)

    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_channel_name = os.getenv('TELEGRAM_CHANNEL_NAME')
    s_latency = os.getenv('TELEGRAM_POSTING_LATENCY', default=str(60*60*24))
    latency = int(s_latency)

    run_bot(telegram_token, latency, telegram_channel_name, images_folder)
