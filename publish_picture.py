import argparse
import os
import random
import telegram
from dotenv import load_dotenv

import download_image


def send_picture(image, chat_id,bot):

    with open(os.path.join(download_image.DIRECTORY, image), 'rb') as file:

        bot.send_document(
            chat_id=chat_id,
            document=file
        )


def select_photo(file_name):
    images = os.listdir(download_image.DIRECTORY)
    image = random.choice(images) if not file_name else file_name
    return image


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=tg_token)
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    parser = argparse.ArgumentParser(description='Программа позволяет отправить фото из папки')
    parser.add_argument(
        '-n',
        '--file_name',
        help='Имя файла ',
        default=None
    )
    args = parser.parse_args()
    image = select_photo(args.file_name)
    send_picture(image, chat_id,bot)