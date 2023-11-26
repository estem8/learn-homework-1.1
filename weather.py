import requests
from setting import weather_api_key

def get_my_ip():
    url='https://ident.me'
    my_ip = requests.get(url=url)
    return my_ip.text
    
def get_geo_by_ip():
    url='http://ip-api.com/json/'
    geo_data = requests.get(url, get_my_ip())
    return geo_data.text

def get_weather():
    weather_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': 'Moscow',
        'appid': weather_api_key
        }
    result = requests.get(weather_url,params=params) 
    weather_data = result.json()
    return weather_data



if __name__=='__main__':
    get_weather()