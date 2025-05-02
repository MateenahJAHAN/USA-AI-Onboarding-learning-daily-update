import requests
import json

# i write my api key that i generated from openai
api_key = "secret key  # (secured)


url = "https://api.openai.com/v1/chat/completions"


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {secret key}"
}


data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Tell me a joke about cats"}
    ],
    "temperature": 0.7
}


response = requests.post(url, headers=headers, data=json.dumps(data))


print("Status Code:", response.status_code)
print("Raw Response Text:")
print(response.text)


if response.status_code == 200:
    result = response.json()
    reply = result['choices'][0]['message']['content']
    print("\nOpenAI's Response:\n", reply)
else:
    print(" Failed with status code:", response.status_code)
