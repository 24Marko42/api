import requests
import os
from pathlib import Path

route_points = [
    "86.086847,55.355198",  # Кемерово
    "86.162243,54.663609",  # Ленинск-Кузнецкий
    "87.136053,53.757553",  # Новокузнецк
    "87.983137,52.929298"   # Шерегеш
]

# Формируем параметры для маршрута
pl_param = "~".join(route_points)

# Параметры запроса
params = {
    "ll": "86.5,54.5",  # Центр области
    "spn": "5,5",       # Охват всей области
    "l": "map",         # Тип карты
    "size": "650,450",  # Размер изображения
    "pl": f"c:8822dd,w:5,{pl_param}"  # Линия маршрута
}

# URL и запрос
url = "https://static-maps.yandex.ru/1.x/"
response = requests.get(url, params=params)  # Передаем params здесь!

# Создаем папку
folder = Path("maps")
folder.mkdir(exist_ok=True)

# Сохраняем результат
filename = "kemerovo_map_way.png"
filepath = folder / filename

if response.status_code == 200:
    with open(filepath, "wb") as file:
        file.write(response.content)
    print(f"Карта сохранена: {filepath.resolve()}")
else:
    print(f"Ошибка {response.status_code}. URL: {response.url}")