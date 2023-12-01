from src.classic_weather import get_weather, get_my_ip, get_geo_by_ip, get_city_name_by_coord

def generate_template()-> dict:
    """Генератор data для render template"""    
    data = get_weather()
    data_by_ip = get_geo_by_ip()
    city_by_cord = get_city_name_by_coord()

    refactoring_data = {
        'my_ip': get_my_ip(),
        'longitude': data['coord']['lon'],
        'latitude': data['coord']['lat'],
        'country': data_by_ip['country'],
        'city': data_by_ip['city'],
        'weather': data['weather'][0]['description'],
        'city_by_cord': city_by_cord,
    }
    return refactoring_data

def main():
    pass

if __name__=='__main__':
    main()