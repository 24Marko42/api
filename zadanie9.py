import requests
from api_keys import geocode_api_key

def get_coordinates(city):
    response = requests.get(f'https://geocode-maps.yandex.ru/v1/?apikey={geocode_api_key}&geocode={city}]&format=json')
    data = response.json()
    pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    return float(pos.split()[1])  # Широта


def main():
    cities = input("Введите города через запятую: ").split(',')
    cities = [c.strip() for c in cities if c.strip()]
    
    coords = {}
    for city in cities:
        lat = get_coordinates(city)
        if lat is not None:
            coords[city] = lat
    
    if coords:
        southern = min(coords.items(), key=lambda x: x[1])
        print(f"Самый южный город: {southern[0]}")
    else:
        print("Не удалось определить координаты")

if __name__ == "__main__":
    main()