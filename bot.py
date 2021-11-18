import os
import random
import time
import telegram
from dotenv import load_dotenv


def run_bot(token, post_latency):
    bot = telegram.Bot(token=telegram_token)

    while True:
        _, _, images = next(os.walk('images'))
        image_filename = random.choice(images)
        image_path = os.path.join('images', image_filename)
        with open(image_path, 'rb') as image_file:
            bot.send_photo(chat_id=channel_name, photo=image_file)

        time.sleep(latency)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    channel_name = os.getenv('TELEGRAM_CHANNEL_NAME')
    s_latency = os.getenv('TELEGRAM_POSTING_LATENCY', default=str(60*60*24))
    latency = int(s_latency)

    run_bot(telegram_token, latency)
