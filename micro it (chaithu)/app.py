from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found.'}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
