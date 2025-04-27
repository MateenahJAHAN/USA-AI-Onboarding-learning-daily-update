Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Last login: Sat Apr 26 14:55:31 on ttys003
... mateenahjahan@Mateenahs-MacBook-Pro ~ % pip3 install requests
... 
... Requirement already satisfied: requests in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (2.32.3)
... Requirement already satisfied: charset-normalizer<4,>=2 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from requests) (3.4.1)
... Requirement already satisfied: idna<4,>=2.5 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from requests) (3.10)
... Requirement already satisfied: urllib3<3,>=1.21.1 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from requests) (2.4.0)
... Requirement already satisfied: certifi>=2017.4.17 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from requests) (2025.1.31)
... 
... [notice] A new release of pip is available: 24.3.1 -> 25.0.1
... [notice] To update, run: pip3 install --upgrade pip
... mateenahjahan@Mateenahs-MacBook-Pro ~ % python3
... 
... Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
... Type "help", "copyright", "credits" or "license" for more information.
... >>> import requests
... ... import json
... ... 
... ... # API URL
... ... url = 'https://randomuser.me/api/'
... ... 
... ... # Sending a GET request to the API
... ... response = requests.get(url)
... ... python3 random_user.py
... 
... ... # Checking if the request was successful
... ... if response.status_code == 200:
... ...     data = response.json()
... ...     user_data = data['results'][0]
... ...     
... ...     # Printing user information
... ...     print(f"Name: {user_data['name']['title']} {user_data['name']['first']} {user_data['name']['last']}")
... ...     print(f"Gender: {user_data['gender']}")
... ...     print(f"Email: {user_data['email']}")
... ...     
... ...     location = user_data['location']
... ...     print(f"Location: {location['street']['number']} {location['street']['name']}, {location['city']}, {location['state']}, {location['country']}, {location['postcode']}")
... ...     print(f"Coordinates: Latitude {location['coordinates']['latitude']}, Longitude {location['coordinates']['longitude']}")
... ...     print(f"Timezone: {location['timezone']['description']}")
... ...     
... ...     dob = user_data['dob']
... ...     print(f"Date of Birth: {dob['date']}")
... ...     print(f"Age: {dob['age']}")
... ...     
... ...     print(f"Phone: {user_data['phone']}")
... ...     print(f"Cell: {user_data['cell']}")
... ...     
... ...     print(f"Profile Picture (Large): {user_data['picture']['large']}")
... ... else:
... ...     print("Error: Could not fetch data")
... ... 
... 
... Name: Mrs Danya Bannink
... Gender: female
... Email: danya.bannink@example.com
... Location: 714 Hendrik Droststraat, Munnekeburen, Limburg, Netherlands, 0354 VL
... Coordinates: Latitude 37.8859, Longitude 23.4527
... Timezone: Pacific Time (US & Canada)
... Date of Birth: 1966-04-03T03:57:02.901Z
Age: 59
Phone: (0696) 298327
Cell: (06) 45971929
Profile Picture (Large): https://randomuser.me/api/portraits/women/1.jpg
>>> 
>>> exit()
... 
mateenahjahan@Mateenahs-MacBook-Pro ~
