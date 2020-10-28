"""Internal pure python model representation of a change job event."""
from service.models.event import Event


class ChangeJob(Event):
    """Definition of a change job event."""

    def apply(self, employee: 'Employee') -> None:
        """Applies the change job mutation event on an employee.

        Args:
            employee: The employee to change the job title for.
        """
        employee.job = self.data['job']
