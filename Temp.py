from bs4 import BeautifulSoup
import requests

print("Lets check the weather where would you like to visit today")
city = input("Pick the city you want:")
state = input("What state is this city in?")
url = f'https://www.wunderground.com/weather/us/{state}/{city}'

response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.content,'html.parser')

# temps = soup.find_all('a')
temp = soup.find(class_='wu-value wu-value-to')
# print(temp.text)s
int_temp = int(temp.text)
comfortability = ""

if int_temp >= 90:
    comfortability = "too hot!!!!"
elif int_temp < 90 and int_temp > 65:
    comfortability = "it is just right."
else:
    comfortability = "It is way way too freaking cold!!"
    
print(f"It is currently {int_temp} degrees. It is {comfortability}")