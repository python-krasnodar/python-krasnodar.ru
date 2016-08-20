# python-krasnodar.ru

Our website.

## Install 

You can install this project in different way.

### virtualenv (recommended for local)

Type this commands

```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

After this you must configure your `src/pykrd/localsettings.py` file, 
apply migrations, collect static files and run local development server.

```sh
cd src
cp pykrd/localsettings.py.dist pykrd/localsettings.py
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

Your local instance of application will accessible in http://localhost:8000.

### Docker (recommended for production)

Copy .env.dist and edit if need. Run this docker-compose command for start local instance.

```sh
docker-compose up -d
```

In .env you must set NGINX_PORT env var and open your instance of application in http://localhost:${NGINX_PORT}.