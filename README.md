![pylint](https://img.shields.io/badge/pylint-1.95-red?logo=python&logoColor=white)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

# server.py
Тренировочный Flask проект получения погоды
1. По ip пользователя 
2. По прямому запросу города.
3. По координатам lon, lat
4. или манипуляции с остаточными данными

## Getting Started
### Prerequisites
* [Python >= 3.6](https://www.python.org/downloads/)
* pip install Flask

#### Running manually using command line
```
python server.py
```
#### Server url
```
http://127.0.0.1:5000/
Через ООП наследование классов
Как мне кажется самый правильный вариант
```
```
http://127.0.0.1:5000/lvl_one
Обычными функциями
Разница в том что есть import Nominatim для получения названия города по lat, lon
```

```
http://127.0.0.1:5000/lvl_two
Через ООП Класс Weather
```
```
http://127.0.0.1:5000/lvl_three
Через бот - не разобрался как работает get, post в Flask :(
```
![alt text](Screenshot.png)
