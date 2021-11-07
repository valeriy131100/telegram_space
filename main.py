import requests
import os
from pathlib import Path


def download_image(image_url, image_path):
    response = requests.get(image_url)
    response.raise_for_status()

    image_dirname = os.path.dirname(image_path)
    Path(image_dirname).mkdir(parents=True, exist_ok=True)

    with open(image_path, 'wb') as file:
        file.write(response.content)


launches_url = 'https://api.spacexdata.com/v4/launches'
response = requests.get(launches_url)
response.raise_for_status()
launches = response.json()

images = []
for launch in launches:
    images = launch['links']['flickr']['original']
    if images:
        for image_num, image_link in enumerate(images):
            image_name = f'spacex{image_num}.jpg'
            image_path = os.path.join('images', image_name)
            download_image(image_link, image_path)
        break
