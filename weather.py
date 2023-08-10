import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("API_KEY")

def get_lan_lon(city_name,state_code,country_code,API_key):
    ## Get the response object from the endpoint and convert it to json format
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}").json()
    
    ## Accesing just the dictionary portion(the response is a list object)
    data = response[0]

    lat , lon = data.get("lat") ,data.get("lon")
    return lat , lon 

def get_current_weather(lat, lon, API_key):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}").json()
    
if __name__ == "__main__":
    lat, lon = get_lan_lon("Toronto", "ON", "Canada", api_key)
    get_current_weather(lat, lon, api_key)


