import requests

from pprint import pprint

lat = 37.56

lon = 126.97

api_key = 'd127ddf90fd5dbfeb5aa6547c8dd9067'
# '737b00c4d5656ff8b3a3a6b96af2d269'

url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}'

response = requests.get(url).json()
pprint(response)
print(type(response))


# temp = response['main']['temp']g

# print(f'온도 = {temp}')

city = "Seoul,KR"
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'