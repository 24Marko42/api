# a) Получите координаты Якутска и Магадана в формате JSON. Какой город находится севернее:
# Якутск или Магадан?
# b) Получите координаты вашего родного города и города Торонто в формате JSON. Какой
# город из них находится южнее?
# c) Определите к каким федеральным округам относятся города: Хабаровск, Уфа, Нижний
# Новгород, Калининград, ваш родной город?
# d) Узнайте почтовый индекс КемГУ

a = "https://geocode-maps.yandex.ru/v1/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Якутск&format=json" & \
"https://geocode-maps.yandex.ru/v1/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Магадан&format=json"
# Якуес примерно 62 градуса, Магадан 59. Получается Якутск севернее.

b = "https://geocode-maps.yandex.ru/v1/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Киселевск&format=json" & \
"https://geocode-maps.yandex.ru/v1/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Торонто&format=json"
# Киселевск примерно 53 градуса, Торонто 43. Торонто южнее.

c = "https://geocode-maps.yandex.ru/v1/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Хабаровск&format=json" & \
"https://geocode-maps.yandex.ru/v1/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Уфа&format=json" & \
"https://geocode-maps.yandex.ru/v1/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Нижний Новгород&format=json" & \
"https://geocode-maps.yandex.ru/v1/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Калининград&format=json" & \
"https://geocode-maps.yandex.ru/v1/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Киселевск&format=json"
# Хабаровск - Дальневосточный федеральный округ
# Уфа - Приволжский федеральный округ 
# Нижний Новгород - Приволжский федеральный округ
# Калинингград - Северо-Западный федеральный округ
# Киселевск - Сибирский федеральный округ

d = "https://geocode-maps.yandex.ru/1.x/?apikey=7e1452af-f376-474c-bf50-304551f7e5f6&geocode=Кемерово, Красная, 6&format=json"
# ну, я на всякий случай картинку прикрепил, т.к. получилось, что почтовый адрес "postal_code" 650000,
# но это почтовое отделение, а не почтовый интедс. 
