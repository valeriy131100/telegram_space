import requests
import os
from pathlib import Path
from file_workers import download_image
from config import images_folder


def fetch_spacex_last_launch(images_folder_path):
    launches_url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(launches_url)
    response.raise_for_status()
    launches = response.json()

    sorted_launches = sorted(
        launches,
        key=(lambda launch: launch['date_utc'])
    )

    for launch in reversed(sorted_launches):
        images = launch['links']['flickr']['original']
        if images:
            for image_num, image_link in enumerate(images):
                image_name = f'spacex{image_num}.jpg'
                image_path = os.path.join(images_folder_path, image_name)
                download_image(image_link, image_path)
            return


if __name__ == '__main__':
    Path(images_folder).mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(images_folder)
