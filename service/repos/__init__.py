from .employee import EmployeeRepository
from .database import db


def get_employee_repo():
    return EmployeeRepository(db=db.session)
