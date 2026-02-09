# Day 11 – Onboarding Progress Update

> **Focus**: FastAPI CRUD, Postman Testing, JavaScript Scripts, Python Practice, and API Testing (Valentino's Coffee)

## Assignment Reference

I started by watching the video shared in the assignment link from the freeCodeCamp course on **Postman API Test Automation for Beginners**.

I also explored and practiced using the workspace **Valentino's Coffee**, where I learned about:

### What I Practiced

- Manual API testing
- Forking an API project
- Writing tests
- Running API calls using mock servers (when no real API is present)
- Using Postman variables to store secrets
- Writing scripts in Postman
- Using the Postman console for debugging scripts
- Writing an API test
- JavaScript basics to writing Postman scripts

## FastAPI Development Progress

### FastAPI Project Setup
- Set up a new FastAPI project using VS Code
- Ran the FastAPI server with `uvicorn main:app --reload`
- Confirmed it was running successfully on [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Path Operations Implemented
Created and tested routes:
- `@app.get("/")`
- `@app.post("/items/")`
- `@app.put("/items/")`
- `@app.delete("/items/")`

### Pydantic Schema Validation
- Implemented request/response models using Pydantic
- Validated incoming request body in POST and PUT requests

### CRUD Operations Done
- Implemented and tested full Create, Read, Update, and Delete functionality
- Used the environment and collection created earlier in Postman to send test requests
- Confirmed working with 200 OK responses for all endpoints

## Postman Setup

### Environment Configuration
- Created a collection and environment in Postman
- Used `{{base_url}}` as variable and set to [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Tested each CRUD endpoint successfully

## Postman Tests and Scripting

### Topics Covered
- Writing test scripts using `pm.test()`
- Accessing response data with `pm.response.json()`
- Using `console.log()` to debug and print values
- Understanding the Postman Console and using it for error checking


### This was the java Test Script that i learn first then pasted and checked 
```javascript
let data = pm.response.json();
console.log("Post Title:", data.title);

pm.test("Title is a string", function () {
    pm.expect(data.title).to.be.a("string");
});
```
### JSON Placeholder Practice

Used https://jsonplaceholder.typicode.com/posts/1 for practicing GET requests
Faced a 404 error initially due to a mistyped URL. Fixed it by:

Changing method to GET
Correcting endpoint spelling to /posts/1
Verifying in browser before testing in Postman
##  Python Practice

- Watched Scaler Academy's Python video on Tuples and Sets
- Practiced approximately 40 questions in Google Colab on tuple and set-related problems
- Will upload the notebook in the Day 11 folder

##  Challenges Faced

###  Issue 1: Cannot read properties of undefined error
- **Cause**: Trying to access `data.item.name` in a response that didn't contain item
- **Fix**: Used `console.log(data)` to check actual structure and updated script accordingly using correct access paths like `data.title`

###  Issue 2: 404 Error on JSONPlaceholder
- **Cause**: Mistyped endpoint URL or incorrect method (POST instead of GET)
- **Fix**: Corrected URL to `/posts/1` and used GET method

##  What I Learned Today

| Topic | Skill Learned |
|-------|---------------|
| FastAPI | Full CRUD setup with validation |
| Postman | Manual testing, environments, variables |
| JavaScript | Variables, functions, methods, callbacks |
| JSON | Format, parsing, reading response |
| Debugging | Console understanding and error handling |
| Python | Tuples and Sets (Scaler + Practice questions) |
| API Testing | Concepts from Valentino's Coffee workspace |

##  Files To Be Uploaded in Day 11
- `main.py` for FastAPI CRUD
- Python Colab notebook (Tuples and Sets practice)
