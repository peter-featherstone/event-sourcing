"""Internal pure python model representation of a create employee event."""
from service.models.event import Event


class CreateEmployee(Event):
    """Definition of a create employee event."""

    def apply(self, employee: 'Employee') -> None:
        """Applies the create employee mutation event on an employee.

        Args:
            employee: The employee to change the data for.
        """
        employee.name = self.data['name']
        employee.job = self.data['job']
        employee.salary = int(self.data['salary'])
