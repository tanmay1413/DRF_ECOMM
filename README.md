# DRF ECOMM - Django Rest Framework E-Commerce
This is a simple e-commerce backend built using Django and Django Rest Framework (DRF). It includes basic functionality such as user authentication, product management (create, list), and API documentation via DRF Spectacular.


# Project Setup
Clone the Repository
To get started, clone the repository to your local machine:

bash
git clone https://github.com/tanmay1413/DRF_ECOMM
cd ecom

# Install Dependencies
You will need to install the required Python dependencies. It is highly recommended to use a virtual environment for managing dependencies.

# Create and activate a virtual environment:

For Windows:
venv\Scripts\activate

# Install the dependencies:
pip install -r requirements.txt

This will install all the required packages, including Django, DRF, and DRF Spectacular.

# Run the Server
Once the dependencies are installed, you can run the Django development server:


python manage.py runserver
The server will run at http://127.0.0.1:8000.

# API Documentation
This project uses DRF Spectacular to automatically generate OpenAPI documentation for the REST API.

# DRF Spectacular Documentation
To access the full API documentation, visit the following URL in your browser:

Copy code
http://127.0.0.1:8000/api/schema/docs/
Here, you will find an interactive API explorer that allows you to test various API endpoints directly from the documentation.

# Authentication
Token Authentication
This project uses Token Authentication via Django Rest Framework (DRF).

# Get Access Token for Existing User:
Under the API section in the documentation, navigate to the token section to retrieve the access token for an existing user.

# Register New User:
If you are a new user, you can register an account using the user registration endpoint. The API will automatically create the user and generate an authentication token.

# Using the Token
For any subsequent requests to protected endpoints (that require authentication), include the token in the Authorization header:


# Authorization: Bearer <your-access-token>
Available Endpoints
1. Register User
URL: /api/accounts/
Method: POST
Description: Registers a new user and returns an authentication token.
Request body:
json
Copy code
{
  "username": "your_username",
  "password": "your_password",
  "email": "your_email@example.com"
}
Response:
json
Copy code
{
  "token": "your-token-key"
}
2. Get List of Products
URL: /api/products/

Method: GET

Description: Retrieves a list of all products (authentication required).

Headers:
Authorization: Bearer <your-access-token>
Response:

3. Create a Product
URL: /api/products/
Method: POST
Description: Creates a new product (authentication required).


### FOR ALL ENDPONTS PLEASE VISIT DOCUMENTATION