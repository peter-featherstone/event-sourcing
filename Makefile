install:
	docker-compose build

run:
	docker-compose up --force-recreate

test:
	docker-compose run service sh -c 'py.test -vv --cov=./ tests'
