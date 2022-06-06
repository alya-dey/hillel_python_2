import unittest
from unittest.mock import patch
from oleksandra_deinechyna_hw_15 import weather_in_chosen_city


class TestWeather(unittest.TestCase):

    def setUp(self):
        pass

    def test_weather_Kyiv(self):
        # Оскільки в тесті не може бути інпут, замінюємо його на свої значення за допомогою модуля patch і мок-об'єктів:
        with unittest.mock.patch('builtins.input', return_value='Kyiv'):
            self.assertEqual(weather_in_chosen_city(),
                             'In Kyiv scattered clouds. Current temperature is 25°C, pressure is 1019hPa.')
            # Перевіряємо актуальний прогноз https://openweathermap.org/city/703448

    def test_weather_London(self):
        with unittest.mock.patch('builtins.input', return_value='London'):
            self.assertEqual(weather_in_chosen_city(),
                             'In London broken clouds. Current temperature is 15°C, pressure is 1015hPa.')
            # https://openweathermap.org/city/2643743

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
