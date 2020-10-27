from .database import db
from .employee import EmployeeRepository


def get_employee_repo():
    return EmployeeRepository(db=db.session)
