from service.models.event import Event


class ChangeJob(Event):

    def apply(self, employee):
        employee.job = self.data['job']
