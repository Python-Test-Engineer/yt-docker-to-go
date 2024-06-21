# Django + Celery


## Source

https://testdriven.io/blog/django-and-celery/

## Changes

Updated to current:

- docker-compose exec web pip freeze > req_21JUN2024.txt

- docker-compose up -d --build
- http://localhost:1337
- docker-compose exec web python -m pytest -vs


http://localhost:5555/tasks

docker-compose up -d --build --scale celery=3

docker-compose exec web python -m pytest -k "test_task and not test_home"

docker-compose exec web python -m pytest -k "test_mock_task" -vs