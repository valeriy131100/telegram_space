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


url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
filename = 'hubble.jpeg'
file_path = 'images'

download_image(url, os.path.join(file_path, filename))
