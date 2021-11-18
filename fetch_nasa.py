import requests
import os
from datetime import datetime
from file_workers import download_image, get_url_file_extension
from config import nasa_token, images_folder


def fetch_nasa_apods(token, count, images_folder_path):
    images_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'count': count
    }
    response = requests.get(images_url, params=params)
    response.raise_for_status()

    images = response.json()
    for image_num, image in enumerate(images):
        image_link = image['url']
        image_extension = get_url_file_extension(image_link)
        image_name = f'nasa{image_num}{image_extension}'
        image_path = os.path.join(images_folder_path, image_name)
        download_image(image_link, image_path)


def fetch_nasa_epic(token, count, images_folder_path):
    epics_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': token
    }
    response = requests.get(epics_url, params=params)
    response.raise_for_status()

    epics = response.json()[0:count]
    for epic in epics:
        image_name = f'{epic["image"]}.png'
        epic_date = datetime.fromisoformat(epic['date'])
        formatted_epic_date = epic_date.strftime('%Y/%m/%d')  # YYYY/MM/DD
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_epic_date}/png/{image_name}'
        image_path = os.path.join(images_folder_path, image_name)
        download_image(epic_image_url, image_path, http_params=params)


if __name__ == '__main__':
    fetch_nasa_apods(nasa_token, 40, images_folder)
    fetch_nasa_epic(nasa_token, 5, images_folder)
