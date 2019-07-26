from service.models import Model
from .events import ChangeName
from .events import ChangeJob
from .events import ChangeSalary


class Customer(Model):

    def __init__(self, name=None, job=None, **kwargs):
        self.name = name
        self.job = job

        super().__init__(**kwargs)

    def change_name(self, name, user_id):
        self._add_event(ChangeName, name=name, user_id=user_id)

    def change_job(self, job, user_id):
        self._add_event(ChangeJob, job=job, user_id=user_id)

    def change_salary(self, salary, user_id):
        self._add_event(ChangeSalary, salary=salary, user_id=user_id)
