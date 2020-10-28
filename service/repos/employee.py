"""Collection of employee repository code."""
from service.models.employee.employee import Employee
from .base import BaseRepository


class EmployeeRepository(BaseRepository):
    """Definition of an employee repository for querying employees."""

    _entity = Employee
