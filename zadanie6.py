import requests
import os

folder = "maps"  # Имя папки
filename = "Astralia_map.jpg"  # Имя файла
filepath = os.path.join(folder, filename)  # Полный путь

response = None
map_request = "https://static-maps.yandex.ru/1.x/?ll=149.125531,-35.3069078&spn=35,35&l=map"
response = requests.get(map_request)


with open(filepath, "wb") as file:
    file.write(response.content)