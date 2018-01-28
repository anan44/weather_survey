# Crowd sourced weather service

### Deployed at https://weather-reaktor.herokuapp.com/

## TODO:
Make everything pretty


## Deployment guide (for Heroku):

1) Create new .env file on root folder
    * File needs to contain following:
    * SECRET_KEY="your-secret-key-goes-here"
    * DEBUG=True
2) Add desired URL (only domain!) to ALLOWED_HOSTS in settings.py
3) Heroku apps:create [desiredn app name]
4) Heroku config:push
    * You might have to install Heroku config plugin for this
    (heroku plugins:install heroku-config)
5) Commit made changes to git. Remember to keep .env out from git,
sharing SECRET_KEY can compromise  website security
    * git add .
    * git commit -m "Preperation for Heroku deployment"
6) Push to heroku
    * git push heroku master
7) Run database migration scripts in heroku
    * heroku run python manage.py migrate
    * heroku run python manage.py makemigrations
    * heroku run python manage.py migrate
8) Check everything is running correctly and turn of DEBUG mode
    * heroku config:set DEBUG=False

## Running locally
1) It is recommended to use virtual environment
	* Your python and package versions might vary from ones used on this project
2) Install required packages per requirements.txt
3) Create new .env file on root folder
    * File needs to contain following:
    * SECRET_KEY="your-secret-key-goes-here"
    * DEBUG=True
4) Run database migrations
	* python manage.py migrate
	* python manage.py makemigrations
	* python manage.py migrate
5) Run server
	* python manage.py runserver
