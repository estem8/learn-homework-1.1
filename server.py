from flask import Flask, request, render_template
import requests
from weather import get_weather

app = Flask(__name__)




def generate_template():
    # data = get_weather()
    return get_weather()


@app.route('/')
def hello():
    data = generate_template()

    return render_template('index.html', data = data)

if __name__=='__main__':
    app.run(debug=True)
