import requests

# Srinagar, Kashmir my city
lat = 34.0837
lon = 74.7973

# my API key
api_key = "9b5a722f72bf70e91afc8b1b2efe206c"

# Weather API URL
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# GET request
response = requests.get(url)

# JSON response
data = response.json()

# Print results
print("📍 City:", data["name"])
print("🌡️ Temperature:", data["main"]["temp"], "°C")
print("☁️ Weather:", data["weather"][0]["description"])
