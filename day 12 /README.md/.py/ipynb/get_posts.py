import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# 1) Locate the .env file right next to this script
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# 2) for debug 
BASE_URL = os.getenv("BASE_URL")
print("DEBUG: BASE_URL =", repr(BASE_URL))

# 
if not BASE_URL:
    raise ValueError("BASE_URL is not set—check your .env file")

# 4) now  making the request
response = requests.get(f"{BASE_URL}/posts")
response.raise_for_status()
posts = response.json()

# 5) Output summary
print(f"Got {len(posts)} posts. First post ID:", posts[0]["id"])
