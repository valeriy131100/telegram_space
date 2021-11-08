import requests
import os
from utils import download_image


def fetch_spacex_last_launch():
    launches_url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(launches_url)
    response.raise_for_status()
    launches = response.json()

    for launch in launches:
        images = launch['links']['flickr']['original']
        if images:
            for image_num, image_link in enumerate(images):
                image_name = f'spacex{image_num}.jpg'
                image_path = os.path.join('images', image_name)
                download_image(image_link, image_path)
            return


if __name__ == '__main__':
    fetch_spacex_last_launch()
