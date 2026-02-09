import requests

# 
token = "key"  

owner = "MateenahJAHAN"
repo = "USA-AI-Onboarding-learning-daily-update"
issue_number = 2  

url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

payload = {
    "state": "closed"
}

response = requests.patch(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
