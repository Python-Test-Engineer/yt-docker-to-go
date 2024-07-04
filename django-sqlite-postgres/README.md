# Docker dev

[YT Video](https://www.youtube.com/watch?v=pwlt8BTYsOU&list=PLsszRSbzjyvklQ2LAjNEURKYAYglUgHsB&index=3)

## Venv

Only needed if running sql_postgres scripts as we need to connect to Postgres

## Using Postgres

Use python-postgres-pgadmin-admine to set up Postgres container...do this first beforesetting up Django

- [link](https://github.com/Python-Test-Engineer/yt-docker-to-go/tree/main/python-postgres-pgadmin-adminer)
- [video]([YouTube](https://youtu.be/mipRKPHwlBkI))

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




