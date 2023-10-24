import argparse
import os

import requests
from dotenv import load_dotenv

import download_image


def download_apod_pictures(nasa_token, count):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": count,
        "api_key": nasa_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images_response = response.json()
    for day_image, day_images in enumerate(images_response):
        if day_images['media_type'] != 'image':
            continue
        image_url = day_images["url"]
        extension = download_image.fetch_image_extension(image_url)
        filename = f'NASA_APOD_{day_image}{extension}'
        download_path = os.path.join(download_image.DIRECTORY, filename)
        download_image.download_image(image_url, download_path)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['TOKEN_NASA']
    parser = argparse.ArgumentParser(description='Программа скачивает Astronomy Picture of the Day NASA')
    parser.add_argument('-c', '--count', help='количество', default=5, type=int)
    args = parser.parse_args()
    count = args.count
    download_apod_pictures(nasa_token, count)