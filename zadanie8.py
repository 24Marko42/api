import requests
import os


route_points = [
    "86.086847,55.355198",  # Кемерово
    "86.162243,54.663609",  # Ленинск-Кузнецкий
    "87.136053,53.757553",  # Новокузнецк
    "87.983137,52.929298"   # Шерегеш
]

# Формируем параметры для маршрута (ломаная линия)
pl_param = ",".join(route_points)  # Соединяем точки маршрута

# Параметры запроса
params = {
    "ll": "86.086848,55.355200",
    "spn": "5,5",
    "l": "map",
    # Параметры линии:  толщина 5px
    "pl": f"w:5,{pl_param}"
}

# URL API Яндекс.Карт
url = "https://static-maps.yandex.ru/1.x/"

# Отправляем запрос
response = requests.get(url, params=params)

# Сохраняем результат
filename = "kemerovo_map_way.png"
folder = "maps"
filepath = os.path.join(folder, filename)  # Полный путь


with open(filepath, "wb") as file:
    file.write(response.content)
    print(f"Карта сохранена: {filepath}")
