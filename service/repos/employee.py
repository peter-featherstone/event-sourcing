from .base import BaseRepository
from ..models import Employee


class EmployeeRepository(BaseRepository):

    _entity = Employee
