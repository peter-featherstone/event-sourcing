"""Internal pure python model representation of a change name event."""
from service.models.event import Event


class ChangeName(Event):
    """Definition of a change name event."""

    def apply(self, employee: 'Employee') -> None:
        """Applies the change name mutation event on an employee.

        Args:
            employee: The employee to change the name for.
        """
        employee.name = self.data['name']
