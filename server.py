from flask import Flask, request, render_template
import requests
from weather import *
from dotenv import load_dotenv
from os.path import join, dirname
import os


app = Flask(__name__)

def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)

def generate_template()-> dict:
    """Генератор data для render template"""    
    data = get_weather()
    data_by_ip = get_geo_by_ip()
    city_by_cord = get_city_name_by_coord()
    refactoring_data = {
        'my_ip':get_my_ip(),
        'longitude': data['coord']['lon'],
        'latitude': data['coord']['lat'],
        'country': data_by_ip['country'],
        'city': data_by_ip['city'],
        'weather': data['weather'][0]['description'],
        'city_by_cord': city_by_cord,

    }

    return refactoring_data


@app.route('/')
def hello():
    data = generate_template()
    return render_template('index.html', data = data)

if __name__=='__main__':
    app.run(debug=True)
