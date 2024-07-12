# Basic Authentication API

## Description

This project demonstrates the implementation of a Basic Authentication system on a simple API using Flask. The authentication process involves encoding and decoding Base64 strings, handling HTTP errors, and securing API endpoints.

## Learning Objectives

By the end of this project, you should be able to:

- Understand what authentication means
- Explain what Base64 is and how to encode/decode strings in Base64
- Describe the Basic authentication process
- Send the Authorization header in HTTP requests

## Setup

### Prerequisites

- Python ~=3.7
- Flask

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/AbdurrahmanIdr/alx-backend-user-data.git
   cd alx-backend-user-data/0x01-Basic_authentication
   ```

2. Install the required packages:

   ```sh
   pip3 install -r requirements.txt
   ```

### Running the Server

1. Start the server:

   ```sh
   API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
   ```

2. Use the API:

   ```sh
   curl "http://0.0.0.0:5000/api/v1/status" -vvv
   ```

## API Endpoints

- `/api/v1/status` - Check API status
- `/api/v1/unauthorized` - Trigger a 401 Unauthorized error
- `/api/v1/forbidden` - Trigger a 403 Forbidden error

## Authentication

### Basic Authentication

- The `Authorization` header must be included in the request for authenticated endpoints.
- The header should contain the word "Basic" followed by a space and a Base64 encoded string of `username:password`.

### Error Handling

- `401 Unauthorized` - When the user is not authorized
- `403 Forbidden` - When the user is authenticated but not allowed to access the resource

## Project Structure

- `api/v1/app.py` - Main application file
- `api/v1/views/index.py` - API routes
- `api/v1/auth/` - Authentication classes and methods

## Running Tests

Run the provided test scripts to verify functionality:

```sh
python3 main_0.py
python3 main_1.py
python3 main_2.py
python3 main_3.py
python3 main_4.py
python3 main_5.py
```

## Authors

- [Abdurrahman Idris](https://github.com/AbdurrahmanIdr)
