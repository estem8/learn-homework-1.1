import requests
from setting import weather_api_key

class City:
    def __init__(self, name=None, lon=None, lat=None):
        if name is None:
            name = 'Moscow'
        self.name = name

        if lon is None or lat is None:
            self.lon, self.lat = self.get_cord_from_web()
        else:
            self.lon = lon
            self.lat = lat


    # @property
    # def cord(self):
    #     return self.lon, self.lat
    
    # @cord.setter
    # def cord(self, num):
    #     lo,la = num
    #     if abs(lo) <= 90 and abs(la) <= 90:
    #         self.lon = lo
    #         self.lat = la
    #     else:
    #         print('Получены не корректные данные')
    
    @staticmethod
    def get_cord_from_web():
        url='https://api.ipify.org'
        ip_data = requests.get(url).text

        url='http://ip-api.com/json/'
        data = requests.get(url,ip_data).json()
        longitude = data['lon']
        latitude = data['lat']
        return longitude, latitude

class Weather(City):
    def __init__(self, temperature = None, description = None):
        super().__init__()

        if temperature is None and description is None:
            self.temperature,self.description = self.get_weather()
        else:
            self.temperature = temperature
            self.description = description

    @staticmethod        
    def get_weather(self):
        weather_url = 'http://api.openweathermap.org/data/2.5/weather'
        name = City(self.name)
        params = {
            'q' : name,
            'appid' : weather_api_key,
        }
        result = requests.get(url=weather_url,params=params).json()
        
        temperature = result['main']['temp']
        description = result['weather'][0]['main']

        return temperature, description

w = Weather()
print(w.__dict__)

# w = City()
# print(w.__dict__)