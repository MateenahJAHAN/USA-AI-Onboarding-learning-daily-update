import requests
import json

#  Your OpenAI API key (keep this private!)
api_key = "secret key"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

#  1. Check Quota (Display)
def check_quota():
    url = "https://api.openai.com/v1/dashboard/billing/credit_grants"
    response = requests.get(url, headers=headers)
    print("\n📊 Quota Check:")
    print("Status Code:", response.status_code)
    print(json.dumps(response.json(), indent=2))

#  2. Create a Chat Completion (like 'Create')
def create_chat(prompt="Tell me a joke about cats"):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=payload)
    print("\n Chat Response (Create + Read):")
    print("Status Code:", response.status_code)
    print(json.dumps(response.json(), indent=2))

#  3. 'Update' & 'Delete' (Simulated)
def simulate_update(prompt):
    print("\n Simulating Update by sending a new modified message...")
    create_chat(prompt)

def simulate_delete():
    print("\n You can't delete an OpenAI chat, but we can simulate clearing context.")
    print(" Context cleared (in real apps, you'd just reset the messages list).")

# Run all operations
if __name__ == "__main__":
    check_quota()  
    create_chat()  
    simulate_update("Actually, tell me a joke about programmers.") 
    simulate_delete()  
