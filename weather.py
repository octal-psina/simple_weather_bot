import json
import requests
import openweather_key

#import telebot

class Weather:
  def __init__(self, city):
    self.city = city

  def get_lat_lon(self):
    """Получение широты и долготы запрашиваемого города"""
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=1&appid={openweather_key.key}"
    city_lat_lon = requests.get(url).json()
    #обращение к API openweather получение json city lat, lon
    # запись информации в файл json
    #with open("city_lat_lon.json", "w") as f:
    #result_lat_lon = json.dump(city_lat_lon, f)
    return city_lat_lon
  
  def get_city_weather(self):
    """Получение широты и долготы из файла city_lat_lon.json"""
    try:
      json_data = Weather.get_lat_lon(self)
      lat = json_data[0]["lat"]
      lon = json_data[0]["lon"]
      url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_key.key}&units=metric"
      city_weather = requests.get(url).json()
    except (IndexError):
      city_weather = False
    return city_weather
  
  def show_city_weather(self):
    json_data = Weather.get_city_weather(self)

#    with open("weather.json", "w") as f:
#        json.dump(json_data, f)
    if json_data != False:
      dict_weather_info = {} 
      dict_weather_info['name_city'] = json_data["name"]
      dict_weather_info['weather'] = json_data['weather'][0]["main"]
      dict_weather_info['wearher_description'] = json_data['weather'][0]["description"]
      dict_weather_info['temp'] = json_data['main']['temp']
      dict_weather_info['humidity'] = json_data['main']['humidity']
      dict_weather_info['wind'] = json_data['wind']['speed']
      #weather_info = f"Город:{self.city}\nПогода: {weather}\nТемпература: {temp}C\nВлажность: {humidity}%\nСкорость ветра: {wind} м/c"
      #print(f"Город:{self.city}\nПогода:{weather}\nТемпература:{temp}C\nВлажность:{humidity}%\nСкорость ветра:{wind} м/c")
    else:
      dict_weather_info = f"Извините нам не известен город:\n{self.city}"
    return 	dict_weather_info  
	  
#weather_moscow = Weather("ташкент")
#print(weather_moscow.show_city_weather())


# from urllib.request import urlopen
# def get_ip_data(self):
#     url = 'https://ifconfig.me/all.json'
#     response = urlopen(url)
#     return json.load(response)
# ip = Weather.get_ip_data(self)
#     print(ip["ip_addr"])
#     your_ip = ip["ip_addr"]
