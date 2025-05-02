import requests

# my  GitHub token
token = "secret key"  

# my details
owner = "MateenahJAHAN"
repo = "USA-AI-Onboarding-learning-daily-update"
issue_number = 2  

# API endpoint to update issue
url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

payload = {
    "title": " Updated Issue Title (via PATCH)",
    "body": " This issue has been updated using Python PATCH request."
}

response = requests.patch(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
