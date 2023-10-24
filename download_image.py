import os
import requests
from urllib.parse import urlsplit

DIRECTORY = "images"


def fetch_image_extension(image_url):
    image_path = urlsplit(image_url).path
    extension = os.path.splitext(image_path)[1]
    return extension


def download_image(image_url, download_path, api_token: str) -> None:
    params = {
        "api_key": api_token,
    }
    response = requests.get(image_url, params)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)