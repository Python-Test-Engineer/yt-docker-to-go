# Django + Celery

## Source

https://testdriven.io/blog/django-and-celery/

## Changes

Updated to current:

- docker-compose exec web pip freeze > req_21JUN2024.txt

## Base run

- docker-compose up -d --build
- docker-compose exec web python -m pytest -vs SANITY CHECK
- http://localhost:1337

## Flower dashboard



- docker-compose up -d --build
- docker-compose up -d --build --scale celery=3
- http://localhost:1337
- http://localhost:5555/tasks
- docker-compose exec web python -m pytest -vs

## Tests

- docker-compose exec web python -m pytest -k "test_task and not test_long_tasks"
- docker-compose exec web python -m pytest -k "test_mock_task" -vs
- docker-compose exec web python -m pytest  -vs