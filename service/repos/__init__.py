from .customer import CustomerRepository
from .database import db


def get_customer_repo():
    return CustomerRepository(db=db.session)
