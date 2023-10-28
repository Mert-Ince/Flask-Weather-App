import requests
from dataclasses import dataclass

@dataclass
class WeatherData:
    name: str
    main: str
    description: str
    icon: str
    temperature: float

lst=[]

def get_lan_lon(city_name, state_code, country_code):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid=8c75b6c97584542d7ad47ab831518ef2').json()

    data = resp[0]
    lat, lon = data.get("lat"), data.get("lon")
    return lat, lon

def get_current_weather(lat, lon):
    resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid=8c75b6c97584542d7ad47ab831518ef2").json()
    data = WeatherData(
        name=resp.get("name"),
        main=resp.get("weather")[0].get("main"),
        description=resp.get("weather")[0].get("description"),
        icon=resp.get("weather")[0].get("icon"),
        temperature=resp.get("main").get("temp")
    )
    return data

def get_weather_forecast(lat, lon):
    resp = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid=8c75b6c97584542d7ad47ab831518ef2").json()
    i = 7
    lst.clear()
    while i < 40:
        date=resp.get("list")[i].get("dt_txt"),
        main=resp.get("list")[i].get("weather")[0].get("main"),
        icon=resp.get("list")[i].get("weather")[0].get("icon"),
        temperature=resp.get("list")[i].get("main").get("temp")
        dates = str(date)
        mains = str(main)
        icons = str(icon)
        temperaturef = str(temperature)
        dates = dates.replace(', ', '\n').replace("'", '').replace('(', '').replace(')', '').replace(',', '')
        mains = mains.replace(', ', '\n').replace("'", '').replace('(', '').replace(')', '').replace(',', '')
        icons = icons.replace(', ', '\n').replace("'", '').replace('(', '').replace(')', '').replace(',', '')
        temperaturef = temperaturef.replace(', ', '\n').replace("'", '').replace('(', '').replace(')', '').replace(',', '')
        lst.append(dates)
        lst.append(mains)
        lst.append(icons)
        lst.append(temperaturef)
        i += 8
    return lst

def main(city_name, state_name, country_name):
    lat, lon = get_lan_lon(city_name, state_name, country_name)
    weather_data=get_current_weather(lat, lon)
    return weather_data

def mainf(city_name, state_name, country_name):
    lat, lon = get_lan_lon(city_name, state_name, country_name)
    weather_f=get_weather_forecast(lat, lon)
    return weather_f

if __name__ == "__main__":
    lat, lon = get_lan_lon("Toronto", "ON", "Canada")
    print(get_current_weather(lat, lon))
    print(get_weather_forecast(lat, lon))