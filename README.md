# Crowd sourced weather service

### Deployed at https://weather-reaktor.herokuapp.com/

## TODO:
* Make everything pretty
* Plug in with some weather API
* Add proper statistic analysis
* Add data visualization


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
    * pip install -r requirements-dev.txt
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

## Requirements
* Requirements are specifiied in following files:
    * runtime.txt
    * requirements-dev.txt
    * requirements.txt
* Running project with other configurations might be possible, but not
  recommended due to possible compatibility issues.

#### Summary of required versions and packages
##### Development and Production
* Python 3.6.4
* beautifulsoup4==4.6.0
* dj-database-url==0.4.2
* dj-static==0.0.6
* Django==2.0.1
* django-bootstrap3==9.1.0
* django-braces==1.12.0
* django-webtest==1.9.2
* python-decouple==3.1
* pytz==2017.3
* six==1.11.0
* static3==0.7.0
* waitress==1.1.0
* WebOb==1.7.4
* WebTest==2.0.29

##### Production only
* gunicorn
* psycopg2
