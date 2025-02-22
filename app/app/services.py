import requests
import openai
from flask import current_app
from config import Config

class AIService:
    def __init__(self):
        self.openai_keys = Config.OPENAI_API_KEYS
        self.current_key_index = 0

    def get_response(self, prompt):
        try:
            openai.api_key = self._get_current_key()
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            current_app.logger.error(f"OpenAI Error: {str(e)}")
            return None

    def _get_current_key(self):
        key = self.openai_keys[self.current_key_index]
        self.current_key_index = (self.current_key_index + 1) % len(self.openai_keys)
        return key

class WeatherService:
    @staticmethod
    def get_weather(city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C"
        return "Failed to retrieve weather data"
