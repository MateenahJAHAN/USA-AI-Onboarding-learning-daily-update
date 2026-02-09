import requests

print("\n--- Making a DELETE Request to JSONPlaceholder ---\n")

# we have to DELETE endpoint: delete post with ID 1
url = "https://jsonplaceholder.typicode.com/posts/1"

# 
response = requests.delete(url)

# 
print("Status Code:", response.status_code)

# Check response
if response.status_code == 200 or response.status_code == 204:
    print(" Post deleted (simulated) successfully.")
else:
    print("Failed to delete post. Response:")
    print(response.text)

#response
Status Code = 200
