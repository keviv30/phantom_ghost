# Phantom Ghost Names

Welcome to Phantom Ghost names site repository. The Phantom Ghost names site allows you to select your own
phantom name, which would be listed on the overview page.

Your name will be displayed in the following format:

Josua (first name)  Bogle (ghost name) Pedersen (last name)

Please visit the website by clicking on the link below
http://ec2-3-135-183-255.us-east-2.compute.amazonaws.com/

# App Functions
- List all the Phantom names and the user's name if they are assigned to a ghost name
- Allow users to login using Google Authentication
- Allow users to create their Phantom name
- Allow users to change their Phantom name to a new Phantom name if it's available

Software used to build the project:
-   Django (web framework)
-   Python3
-   Bootstrap

# Installation

How to run the application locally:

 - Create Python3 virtualenv and install project dependencies and requirements from the requirements.txt file.
 - Please create a secrets.json file in the project folder next to manage.py and add the following before running the project locally.

        {
          "SECRET_KEY":"your_secret_key"
        }

-   Enter the following on the command-line to run the server.
        python manage.py runserver

-   Enter the following on the command-line to run the tests.
        python manage.py test blogs/tests/

# DevOps
-   The App is using AWS EC2 for hosting. Nginx for handing requests and Gunicorn to interact with Django Application.
