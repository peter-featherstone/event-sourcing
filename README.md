# Event Sourcing

This is me playing around with Event Sourcing in Domain Driven Design as 
part of a hackday project and lightning talk for learning purposes. If there
are any misunderstanding then please raise up a PR or an Issue to help me 
learn!

I've tried to make the code as clean as possible but still beware of some
lurking dragons.

### Building the application
The first time you clone the application you will need to run a `make install`
to build the containers and run the migrations.

If this fails the first time, try and wait for the postgres container to fully
spin up and then try again as postgres is not always ready for the alembic 
migrate step to run.

### Running the application
To run the application type `make run` at the console and then navigate to 
http://127.0.0.1. 

### Running the tests
To run the tests type `make test` at the console.

### Running migrations
To run database migrations type `make migrate` at the console.

### Tech Stack
* Docker
* Python 3
* Flask
* Gunicorn
* Postgres
