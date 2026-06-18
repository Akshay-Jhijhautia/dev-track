**DevTrack**
DevTrack is a minimal Django backend API for tracking engineering issues. Engineers can create reporters, file issues, assign priorities, and track issue status. The project uses object-oriented Python classes and stores data in JSON files instead of a database.

**Features**
Create a reporter
Get all reporters
Get reporter by ID
Create an issue
Get all issues
Get issue by ID
Filter issues by status
Validate request data using OOP class methods
Use inheritance for priority-specific issue descriptions

**Tech Stack**
Python
Django
JSON file storage
Postman for API testing

**Project Structure**
devtrack/
├── manage.py
├── reporters.json
├── issues.json
├── devtrack/
│   ├── settings.py
│   └── urls.py
├── issues/
│   ├── models.py
│   ├── views.py
│   └── urls.py

**How to Run the Project**
Clone the repository:

git clone <your-github-repo-url>
cd devtrack
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Run migrations:

python manage.py migrate
Start the server:

python manage.py runserver
The API will be available at:

http://127.0.0.1:8000/

**API Endpoints**
Reporter Endpoints:
POST	/api/reporters/	Create a new reporter
GET	/api/reporters/	Get all reporters
GET	/api/reporters/?id=1	Get reporter by ID

Issue Endpoints:
Method	Endpoint	Description
POST	/api/issues/	Create a new issue
GET	/api/issues/	Get all issues
GET	/api/issues/?id=1	Get issue by ID
GET	/api/issues/?status=open	Filter issues by status

**Sample Create Reporter Request**
{
  "id": 1,
  "name": "Akshay Jhijhautia",
  "email": "akshay@example.com",
  "team": "backend"
}

**Sample Create Issue Request**
{
  "id": 1,
  "title": "Login button not working on mobile",
  "description": "Users on iOS 17 cannot tap the login button",
  "status": "open",
  "priority": "critical",
  "reporter_id": 1
}

**Sample Success Response**
{
  "id": 1,
  "title": "Login button not working on mobile",
  "description": "Users on iOS 17 cannot tap the login button",
  "status": "open",
  "priority": "critical",
  "reporter_id": 1,
  "created_at": "2026-06-18 12:10:20.123456",
  "message": "[URGENT] Login button not working on mobile — needs immediate attention"
}

**Sample Failure Response**
{
  "error": "Title cannot be empty"
}

**Design Decision**
I kept the OOP entity classes inside issues/models.py and kept API logic inside issues/views.py. This separates business rules from request-handling code. The Reporter and Issue classes are responsible for validation and dictionary conversion, while the views are responsible for reading requests, writing JSON files, and returning HTTP responses.

I also created CriticalIssue and LowPriorityIssue as subclasses of Issue to demonstrate inheritance and method overriding. Each subclass overrides the describe() method to return a different message based on priority.
