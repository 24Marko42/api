import requests
from api_keys import geocode_api_key

cities = ["Барнаул", "Мелеуз", "Йошкар-Ола"]

for city in cities:
    response = requests.get(f"https://geocode-maps.yandex.ru/v1/?apikey={geocode_api_key}&geocode={city}&format=json")
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    name_area = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
    print(city + " : " + name_area)

