import requests
import config


class WeatherChecker:
    URL = "https://api.openweathermap.org/data/2.5/"

    def get_city_coordinates(self, user_city: str, user_lang: str):
        # Getting a city's coordinates first
        response = requests.get(url=f"{self.URL}weather",
                                params={"q": user_city, "lang": user_lang, "appid": config.WEATHER_TOKEN})
        response.raise_for_status()
        city_coordinates = response.json()

        return city_coordinates["coord"]

    def will_rain(self, city_coordinates):
        lon = city_coordinates["lon"]
        lat = city_coordinates["lat"]

        # Using the "exclude" parameter it is possible to exclude some parts of the response. Only "hourly" is left.
        parameters = {
            "lon": lon,
            "lat": lat,
            "appid": config.WEATHER_TOKEN,
            "exclude": "currently,minutely,daily"
        }

        response = requests.get(url=f"{self.URL}onecall", params=parameters)
        response.raise_for_status()

        data = response.json()

        weather_ids = [hourly_forecast["weather"][0]["id"] for hourly_forecast in data["hourly"]][:12]

        for id in weather_ids:
            if id < 700:
                return True

        return False
