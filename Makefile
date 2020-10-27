install:
	docker-compose build
	docker-compose up postgres
	docker-compose run service sh -c 'alembic upgrade head'

run:
	docker-compose up --force-recreate

test:
	docker-compose run service sh -c 'pytest -vv --cov=./ tests'
