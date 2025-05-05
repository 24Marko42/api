import requests

start = 0
url = 'http://olympus.realpython.org/profiles'
response = requests.get(url)

html_text = response.text

while True:
    # находим индекс тега
    href_index = html_text.find('<a href="/profiles', start)
    if href_index == -1:  # Если больше не найдено
        break

    # находим начальный индекс содержимого
    start_index = href_index + len('<a href="/profiles')

    # находим конечный индекс содержимого
    end_index = html_text.find('"', start_index)

    # вырезаем содержимое
    a = html_text[start_index:end_index]
    print(url+a)
    start = end_index + 1