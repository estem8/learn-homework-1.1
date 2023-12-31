from flask import Flask, request, render_template

import requests

from dotenv import load_dotenv
from os.path import join, dirname
import os

from src.lvl_one import generate_template
from src.lvl_two import Weather as Weather_two
from src.lvl_four import Weather as Weather_four

from setting import *


app = Flask(__name__)

def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)

#Через ООП наследование классов
@app.route('/')
def lvl_four():
    data = Weather_four()
    return render_template('lvl_four.html', data = data)

#Обычными функциями - работает
@app.route('/lvl_one')
def lvl_one():
    data = generate_template()
    return render_template('index.html', data = data)

#Через ООП Класс Weather - работает
@app.route('/lvl_two')
def lvl_two():
    data = Weather_two.create_data_with_my_ip()
    return render_template('index.html', data = data)


#Через бот - не работает post :(
@app.route('/lvl_three', methods=['GET', 'POST'])
def receive_update():
    if request.method == 'POST':
        chat_id = request.json['chat']['id']
        send_message(chat_id)
    return {'ok': True}

if __name__=='__main__':
    app.run(debug=True)
