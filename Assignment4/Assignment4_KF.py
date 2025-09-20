import json
import ssl
import textwrap
from urllib.request import urlopen

def get_forecast_data():
    url = "https://api.weather.gov/points/40.1934,-85.3864"
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    weatherData = json.loads(response.read())
    forecastUrl = weatherData["properties"]["forecast"]
    response2 = urlopen(forecastUrl, context=context)
    return json.loads(response2.read())

def print_forecast():
    forecastData = get_forecast_data()
    wrapper = textwrap.TextWrapper(width=70, subsequent_indent="\t")
    for data in forecastData["properties"]["periods"]:
        print( "name:" , data["name"])
        print("temperature:" , data["temperature"])
        print("Detailed forecast:", wrapper.fill(data["detailedForecast"]), "\n")
        
if __name__ == "__main__":
    print_forecast()