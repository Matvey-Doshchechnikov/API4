import datetime
import argparse
import os

import requests
from dotenv import load_dotenv
import download_image


def download_epic_photos(nasa_token, count):
    params = {
        "api_key": nasa_token
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()[:count]
    for picture, pictures in enumerate(images):
        image_name = pictures['image']
        image_datetime = datetime.datetime.fromisoformat(pictures['date'])
        image_date = image_datetime.strftime("%Y/%m/%d")
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"
        filename = f'EPIC_{picture}.png'
        download_path = os.path.join(
            download_image.DIRECTORY,
            filename
        )
        download_image.download_image(image_url, download_path, nasa_token)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['TOKEN_NASA']
    parser = argparse.ArgumentParser(description='Программа скачивает фото EPIC: Earth Polychromatic Imaging Camera.')
    parser.add_argument('-c', '--count', help='количество', default=5, type=int)
    args = parser.parse_args()
    count = args.count
    download_epic_photos(nasa_token, count)