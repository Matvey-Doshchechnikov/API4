import argparse
import os
import random
from time import sleep

import telegram
from dotenv import load_dotenv

from download_image import DIRECTORY
from publish_picture import send_picture


def get_delay():
    parser = argparse.ArgumentParser(
        description='Отправка с задержкой'
    )
    parser.add_argument(
        '-t',
        '--wait_time',
        help='время задержки',
        type=int,
        default = 5
    )
    args = parser.parse_args()
    return args.wait_time


def send_photos(wait_time, chat_id,bot):
    images = os.listdir(DIRECTORY)
    while True:
        try:
            for image in images:
                send_picture(image, chat_id,bot)
                sleep(wait_time)
            random.shuffle(images)
        except telegram.error.NetworkError:
            sleep(5)


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=tg_token)
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    wait_time = get_delay()
    send_photos(wait_time, chat_id,bot)