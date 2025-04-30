import requests

print("\n--- Making a PUT Request to JSONPlaceholder ---\n")

# 
url = "https://jsonplaceholder.typicode.com/posts/1"

# 
updated_data = {
    "id": 1,
    "title": "Hey Tom i am very thankful to you ",
    "body": "Tom your best teacher.",
    "userId": 1
}


response = requests.put(url, json=updated_data)


print("Status Code:", response.status_code)

if response.status_code == 200:
    print("✅ Post updated successfully!")
    print("📦 Updated Data:")
    print(response.json())
else:
    print("❌ Failed to update post. Response:")
    print(response.text)
