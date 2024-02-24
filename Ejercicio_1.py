import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
    TEMP_MAX = 28

    @classmethod
    def is_hot_in_pehuajo(cls):
        try:
            url = f'{cls.API_ENDPOINT}?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric'
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción en caso de error HTTP

            data = response.json()
            temp = data['main']['temp']

            return temp > cls.TEMP_MAX

        except requests.RequestException:
            # Manejar cualquier excepción HTTP
            return False
