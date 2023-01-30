import json
import urllib.request 

map_city_to_coords = {
    'Abuja': 'lat=9.0764785&lon=7.398574',
    'Nairobi': 'lat=-1.2920659&lon=36.8219462',
    'Accra': "lat=5.6037168&lon=-0.1869644",
    'Denver': "lat=39.7392&lon=-104.985"

}
        
def show_weather_to_user(weather_data_list):
    for weather_data in weather_data_list:
        hour_number = weather_data['timepoint']
        temperature = weather_data['temp2m']
        wind_direction = weather_data['wind10m']['direction']
        print(f'On hour {hour_number},')
        if hour_number == 24:
            print('(in one day)')
        elif hour_number == 48:
            print('(in two days)')
        else:
            print('(in three days)')

        if wind_direction == "N":
            wind_direction = "From the North"
        elif wind_direction == "S":
            wind_direction = "From the South"
        elif wind_direction == "W":
            wind_direction = "From the West"
        elif wind_direction == "E":
            wind_direction = "From the East"
        elif wind_direction == "NW":
            wind_direction = "From the North West"
        elif wind_direction == "NE":
            wind_direction = 'From the North East'
        elif wind_direction == "SE":
            wind_direction = "From the South East"
        else:
            wind_direction = "From the South West"

        print(f'The wind direction is {wind_direction} and this is the temperature {temperature}')

def show_weather():
    city_name = input('Please type a city: ')
    if city_name not in map_city_to_coords:
        print('We do not have coordinates for that city.')
    else:
        get_api_results(city_name)
        with open('api_output.json', 'r') as f:
            all_data = json.load(f)
            weather_data_list = all_data['dataseries']
        
        
        show_weather_to_user(weather_data_list)



def get_api_results(city):
    coords = map_city_to_coords[city]
    url = ('https://www.7timer.info/bin/astro.php?' + 
        f'{coords}&ac=0&unit=metric&output=json')
    results = urllib.request.urlopen(url)
    json_content = results.read().decode('utf-8')
    with open('api_output.json', 'w') as f:
        f.write(json_content)

show_weather()
