from flask import Flask, jsonify
import datetime
import pytz

app = Flask(__name__)

def get_time_in_city(city, timezone):
    tz = pytz.timezone(timezone)
    city_time = datetime.datetime.now(tz)
    return f"{city}: {city_time.strftime('%Y-%m-%d %H:%M:%S')}"

@app.route('/')
def world_clock():
    cities = {
        "New York": "America/New_York",
        "London": "Europe/London",
        "Paris": "Europe/Paris",
        "Sydney": "Australia/Sydney",
        "Tokyo": "Asia/Tokyo"
    }

    result = [get_time_in_city(city, timezone) for city, timezone in cities.items()]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
