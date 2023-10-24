import requests
import os
import argparse
import download_image


def get_launch_id():
    parser = argparse.ArgumentParser(
        description = 'Программа позволяет скачать картинки с запуска SpaceX по id запуска '
    )
    parser.add_argument('-id', '--launch_id', help='id запуска', default="latest")
    args = parser.parse_args()
    return args.launch_id




def fetch_spacex_last_launch(launch_id):
    api_url = "https://api.spacexdata.com/v5/launches/{}".format(launch_id)
    response = requests.get(api_url)
    response.raise_for_status()
    pictures_links = response.json()['links']['flickr']['original']
    for picture, links in enumerate(pictures_links):
        filename = os.path.basename(links)
        download_image.download_image(links, os.path.join(download_image.DIRECTORY, filename))






if __name__=='__main__':
    launch_id = get_launch_id()
    fetch_spacex_last_launch(launch_id)