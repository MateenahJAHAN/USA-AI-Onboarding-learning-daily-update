import requests


url = "https://api.github.com/events"


response = requests.get(url)


print("Status Code:", response.status_code)


if response.status_code == 200:
    data = response.json()  
    print("First Public Event:")
    print(data[0])  
else:
    print("Failed to fetch data. Response:")
    print(response.text)
