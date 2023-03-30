import requests
import json
from pprint import pprint as pp
from json import JSONDecodeError
import time

class Town:
    def __init__(self,name,lat,lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.getData()
    
    def getData(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid=ae11ed6088c4b3fe5c09144419adb1d0'
        parmateres = {'APPID': 'ae11ed6088c4b3fe5c09144419adb1d0', 'q': 'Piscataway,NJ,US'}
        r = requests.get(url, params= parmateres)

        #PRinting the data for Piscataway< New Jersey
        #print("The Requested data via API of Piscataway, NJ is: ")
        dataobj = r.json()
        time.sleep(1)
        #print(json.dumps(dataobj, indent= 4))
        print()
        
        print("The keys of the Requested API are:")
        time.sleep(1)
        pp(((list(dataobj.keys()))))
        print()

        try:
            self.name = dataobj['name']
        except JSONDecodeError as error:
            print("JSON DATA decoding error:")
            print(error.msg)
            print("The error line number is : ", error.lineno)
            print("The column number is:", error.colno)

        try:
            self.temp = dataobj['main']['temp']
        except JSONDecodeError as error1:
            print("JSON DATA decoding error:")
            print(error1.msg)
            print("The error line number is : ", error1.lineno)
            print("The column number is:", error1.colno)

        try:
            self.visibilty = dataobj['visibility']
        except JSONDecodeError as error2:
            print("JSON DATA decoding error:")
            print(error2.msg)
            print("The error line number is : ", error2.lineno)
            print("The column number is:", error2.colno)

        try:
            self.country = dataobj['sys']['country']
        except JSONDecodeError as error3:
            print("JSON DATA decoding error:")
            print(error3.msg)
            print("The error line number is : ", error3.lineno)
            print("The column number is:", error3.colno)

        try:
            self.timezone = dataobj['timezone']
        except JSONDecodeError as error4:
            print("JSON DATA decoding error:")
            print(error4.msg)
            print("The error line number is : ", error4.lineno)
            print("The column number is:", error4.colno)
    
        try: 
            self.weather = dataobj['weather']
        except JSONDecodeError as error5:
            print("JSON DATA decoding error:")
            print(error5.msg)
            print("The error line number is : ", error5.lineno)
            print("The column number is:", error5.colno)
       
    def printing_all_the_values(self):
        units = 'F'

        print(f"The name of the {name} is : {self.name}")
        time.sleep(1)
        print()

        print(f"{name} is in which country?: {self.country}")
        time.sleep(1)
        print()

        print(f"The timezone of {name} is: {self.timezone}")
        time.sleep(1)
        print()

        print(f"The Temperature in {name} is: {self.temp} {units}")
        time.sleep(1)
        print()
        
        print(f"The visibilty in {name} is: {self.visibilty}")
        time.sleep(1)
        print()

        print(f"The weather in {name} is: {self.weather}")
        time.sleep(1)
        print()


name = input("City Name : ")
lat = input("Latitude : ")
lon = input ("Longitude : ")

my_town = Town(name, lat, lon)
my_town.printing_all_the_values()

#Use
#City Name : Piscataway,NJ
#Latitude : 40.5549 
# Longitude : 74.4643