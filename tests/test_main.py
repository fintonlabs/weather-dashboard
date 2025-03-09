import unittest
from main import process_current_weather_data, process_forecast_data

class TestMain(unittest.TestCase):

    def test_process_current_weather_data(self):
        data = {
            'main': {'temp': 300, 'humidity': 80},
            'wind': {'speed': 5},
            'weather': [{'description': 'clear sky'}]
        }
        result = process_current_weather_data(data)
        self.assertEqual(result, {
            'temperature': 300,
            'humidity': 80,
            'wind_speed': 5,
            'description': 'clear sky'
        })

    def test_process_forecast_data(self):
        data = {
            'list': [
                {
                    'dt': 1622476800,
                    'main': {'temp': 300, 'temp_min': 290, 'temp_max': 310, 'humidity': 80},
                    'wind': {'speed': 5},
                    'weather': [{'description': 'clear sky'}]
                }
            ]
        }
        result = process_forecast_data(data)
        self.assertEqual(result, [
            {
                'date': '2021-05-31 12:00:00',
                'average_temperature': 300,
                'min_temperature': 290,
                'max_temperature': 310,
                'humidity': 80,
                'wind_speed': 5,
                'description': 'clear sky'
            }
        ])

if __name__ == '__main__':
    unittest.main()