import requests
from flask import Flask, render_template, jsonify
from configure import WEATHER_API_KEY

CITY = "Moscow"

app = Flask(__name__)
app.json.ensure_ascii = False

def weather():
    params = {
        "key": WEATHER_API_KEY,
        "q": CITY,
        "lang": "en"
    }

    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params=params,
        timeout=10
    )
    data = response.json()
    our_data = {
        "city": data["location"]["name"],
        "timezone": data["location"]["tz_id"],
        "temp": round(data["current"]["temp_c"]),
        "feels": round(data["current"]["feelslike_c"]),
        "text": data["current"]["condition"]["text"]
    }
    return our_data

@app.route("/")
def index():
    return render_template("index.html", w=weather())

@app.route("/api/weather")
def api():
    return jsonify(weather())

app.run(debug=True, port=5001)
