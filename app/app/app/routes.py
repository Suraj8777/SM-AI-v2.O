from flask import render_template, request, jsonify
from .services import AIService, WeatherService
from . import app

ai_service = AIService()
weather_service = WeatherService()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def handle_query():
    user_input = request.json.get('input', '').lower()
    
    if 'weather' in user_input:
        city = user_input.replace('weather', '').strip()
        return jsonify({'response': weather_service.get_weather(city)})
    
    ai_response = ai_service.get_response(user_input)
    return jsonify({'response': ai_response if ai_response else "Sorry, I'm having trouble processing your request"})
