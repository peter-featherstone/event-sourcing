install:
	docker-compose build
	docker-compose run alembic upgrade head

run:
	docker-compose up service

test:
	docker-compose run pytest -vv --cov=./ --cov-report=html tests

migrate:
	docker-compose run alembic upgrade head
