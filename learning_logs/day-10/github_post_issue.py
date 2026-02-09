import requests

# my github api 
token = "secret key"  

# My GitHub username and repo name
owner = "MateenahJAHAN"
repo = "USA-AI-Onboarding-learning-daily-update"

# GitHub API endpoint for creating an issue
url = f"https://api.github.com/repos/{owner}/{repo}/issues"

# Headers with authentication and content type
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

# Data for the new issue
payload = {
    "title": "Day 10 API Practice Issue",
    "body": "This issue was created using a POST request in Python."
}

# Send POST request
response = requests.post(url, headers=headers, json=payload)

# Show the response
print("Status Code:", response.status_code)
print("Response:", response.json())
