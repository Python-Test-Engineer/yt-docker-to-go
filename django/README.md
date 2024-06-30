# Docker dev

[YT Video]()
## Set up

Create venv and install...

docker compose up -d --build

http://127.0.0.1:8000/ 

`docker exec -it django_container bash` to enter docker container

Then you can do usual Django stuff...

root@c46509fc6029:/django# python manage.py createsuperuser

## Development

Add code as usual in the app.
