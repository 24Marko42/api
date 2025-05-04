import requests
from api_keys import geocode_api_key


response = requests.get(f'https://geocode-maps.yandex.ru/v1/?apikey={geocode_api_key}&geocode=Москва, Красная площадь, 1&format=json')

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
# Полный адрес топонима:
toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
print(toponym_address, "имеет координаты:", toponym_coodrinates)
