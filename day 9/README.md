# Day 9 Learning Log –  Weather API Practice

## Weather API – Srinagar, Kashmir

**Tools used:**
* VS Code (Python)
* Postman

### Achievements:
* Created a weather API request for Srinagar kashmir using Python and the `requests` module
* Used the OpenWeatherMap endpoint to **GET** real-time weather data
* Parsed and printed:
   * City Name
   * Temperature (°C)
   * Weather Condition

### Code Implementation:

```python
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
print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Weather:", data["weather"][0]["description"])
```

### Postman Setup:
* Created a **collection** and **environment** named `weather_api_env`
* Used variables like `{{city}}`, `{{api_key}}`, and `{{url}}`
* Sent **CRUD-style requests** (GET, POST, PUT, DELETE simulated)
* Learned to configure **headers**, interpret **responses**, and save requests properly

## API Concepts Revised (from Day 1 video)
* I watched again day 1 video to make my foundation strong
* Difference between **HTTP** and **HTTPS**
* What is an **endpoint**
* What is a **header** and how to write it
* How to read and understand API **responses**
  

## Scaler Python Learning: Lists

### Concepts Learnt:
* Syntax of lists:
  ```python
  my_list = [1, 2, 3, "hello", True]
  ```
* Key Features of Lists:
   * **Ordered** (maintains sequence)
   * **Mutable** (can be changed)
   * **Allows duplicates**
   * Can contain **mixed data types**

### List Operations Explored:
* Indexing: `my_list[0]`
* Appending: `my_list.append("new")`
* Removing: `my_list.remove(2)`
* Slicing: `my_list[1:3]`

### Practice Examples I Created:

#### Example 1: Appending items to a list
```python
# Creating a shopping list
shopping = ["milk", "bread", "eggs"]
print("Original shopping list:", shopping)

# Adding items using append
shopping.append("butter")
print("After adding butter:", shopping)

# Adding another item
shopping.append("cheese")
print("Final shopping list:", shopping)
```

#### Example 2: Using index to access and modify list items
```python
# List of my favorite movies
movies = ["Inception", "Interstellar", "Dark Knight", "Titanic"]
print("My second favorite movie is:", movies[1])

# Changing my mind about one movie
movies[3] = "Avatar"
print("Updated movie list:", movies)
```

#### Example 3: Removing items from a list
```python
# List of cities I want to visit
cities = ["Paris", "New York", "Tokyo", "Dubai", "London"]
print("Cities I want to visit:", cities)

# Removing a city I already visited
cities.remove("Dubai")
print("After removing Dubai:", cities)

# Another way to remove using index with pop()
removed_city = cities.pop(1)  # Removes and returns New York
print(f"I just visited {removed_city}")
print("Remaining cities to visit:", cities)
```

#### Example 4: Slicing lists to get portions
```python
# My weekly schedule
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Full week:", week)

# Getting just weekdays
weekdays = week[0:5] 
print("Weekdays:", weekdays)

# Getting weekend days
weekend = week[5:7]  
print("Weekend days:", weekend)
```

### Practice Questions I Solved:

1. **Appending Question**: Create a list of 3 friends' names. Then add 2 more friends and print the final list.
   ```python
   friends = ["Rahul", "Amit", "Priya"]
   friends.append("Neha")
   friends.append("Sanjay")
   print("My friends:", friends)
   ```

2. **Indexing Question**: Create a list of 5 colors. Print the 1st, 3rd, and last color using positive and negative indexing.
   ```python
   colors = ["red", "blue", "green", "yellow", "purple"]
   print("First color:", colors[0])
   print("Third color:", colors[2])
   print("Last color:", colors[4])  # or colors[-1]
   
   # Using negative indexing
   print("First color with negative index:", colors[-5])
   print("Third color with negative index:", colors[-3])
   print("Last color with negative index:", colors[-1])
   ```

3. **Removing Question**: Create a list of 4 fruits. Remove the second fruit and print the list. Then remove 'apple' if it exists in the list.
   ```python
   fruits = ["banana", "apple", "orange", "grape"]
   # Remove second fruit
   del fruits[1]  # removes apple
   print("After removing second fruit:", fruits)
   
   # Try to remove apple if it exists
   if "apple" in fruits:
       fruits.remove("apple")
   else:
       print("Apple is not in the list anymore")
   print("Final fruit list:", fruits)
   ```

4. **Slicing Question**: Create a list of numbers from 1 to 10. Use slicing to get even numbers and odd numbers in separate lists.
   ```python
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   # Get even numbers (starting from index 1, step 2)
   even_numbers = numbers[1::2]
   # Get odd numbers (starting from index 0, step 2)
   odd_numbers = numbers[0::2]
   print("Even numbers:", even_numbers)
   print("Odd numbers:", odd_numbers)
   ```

## Summary:
Today was all about **reinforcing API fundamentals**, building hands-on practice in **Python and Postman**, and revising Python core concepts like **lists**.

* Practical understanding of **real-world API workflows**
* Stronger command on tools like **Postman & requests**
* Improved confidence in reading/writing Python lists
