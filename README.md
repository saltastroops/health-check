# WEB MANAGER Health Check
A script that check if the Web Manager containers are running. 
If any of the two are down the script will email SALT Team. 

# Prerequisites
Python 3.8 must be installed for running the service.

# Environment variables
The following environment variables need to be defined, preferably in the .env file.

| Variable name              | Description                                    | Example               |
|----------------------------|------------------------------------------------|-----------------------|
| WEB_MANAGER_CONTAINER_NAME | Name of the container given to the WEB Manager | web-manager-container |
| SALT_API_CONTAINER_NAME    | Name of the container given to the SALT API    | salt-api-container    |
| SALT_API_CONTAINER_NAME    | Name of the container given to the SALT API    | salt-api-container    |
| TO_EMAIL                   | SALT SOFTWARE team email                       | example@example.com   |
| FROM_EMAIL                 | Email dedicated to send emails                 | example@example.com   |
| FROM_EMAIL                 | Email dedicated to send emails                 | example@example.com   |
| SMTP_SERVER                | An SMTP server for sending emails              | smtp.example.com      |
| SMTP_PORT                  | An SMTP server port for sending emails         | 123                   |

# Running the script.

Make sure that docker is installed to the python interpreter you are using.
If not you can install using poetry or pip. 

Poetry
```bash
poetry install
```
Pip
```bash
pip install docker
```

### To run the script
```bash
python main.py
```

or 
```bash
poetry run main.py
```