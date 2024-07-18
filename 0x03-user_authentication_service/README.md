# User Authentication Service

This project is a user authentication service implemented using Flask and SQLAlchemy. It covers the following functionalities:

- User registration and login
- Password hashing
- Session management
- Basic Flask API setup

## Learning Objectives

By the end of this project, you should be able to:

- Declare API routes in a Flask app
- Handle cookies in Flask
- Retrieve request form data
- Return various HTTP status codes
- Understand the basics of user authentication mechanisms

## Requirements

- Python 3.7
- Flask
- SQLAlchemy 1.3.x
- bcrypt
- Ubuntu 18.04 LTS

## Setup

Install the required packages:

```bash
pip3 install flask sqlalchemy bcrypt
```

## Usage

Run the Flask application:

```bash
python3 app.py
```

## Endpoints

- `GET /` : Welcome message
- `POST /users` : Register a new user
- `POST /sessions` : Login and create a session
- `DELETE /sessions` : Logout and destroy a session
- `GET /profile` : Get user profile

## Author

This project is maintained by [ABDURRAHMAN IDRIS](github.com/AbdurrahmanIdr).
