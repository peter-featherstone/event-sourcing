from .database import db
from .customer import CustomerRepository


def get_customer_repo():
    return CustomerRepository(db=db.session)
