import requests

# my token
token = "ke"

# my GitHub username and repo
owner = "MateenahJAHAN"
repo = "USA-AI-Onboarding-learning-daily-update"

#  GitHub API endpoint to get repo info
url = f"https://api.github.com/repos/{owner}/{repo}"

#  Headers including Bearer token and Accept header
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

# Send GET request
response = requests.get(url, headers=headers)

#  Print results
print("Status Code:", response.status_code)
print("Repo Info:", response.json())
