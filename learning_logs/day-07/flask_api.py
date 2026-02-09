from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data - in-memory database
posts = [
    {
        "id": 1,
        "title": "First Post",
        "body": "This is the first post content",
        "userId": 1
    },
    {
        "id": 2,
        "title": "Second Post",
        "body": "This is the second post content",
        "userId": 1
    }
]

# GET all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# GET a single post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

# POST a new post
@app.route('/posts', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json:
        return jsonify({"error": "Title is required"}), 400
    
    # Get the highest ID and add 1
    new_id = max(post['id'] for post in posts) + 1
    
    new_post = {
        'id': new_id,
        'title': request.json['title'],
        'body': request.json.get('body', ""),
        'userId': request.json.get('userId', 1)
    }
    
    posts.append(new_post)
    return jsonify(new_post), 201

# PUT (update) a post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    
    post['title'] = request.json.get('title', post['title'])
    post['body'] = request.json.get('body', post['body'])
    post['userId'] = request.json.get('userId', post['userId'])
    
    return jsonify(post)

# DELETE a post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    original_length = len(posts)
    posts = [post for post in posts if post['id'] != post_id]
    
    if len(posts) < original_length:
        return jsonify({"message": f"Post {post_id} has been deleted"})
    return jsonify({"error": "Post not found"}), 404

if __name__ == '__main__':
    print("Starting Flask API server...")
    print("API available at http://127.0.0.1:5000/")
    print("Available endpoints:")
    print("  GET    /posts")
    print("  GET    /posts/<id>")
    print("  POST   /posts")
    print("  PUT    /posts/<id>")
    print("  DELETE /posts/<id>")
    app.run(debug=True)


#### ON Terminal 

mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % pip3 install flask
Requirement already satisfied: flask in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (3.1.0)
Requirement already satisfied: Werkzeug>=3.1 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from flask) (3.1.3)
Requirement already satisfied: Jinja2>=3.1.2 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from flask) (3.1.6)
Requirement already satisfied: itsdangerous>=2.2 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from flask) (2.2.0)
Requirement already satisfied: click>=8.1.3 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from flask) (8.1.8)
Requirement already satisfied: blinker>=1.9 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from flask) (1.9.0)
Requirement already satisfied: MarkupSafe>=2.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from Jinja2>=3.1.2->flask) (3.0.2)

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: pip3 install --upgrade pip
mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % python3 flask_api.py
Traceback (most recent call last):
  File "/Users/mateenahjahan/Documents/api_assignment  /flask_api.py", line 1, in <module>
    flask_api.py
    ^^^^^^^^^
NameError: name 'flask_api' is not defined
mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % python3 flask_api.py
Traceback (most recent call last):
  File "/Users/mateenahjahan/Documents/api_assignment  /flask_api.py", line 1, in <module>
    flask_api.py
    ^^^^^^^^^
NameError: name 'flask_api' is not defined
mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % python3 flask_api.py
Traceback (most recent call last):
  File "/Users/mateenahjahan/Documents/api_assignment  /flask_api.py", line 1, in <module>
    flask_api.py
    ^^^^^^^^^
NameError: name 'flask_api' is not defined
mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % python3 app.py
/Library/Frameworks/Python.framework/Versions/3.13/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/mateenahjahan/Documents/api_assignment  /app.py': [Errno 2] No such file or directory
mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % pwd
/Users/mateenahjahan/Documents/api_assignment  
mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % touch app.py
mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % python3 app.py
mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % ls -la
total 32
drwxr-xr-x@ 10 mateenahjahan  staff   320 Apr 29 12:42 .
drwx------+ 22 mateenahjahan  staff   704 Apr 29 11:28 ..
-rw-r--r--@  1 mateenahjahan  staff     0 Apr 29 11:59 .env.template
-rw-r--r--@  1 mateenahjahan  staff   133 Apr 29 12:41 api_requests.md
-rw-r--r--@  1 mateenahjahan  staff  1000 Apr 29 12:15 api_requests.py
-rw-r--r--@  1 mateenahjahan  staff     0 Apr 29 11:54 api-
-rw-r--r--@  1 mateenahjahan  staff     0 Apr 29 12:42 app.py
-rw-r--r--@  1 mateenahjahan  staff  2478 Apr 29 12:41 flask_api.py
-rw-r--r--@  1 mateenahjahan  staff     0 Apr 29 11:58 openai_api.py
-rw-r--r--@  1 mateenahjahan  staff  1234 Apr 29 12:41 README.md
mateenahjahan@Mateenahs-MacBook-Pro api_assignment   % python3 flask_api.py
Starting Flask API server...
API available at http://127.0.0.1:5000/
Available endpoints:
  GET    /posts
  GET    /posts/<id>
  POST   /posts
  PUT    /posts/<id>
  DELETE /posts/<id>
 * Serving Flask app 'flask_api'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
Starting Flask API server...
API available at http://127.0.0.1:5000/
Available endpoints:
  GET    /posts
  GET    /posts/<id>
  POST   /posts
  PUT    /posts/<id>
  DELETE /posts/<id>
 * Debugger is active!
 * Debugger PIN: 135-509-750
127.0.0.1 - - [29/Apr/2025 12:56:41] "POST /posts HTTP/1.1" 415 -
127.0.0.1 - - [29/Apr/2025 12:57:31] "POST /posts/1 HTTP/1.1" 405 -
127.0.0.1 - - [29/Apr/2025 12:58:58] "POST /posts/1 HTTP/1.1" 405 -
127.0.0.1 - - [29/Apr/2025 12:59:02] "POST /posts/1 HTTP/1.1" 405 -
127.0.0.1 - - [29/Apr/2025 12:59:18] "POST /posts/1 HTTP/1.1" 405 -
127.0.0.1 - - [29/Apr/2025 12:59:41] "POST /posts HTTP/1.1" 201 -
127.0.0.1 - - [29/Apr/2025 13:00:37] "GET /posts/1 HTTP/1.1" 200 -
127.0.0.1 - - [29/Apr/2025 13:00:58] "GET /posts/1 HTTP/1.1" 200 -
127.0.0.1 - - [29/Apr/2025 13:01:20] "DELETE /posts/1 HTTP/1.1" 200 -
127.0.0.1 - - [29/Apr/2025 13:01:36] "PUT /posts/1 HTTP/1.1" 404 -
127.0.0.1 - - [29/Apr/2025 13:01:44] "GET /posts/1 HTTP/1.1" 404 -
127.0.0.1 - - [29/Apr/2025 13:02:03] "PUT /posts/1 HTTP/1.1" 404 -
127.0.0.1 - - [29/Apr/2025 13:03:40] "PUT /posts/1 HTTP/1.1" 404 -
127.0.0.1 - - [29/Apr/2025 13:03:42] "PUT /posts/1 HTTP/1.1" 404 -
127.0.0.1 - - [29/Apr/2025 13:04:13] "PUT /posts/1 HTTP/1.1" 404 -
127.0.0.1 - - [29/Apr/2025 13:05:17] "PUT /posts HTTP/1.1" 405 -
127.0.0.1 - - [29/Apr/2025 13:06:56] "GET /posts HTTP/1.1" 200 -
127.0.0.1 - - [29/Apr/2025 13:07:04] "POST /posts HTTP/1.1" 201 -
127.0.0.1 - - [29/Apr/2025 13:07:09] "DELETE /posts HTTP/1.1" 405 -
127.0.0.1 - - [29/Apr/2025 13:07:15] "PUT /posts HTTP/1.1" 405 -


  #### https http://127.0.0.1:5000
