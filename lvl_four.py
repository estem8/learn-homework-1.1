import requests
from setting import weather_api_key

class City:
    def __init__(self, name=None, lon=None, lat=None):
        if name is None:
            name = self.get_name_from_web()
        self.name = name

        if lon is None or lat is None:
            self.lon, self.lat = self.get_cord_from_web()
        else:
            self.lon = lon
            self.lat = lat
    

    def get_name_from_web(self):
        my_ip = requests.get('https://api.ipify.org').text
        ip_data = requests.get('http://ip-api.com/json/',my_ip).json()
        return ip_data['city']

    # @staticmethod
    
    def get_cord_from_web(self):
        url='https://api.ipify.org'
        ip_data = requests.get(url).text

        url='http://ip-api.com/json/'
        data = requests.get(url,ip_data).json()

        longitude = data['lon']
        latitude = data['lat']
        return longitude, latitude

class Weather(City):
    def __init__(self, temperature = None, description = None, weather_icon = None):
        super().__init__()

        if temperature is None or description is None or weather_icon is None:
            self.temperature,self.description, self.weather_icon = self.get_weather()
        else:
            self.temperature = temperature
            self.description = description

    
    # @staticmethod УДАЛИТЬ :) и больше никогда не использовать
    def get_weather(self):
        weather_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q' : self.name,
            'appid' : weather_api_key,
        }
        result = requests.get(url=weather_url,params=params).json()
        
        temperature = result['main']['temp']
        description = result['weather'][0]['main']
        weather_icon = result['weather'][0]['icon']

        return temperature, description, weather_icon

w = City()
print(w.__dict__)