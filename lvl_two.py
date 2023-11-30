
import requests

class Weather:
    def __init__(self, ip = None, lon:float = None, lat:float = None, city:str = None):
        self.ip = ip
        self.lon = lon
        self.lat = lat
        self.city = city

    @staticmethod
    def collect_data() -> dict:
        data = {} 
        url = 'https://api.ipify.org'
        params = {'format':'json'}
        result = requests.get(url=url,params=params).json()
        data['ip'] = result['ip']

        url = 'http://ip-api.com/json/'
        result = requests.get(url, data['ip']).json()
        data['lon'] = result['lon']
        data['lat'] = result['lat']
        data['city'] = result['city']
        return data #на выходе словарь с данными -> которые вызываем из create_data_with_my_ip

    @classmethod
    def create_data_with_my_ip(cls):
        data = cls.collect_data() #вызываем collect_data для того что бы сделать 1 проход
        ip = data['ip']
        lon = data['lon']
        lat = data['lat']
        city = data['city']
        return cls(ip, lon, lat, city)


# w = Weather
# print(w.collect_data())
