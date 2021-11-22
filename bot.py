import os
import random
import time
import telegram
from config import images_folder, telegram_token, telegram_channel_name, latency


def start_images_posting(token, post_latency, channel_name, images_folder_path):
    bot = telegram.Bot(token=token)

    while True:
        _, _, images = next(os.walk(images_folder_path))
        image_filename = random.choice(images)
        image_path = os.path.join(images_folder_path, image_filename)
        with open(image_path, 'rb') as image_file:
            bot.send_photo(chat_id=channel_name, photo=image_file)

        time.sleep(post_latency)


if __name__ == '__main__':
    start_images_posting(telegram_token, latency, telegram_channel_name, images_folder)
