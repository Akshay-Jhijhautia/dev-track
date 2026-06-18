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

**How to Run the Project**                                                
Clone the repository: git clone <your-github-repo-url>                                  
cd devtrack                            
Create and activate a virtual environment: python3 -m venv venv                                                          
source venv/bin/activate                                     
Install dependencies: pip install -r requirements.txt                                         
Run migrations: python manage.py migrate                                        
Start the server: python manage.py runserver                                   
The API will be available at: http://127.0.0.1:8000/                               

**API Endpoints**                                      

1. Reporter Endpoints:                                                   
POST	/api/reporters/	Create a new reporter                                           
GET	/api/reporters/	Get all reporters                                                      
GET	/api/reporters/?id=1	Get reporter by ID                                                   

2. Issue Endpoints:                                                  
POST	/api/issues/	Create a new issue                                               
GET	/api/issues/	Get all issues                                                    
GET	/api/issues/?id=1	Get issue by ID                                                             
GET	/api/issues/?status=open	Filter issues by status                                                   
