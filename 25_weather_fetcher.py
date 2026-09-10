"""Simple weather fetcher using a public API."""

import requests


def get_weather(city: str, api_key: str) -> dict:
    """Fetch current weather for a city using OpenWeatherMap API."""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return {
        "city": data.get("name"),
        "temperature": data.get("main", {}).get("temp"),
        "description": data.get("weather", [{}])[0].get("description"),
        "humidity": data.get("main", {}).get("humidity"),
        "wind_speed": data.get("wind", {}).get("speed"),
    }


def format_weather(weather: dict) -> str:
    return (
        f"Weather in {weather['city']}:\n"
        f"  Temperature: {weather['temperature']}\u00b0C\n"
        f"  Conditions:  {weather['description']}\n"
        f"  Humidity:    {weather['humidity']}%\n"
        f"  Wind:        {weather['wind_speed']} m/s"
    )


if __name__ == "__main__":
    import os

    api_key = os.getenv("OPENWEATHER_API_KEY", "your_api_key_here")
    try:
        weather = get_weather("London", api_key)
        print(format_weather(weather))
    except Exception as e:
        print(f"Error fetching weather: {e}")
