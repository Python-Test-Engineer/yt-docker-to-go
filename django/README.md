# Docker dev

[YT Video]()

## Venv

Only needed if running sql_postgres scripts as we need to connect to Postgres

## Using Postgres

Use yt-post... to set up Postgres container...do this first before Django
[link](https://github.com/Python-Test-Engineer/yt-docker-to-go/tree/main/python-postgres-pgadmin-adminer)

copy contents of settings_postgres.py to settings.py (or combine and comment/uncomment as needed).
## Set up

Create venv and install...

docker compose up -d --build

http://127.0.0.1:8000/ 

`docker exec -it django_container bash` to enter docker container

Then you can do usual Django stuff...

root@c46509fc6029:/django# python manage.py createsuperuser

## Development

Add code as usual in the app.




