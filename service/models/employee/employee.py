from ..model import Model
from .events import ChangeJob
from .events import ChangeName
from .events import ChangeSalary


class Employee(Model):

    def __init__(self, name=None, job=None, **kwargs):
        self.name = name
        self.job = job

        super().__init__(**kwargs)

    def change_name(self, name):
        self._add_event(ChangeName, name=name)

    def change_job(self, job):
        self._add_event(ChangeJob, job=job)

    def change_salary(self, salary):
        self._add_event(ChangeSalary, salary=salary)
