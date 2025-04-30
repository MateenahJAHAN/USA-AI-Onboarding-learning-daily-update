# Day 8 
## 1. External API Integration: OpenAI (via Python)

### Objective
Practice calling an external API (OpenAI Chat Completion API) using Python's `requests` module to understand authentication, response handling, and error codes.

### API Used
OpenAI Chat API
Endpoint: `https://api.openai.com/v1/chat/completions`

### Methodology
- Language: Python 3.13
- Library: `requests`, `json`
- HTTP Method: `POST`
- Model: `gpt-3.5-turbo`
- Prompt sent: `"Tell me a joke about cats"`
- Authentication: Bearer Token via Authorization Header

### Python Code

```python
import requests
import json


#  My openAI api
api_key = "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"

#  API Endpoint
url = "https://api.openai.com/v1/chat/completions"

#  Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

#  Data (Prompt)
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Tell me a joke about cats"}
    ],
    "temperature": 0.7
}

#  POST Request
response = requests.post(url, headers=headers, data=json.dumps(data))

#  Debug Output
print("Status Code:", response.status_code)
print("Raw Response Text:")
print(response.text)

# If success, print response
if response.status_code == 200:
    result = response.json()
    print("\n Response from OpenAI:\n", result['choices'][0]['message']['content'])
else:
    print(" Failed with status code:", response.status_code)
 

Response Output
Status Code: 429   

{
  "error": {
    "message": "You exceeded your current quota, please check your plan and billing details.",
    "type": "insufficient_quota",
    "code": "insufficient_quota"
  }
}

## 2. __GitHub API (via Python)__

Objective
Use Python to send a GET request to the GitHub public events API and understand how to fetch and handle external API responses.

API Used
GitHub Events API
Endpoint: https://api.github.com/events
Method

Language: Python
Library: requests
HTTP Method: GET
Authentication:  Not required (Public API)
Response Format: JSON (List of public GitHub events)

Python Script code that I wrote
import requests

url = "https://api.github.com/events"

# Make GET request
response = requests.get(url)

print("Status Code:", response.status_code)

# Handle response
if response.status_code == 200:
    data = response.json()
    print("First Public Event:")
    print(data[0])
else:
    print("Failed to fetch data. Response:")
    print(response.text)
Output I got
Status Code: 200
First Public Event:
{
  "id": "32029844893",
  "type": "PushEvent",
  "actor": {
    "login": "example-user",
    ...
  },
  "repo": {
    "name": "octocat/Hello-World",
    ...
  },
  ...
}

Learning Outcomes

Learned how to use requests.get() in Python to call a real API
Understood that some APIs can be accessed without login or an API key (public APIs)
Learned how to convert API response from JSON format into Python dictionaries or lists
Practiced printing specific parts of the API response (like the first item)

3. External API Practice: JSONPlaceholder API (via Python)
Objective
Learn how to send a GET request to a public API (JSONPlaceholder) using Python, and understand how to work with JSON responses.
API Used

## 3. __External API Practice: JSONPlaceholder API (via Python)__

Endpoint: https://jsonplaceholder.typicode.com/posts
(Returns a list of fake blog posts in JSON format used for testing and practice)

Method

Language: Python
Library: requests
HTTP Method: GET
Authentication:  Not required (public API)
Response Format: JSON (list of post dictionaries)

Python Script that I wrote
import requests

# API Endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Send GET request
response = requests.get(url)

# Print status 
print("Status Code:", response.status_code)

# Handle response
if response.status_code == 200:
    data = response.json()
    print("First Post:")
    print(data[0])
else:
    print("Failed to fetch data. Response:")
    print(response.text)
Output that I got
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum..."
}
3.1 JSONPlaceholder API – POST Request
Task
Send a fake blog post using Python requests.post() to https://jsonplaceholder.typicode.com/posts.
Data Sent
{
  "title": "My Mentor is best",
  "body": "His personality is inspiring",
  "userId": 1
}
Output/Response

Status Code: 201 Created
Returned fake post ID: 101
Practiced sending data to an external API using POST
Understood response codes (201) and payload structure

3.2 JSONPlaceholder API – DELETE Request
Task
Send a DELETE request to remove post with ID 1 from https://jsonplaceholder.typicode.com/posts/1.
Response

Status Code: 200 OK
Note: JSONPlaceholder fakes the delete; data isn't really removed.
Learning

Practiced sending a DELETE request using requests.delete()
Understood simulated deletion behavior with 200/204 status codes

3.3 JSONPlaceholder API – PUT Request
Task
Update an existing post (ID 1) using Python requests.put().
Data Sent
{
  "id": 1,
  "title": "Hey Tom I am very thankful to you",
  "body": "Tom your best teacher.",
  "userId": 1
}
Response

Status Code: 200 OK
API returned the updated post (simulated)

Learning

Practiced using PUT method to update data
Understood idempotent requests and full object replacement
