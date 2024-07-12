# Backend User Data

## Requirements

- Python 3.7
- All files interpreted/compiled on Ubuntu 18.04 LTS
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Code should follow the `pycodestyle` style (version 2.5).
- All files must be executable.
- Documentation for all modules, classes, and functions is required.

## Project Structure

- [0x00. Personal data](./0x00-personal_data/)
- [0x01. Basic Auth](./0x01-Basic_authentication/)

## Usage

1. Clone the repository:

   ```sh
   git clone https://github.com/AbdurrahmanIdr/alx-backend-user-data.git
   ```

2. Navigate to the project directory:

   ```sh
   cd alx-backend-user-data/<project name>
   ```

3. Install the required dependencies:

   ```sh
   pip3 install -r requirements.txt
   ```

4. Start the server:

   ```sh
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
   ```

5. Test the endpoints using `curl` or your preferred method:

   ```sh
   curl "http://0.0.0.0:5000/api/v1/status"
   ```

## Author

This project is maintained by [Abdurrahman Idris](https://github.com/AbdurrahmanIdr).

Feel free to reach out for any questions or contributions!
