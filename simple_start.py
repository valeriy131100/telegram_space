import os
from dotenv import load_dotenv
from bot import run_bot
from fetch_nasa import fetch_nasa_epic, fetch_nasa_apods
from fetch_spacex import fetch_spacex_last_launch

if __name__ == '__main__':
    load_dotenv()

    fetch_spacex_last_launch()

    nasa_token = os.getenv('NASA_TOKEN')
    fetch_nasa_apods(nasa_token, 40)
    fetch_nasa_epic(nasa_token, 5)

    telegram_token = os.getenv('TELEGRAM_TOKEN')
    channel_name = os.getenv('TELEGRAM_CHANNEL_NAME')
    s_latency = os.getenv('TELEGRAM_POSTING_LATENCY')
    if s_latency:
        latency = int(s_latency)
    else:
        latency = 60 * 60 * 24  # сутки

    run_bot(telegram_token, latency)
