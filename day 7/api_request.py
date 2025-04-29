import requests
import json
print("Script is running!")

def simple_request_demo():
    """
    A simple demonstration of basic GET and POST requests
    """
    print("===== Simple API Request Demo =====")
    
    # GET request example
    print("\nMaking a GET request...")
    get_response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"Status code: {get_response.status_code}")
    print("Response body:")
    print(json.dumps(get_response.json(), indent=2))
    
    # POST request example
    print("\nMaking a POST request...")
    post_data = {
        'title': 'New Post',
        'body': 'This is the content of my new post',
        'userId': 1
    }
    post_response = requests.post(
        'https://jsonplaceholder.typicode.com/posts', 
        json=post_data
    )
    print(f"Status code: {post_response.status_code}")
    print("Response body:")
    print(json.dumps(post_response.json(), indent=2))

if __name__ == "__main__":
    simple_request_demo()


output 
#### Script is running!
===== Simple API Request Demo =====

Making a GET request...
Status code: 200
Response body:
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}

Making a POST request...
Status code: 201
Response body:
{
  "title": "New Post",
  "body": "This is the content of my new post",
  "userId": 1,
  "id": 101
}
