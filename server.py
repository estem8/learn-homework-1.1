from flask import Flask, request, render_template

from dotenv import load_dotenv
from os.path import join, dirname
import os

from lvl_one import generate_template
from weather_as_class import Weather



app = Flask(__name__)

def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)




@app.route('/lvl_one')
def lvl_one():
    data = generate_template()
    return render_template('index.html', data = data)


@app.route('/lvl_two')
def lvl_two():
    data = Weather.create_data_with_my_ip()
    print(data.__dict__)
    return render_template('index.html', data = data)


if __name__=='__main__':
    app.run(debug=True)
