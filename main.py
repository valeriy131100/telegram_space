import requests
import os
from pathlib import Path

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
filename = 'hubble.jpeg'
file_path = 'images'

Path(file_path).mkdir(parents=True, exist_ok=True)

response = requests.get(url)
response.raise_for_status()

with open(os.path.join(file_path, filename), 'wb') as file:
    file.write(response.content)
