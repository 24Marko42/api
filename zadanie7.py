import requests
import os


# Список точек для отметок
points = [
    
    {"coords": "86.060110,55.344206", "style": "pm2rdl"},       # ЖД Вокзал (красная)
    {"coords": "86.125771,55.389487", "style": "pm2gnl"},       # Кардиодиспансер (зелёная)
    {"coords": "86.071903,55.375438", "style": "pm2orl"},       # Красная Горка (оранжевая)
    {"coords": "86.078354,55.361069", "style": "pm2bll"}        # Парк Чудес (синяя)
]

pt_params = "~".join([f"{p['coords']},{p['style']}" for p in points])


url = (
    f"https://static-maps.yandex.ru/1.x/?ll=86.0898,55.3548"
    f"&spn=0.1,0.1&l=map&size=650,450&pt={pt_params}"
)

# Создаем папку для сохранения
filename = "kemerovo_map.png"
folder = "maps"
filepath = os.path.join(folder, filename)  # Полный путь

# Отправляем запрос
response = requests.get(url)

with open(filepath, "wb") as file:
    file.write(response.content)
    print(f"Карта сохранена: {filepath}")
