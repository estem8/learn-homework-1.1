import requests
from setting import weather_api_key
from geopy.geocoders import Nominatim


def get_my_ip() -> str:
    url='https://ident.me'
    my_ip = requests.get(url=url)
    return my_ip.text
    
def get_geo_by_ip() -> dict:
    url='http://ip-api.com/json/'
    geo_data = requests.get(url, get_my_ip())
    return geo_data.json()

def get_weather() -> dict:
    weather_url = 'http://api.openweathermap.org/data/2.5/weather'
    city = get_geo_by_ip()['city']
    params = {
        'q': city,
        'appid': weather_api_key
        }
    result = requests.get(weather_url,params=params) 
    weather_data = result.json()
    return weather_data

def get_city_name_by_coord():
    data = get_geo_by_ip()
    latitude = data['lat']
    longitude = data['lon']
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.reverse((latitude, longitude), language='ru')
    if location and 'address' in location.raw:
        city_name = location.raw['address'].get('city', '')
        return city_name
    else:
        return None

def main():
    pass

if __name__=='__main__':
    main()