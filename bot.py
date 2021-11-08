import os
import telegram
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=telegram_token)
    print(bot.get_me())
