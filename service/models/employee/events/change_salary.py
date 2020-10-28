"""Internal pure python model representation of aa change salary event."""
from service.models.event import Event


class ChangeSalary(Event):
    """Definition of a change salary event."""

    def apply(self, employee: 'Employee') -> None:
        """Applies the change salary mutation event on an employee.

        Args:
            employee: The employee to change the salary for.
        """
        employee.salary = int(self.data['salary'])
