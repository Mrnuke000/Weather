# importing requests and json
#imports
import requests, json
import replit
from replit import db
import os 
API = os.environ['APIK']
db["CITY"] = "Solana Beach"
CITY = db["CITY"]
#storing keys

# base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
keys = db.keys()
API_KEY = API
#CITY = "Solana Beach"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
#URL = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=e5edf2a56c8fa822eee2177b99fa886b"
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   temperature = temperature - 273.15
   temperature = temperature * 1.8
   temperature = temperature + 32
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature} F")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
elif response.status_code == 401:
  print('API KEY IS INVALID')
else:
   # showing the error message
   print("Error in the HTTP request")

#--------------------------------------
if report ==  'clear sky' or  report == 'rainy':
    wear = 'a rain jacket'
elif report == 'snow':
    wear = 'a warm jacket'
elif report == 'Clear':
  wear = 'some shorts'
else:
    wear = 'sandals'

#print('todays weather is ' report ' and its ' + Temperature + ' F outside, you should wear ' + wear ) 