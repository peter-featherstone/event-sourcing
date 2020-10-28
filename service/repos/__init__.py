"""Collection of repositories and repository factories in the application."""
from .database import db as default_db
from .employee import EmployeeRepository


def get_employee_repo(db=None) -> EmployeeRepository:
    """Instantiates an employee repository using application defaults.

    Args:
        db: A custom db session if wanting to override the default.

    Returns:
        An instantiated EmployeeRepository instance.
    """
    return EmployeeRepository(db=db or default_db.session)
