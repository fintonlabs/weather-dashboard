from flask import Flask, jsonify, request
import requests
import datetime

app = Flask(__name__)

API_KEY = 'your_openweathermap_api_key'  # replace with your API key

@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Fetches weather data for a given location from OpenWeatherMap API
    """
    location = request.args.get('location', default='London,uk', type=str)
    current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}'

    try:
        current_weather_response = requests.get(current_weather_url)
        forecast_response = requests.get(forecast_url)

        current_weather_response.raise_for_status()
        forecast_response.raise_for_status()

        current_weather_data = current_weather_response.json()
        forecast_data = forecast_response.json()

        processed_current_weather_data = process_current_weather_data(current_weather_data)
        processed_forecast_data = process_forecast_data(forecast_data)

        return jsonify({
            'current_weather': processed_current_weather_data,
            'forecast': processed_forecast_data
        })

    except requests.exceptions.HTTPError as err:
        return jsonify({'error': str(err)}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def process_current_weather_data(data):
    """
    Processes the current weather data to a more readable format
    """
    return {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'description': data['weather'][0]['description']
    }


def process_forecast_data(data):
    """
    Processes the forecast data to a more readable format
    """
    processed_data = []
    for forecast in data['list']:
        processed_data.append({
            'date': datetime.datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d %H:%M:%S'),
            'average_temperature': forecast['main']['temp'],
            'min_temperature': forecast['main']['temp_min'],
            'max_temperature': forecast['main']['temp_max'],
            'humidity': forecast['main']['humidity'],
            'wind_speed': forecast['wind']['speed'],
            'description': forecast['weather'][0]['description']
        })
    return processed_data


if __name__ == '__main__':
    app.run(debug=True)