import os
from dotenv import load_dotenv
from bot import run_bot
from fetch_nasa import fetch_nasa_epic, fetch_nasa_apods
from fetch_spacex import fetch_spacex_last_launch
from config import images_folder, nasa_token, latency, telegram_token, telegram_channel_name

if __name__ == '__main__':
    fetch_spacex_last_launch(images_folder)

    fetch_nasa_apods(nasa_token, 40, images_folder)
    fetch_nasa_epic(nasa_token, 5, images_folder)

    run_bot(telegram_token, latency, telegram_channel_name, images_folder)
