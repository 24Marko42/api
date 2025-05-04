import requests
from api_keys import geocode_api_key

response = requests.get(f"https://geocode-maps.yandex.ru/v1/?apikey={geocode_api_key}&geocode=Москва, Петровка, 38&format=json")

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
print(postal_code)