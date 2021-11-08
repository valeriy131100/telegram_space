import os
import random
import telegram
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=telegram_token)

    _, _, images = next(os.walk('images'))
    image_filename = random.choice(images)
    image_path = os.path.join('images', image_filename)
    with open(image_path, 'rb') as image_file:
        telegram_image = telegram.InputMediaPhoto(media=image_file)
        bot.send_media_group(chat_id='@justsomespaceposting', media=[telegram_image])
