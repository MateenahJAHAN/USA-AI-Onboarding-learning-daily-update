6th Day Learning
### 
Twitter DOM & API Analysis
API Documentation:

Examined Twitter API v2 structure for Likes/Retweets endpoints
Compared v1.1 to v2 migration paths and authentication requirements
Studied pagination implementation (100 users per batch)

DevTools Investigation:

Used Chrome Network tab to monitor API calls during tweet interactions
Identified key JavaScript modules handling engagement features
Observed request sizes (~2.1 KB) and resource patterns

DOM Structure:

Located tweet container elements with nested engagement components
Analyzed event listeners connecting UI interactions to API requests
Traced the path of data flow from user clicks to DOM updates

### Quickstart Flask: Tried building APIs using Flask, tested on Postman and a web browser.

Flask API Development:

Created loan approval API endpoints in flask_loan_api_builder.py
Implemented GET/POST routes for loan application processing
Tested API responses via Postman showing JSON response structure

Virtual Environment: Created a virtual environment to manage projects better.
with this code  cd flask_loan_app
python3 -m venv venv and activated by typing this source venv/bin/activate
pip install flask
python3 app.py

### Challenges:

Faced errors when running multiple requests in the terminal, getting only one response.
# Create a Flask application object
app = Flask(__name__)

# Basic homepage route
@app.route('/')
def hello_world():
    return "<h1>Hello there!!</h1>"

# Ping route that returns a message
@app.route('/ping')
def ping():
    return {"message": "Why are you pinging me?"}

# Loan application routes
@app.route('/loan-app')
def home():
    return "<h1>Loan App</h1>"

@app.route('/predict')
def predict():
    return "<h1>Loan App</h1><p>Prediction endpoint</p>"

# Run the application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
here i was expecting that i will get 1 http for this Basic homepage route,2nd for this Ping route that returns a message,third for this Loan application routes but i couldnot , i will explore and will fix it. 
Spent time troubleshooting and experimenting with different platforms for better practice.

### Assistance:

ChatGPT and Claude helped identify errors in the code and clarified where I was going wrong.
