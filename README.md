## Session Authentication Sample Project

Most of the code from this project was adapted from the following source:
https://github.com/linkedweb/session_auth

## Installing Dependencies
- First, create a Python virtual environment by running `python -m venv .venv` from root
project directory. This ensures python dependencies are installed locally.
- From the root directory run `pip install -r requirements.txt` to install Django 
dependencies
- cd into the frontend directory and run `npm install` to install node modules

## Running this Program
- Open a terminal then run `python manage.py migrate` from the backend/ directory 
to create the sqlite database tables
- In the same terminal run `python manage.py runserver` to run the Django server
- Open another terminal then run `npm start` from the frontend/ directory

## Important Info
- You must create a .env.local file with HOST=127.0.0.1 in it. This ensures the React development server does not start using localhost, which prevents cookies from being saved.
- The CSRFToken.js file in the React components directory makes a call to the Django server to send back the CSRF cookie. This component should be included in any React component that will be sending a POST, PUT, or DELETE request. The purpose of this CSRFToken component is to ensure that the browser has a copy of the CSRF cookie saved, otherwise POST, PUT, and DELETE requests won't work. This token file, however, is not necessary once the user has already logged in since the sessionid cookie will provide authentication at that point.
- The checkAuthenticated function in App.js calls the Django server to check if a user is already logged in the browser. This function sets the isAuthenticated state variable, which, when true, allows the user to access "protected" areas of the app that only logged in users should see.

## Useful Django Commands


- Create superuser to access the admin site. Admin site can be accessed at localhost:8000/admin  
`python manage.py createsuperuser`
- Build the database used by the app:  
`python manage.py migrate`
- Run the Django server  
`python manage.py runserver`
- Make the SQL migration files, which is required any time a model is added or modified, and upon creating a brand new app. Shouldn't be needed for this repo.   
`python manage.py makemigrations polls`
- Create a brand new django project:  
`django-admin startproject projectnamehere`