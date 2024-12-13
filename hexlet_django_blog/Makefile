install:
	poetry install

lint:
	poetry run flake8 hexlet_django_blog

test:
	poetry run pytest

check:
	ruff check --fix --select I

start:
	python manage.py runserver