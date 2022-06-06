import requests
KELVIN = 273.15


def weather_in_chosen_city():
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    city_name = input('Please fill up your city:\n')
    api_key = 'd82759ebf4a4a5ed987117c4027b9dfa'  # if api_key not works, generate yours on website
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    r_data = response.json()
    if r_data["cod"] != "404":
        y = r_data['main']
        current_t_kelvin = y['temp']
        current_t = round(current_t_kelvin - KELVIN)
        current_p = y["pressure"]
        z = r_data["weather"]
        weather_description = z[0]["description"]
        return f'In {city_name} {weather_description}. ' \
               f'Current temperature is {current_t}°C, pressure is {current_p}hPa.'
    else:
        return 'City not found'


if __name__ == '__main__':
    print(weather_in_chosen_city())


"""
1. создать функцию(ии) для  определения погоды по данным(Город).
2. Вынести некоторрые данные в константу(ы).
3. Для запуска функции использовать if __name__ == '__main__': запуск!
4. Создать файл test.py  внутри создать Класс для тестирования функции, с помощью unittest.
"""