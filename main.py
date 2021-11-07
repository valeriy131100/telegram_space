import requests
import os
import urllib.parse
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path


def get_url_file_extension(url):
    parsed_url = urllib.parse.urlparse(url)
    path = urllib.parse.unquote(parsed_url.path)
    extension = os.path.splitext(path)[1]
    return extension


def download_image(image_url, image_path, http_params=None):
    response = requests.get(image_url, params=http_params)
    response.raise_for_status()

    image_dirname = os.path.dirname(image_path)
    Path(image_dirname).mkdir(parents=True, exist_ok=True)

    with open(image_path, 'wb') as file:
        file.write(response.content)


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


def fetch_nasa_apods(token, count):
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
        image_path = os.path.join('images', image_name)
        download_image(image_link, image_path)


def fetch_nasa_epic(token, count):
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
        epic_date_formatted = epic_date.strftime('%Y/%m/%d')  # YYYY/MM/DD
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{epic_date_formatted}/png/{image_name}'
        image_path = os.path.join('images', image_name)
        download_image(epic_image_url, image_path, http_params=params)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')

    fetch_nasa_epic(nasa_token, 5)


