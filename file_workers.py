import requests
import urllib.parse
import os


def get_url_file_extension(url):
    parsed_url = urllib.parse.urlparse(url)
    path = urllib.parse.unquote(parsed_url.path)
    extension = os.path.splitext(path)[1]
    return extension


def download_image(image_url, image_path, http_params=None):
    response = requests.get(image_url, params=http_params)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)
