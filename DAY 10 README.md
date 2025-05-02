#  Day 10 – GitHub API, OpenAI API & Python Practice

---

##  API Key Security Reminder

As advised, **API keys must never be shared or exposed**.  
Today, all authentication was handled using **Postman Environment Variables** (marked as `secret`) and securely passed in headers.

- My OpenWeatherMap key used earlier has been revoked.
- For GitHub and OpenAI APIs, I used secure tokens handled only in code or Postman environment.
- No API keys were pushed to GitHub.



##  APIs Practiced

### GitHub REST API

####  Methods Used:
- `GET`: Fetch repository details
- `POST`: Create an issue
- `PATCH`: Update issue (title/body)
- `PATCH (close)`: Close issue (used instead of DELETE)

####  Note:
GitHub **does not support true DELETE for issues**, so I used:
```json
{
  "state": "closed"
}

to simulate delete by closing the issue — as per API documentation.

All GitHub requests were tested via:

Python (requests) scripts

Postman using environment variables

2 OpenAI API
 Methods Used:
POST: Chat completion (prompt → response)

Simulated Update by modifying the prompt

Simulated Delete by clearing the message context

GET: Attempted quota check (401 error on project API key)


 Limitations Faced
 Billing Endpoint Access Denied (Session Key Required)

{
  "message": "Your request to GET /v1/dashboard/billing/credit_grants must be made with a session key (that is, it can only be made from the browser). You made it with the following key type: ."
}
 OpenAI Quota Exceeded (Free Tier Limit)

{
  "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.",
  "type": "insufficient_quota",
  "code": "insufficient_quota"
}
 Learning:
OpenAI API doesn’t support CRUD in the traditional sense — operations like update and delete are simulated by sending new prompts or clearing context.

 Python Fundamentals (Scaler Practice)
Today I also deepened my understanding of Python basics critical for API & LLM work:

 Functions
def, return values, default/keyword arguments

Lambda functions, *args, **kwargs

Scope: local vs global

 Dictionaries
Access with .get(), .keys(), .values()

Updating, deleting using .pop(), .update()

Nested dictionaries & JSON-style structures

Used for representing structured API responses

 Files Pushed
github_get_repo.py

github_post_issue.py

github_patch_issue.py

github_close_issue.py

openai_api_dcrud.py (multi-action script)

function_practice.ipynb (Colab)

dictionary_practice.ipynb (Colab)

 Troubleshooting & Fixes
Problem	Solution
401 Unauthorized	Fixed missing or misconfigured tokens in Postman
429 Quota Exceeded	Identified free tier usage limit and logged error
Postman URL errors	Used hardcoded values to debug then corrected env variables

 Tools Used
Python 3.13

requests library

Postman (collections, environments, variables)

Google Colab for practice notebooks

GitHub for daily log & README
