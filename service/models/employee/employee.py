"""Internal pure python model representation of an employee."""
from service.models.model import Model
from .events import ChangeJob, ChangeName, ChangeSalary, CreateEmployee


class Employee(Model):
    """Definition of the employee model."""

    def __init__(
        self,
        name: str = None,
        job: str = None,
        salary: int = None,
        **kwargs
    ) -> None:
        """Instantiates an Employee object with all required data.

        Args:
            name: Initial name to set on the employee.
            job: Initial job title to set on the employee.
            salary: Initial salary to set on the employee.
            kwargs: See base definition of Model for extra args.
        """
        self.name = name
        self.job = job
        self.salary = salary

        super().__init__(**kwargs)

    def change_name(self, name: str) -> None:
        """Adds a new change name event to the employee.

        Args:
            name: The new name for the employee.
        """
        self.name = name

        self._add_event(ChangeName, name=name)

    def change_job(self, job: str) -> None:
        """Adds a new change job event to the employee.

        Args:
            job: The new title of the job for the employee.
        """
        self.job = job

        self._add_event(ChangeJob, job=job)

    def change_salary(self, salary: int) -> None:
        """Adds a new change salary event to the employee.

        Args:
            salary: The new salary for the employee.
        """
        self.salary = salary

        self._add_event(ChangeSalary, salary=salary)

    def create(self, name: str, job: str, salary: int) -> None:
        """Adds a new create event for an employee.

        Args:
            name: Thew name for the employee.
            job: The new title of the job for the employee.
            salary: The new salary for the employee.
        """
        self.name = name
        self.job = job
        self.salary = salary

        self._add_event(CreateEmployee, name=name, job=job, salary=salary)
