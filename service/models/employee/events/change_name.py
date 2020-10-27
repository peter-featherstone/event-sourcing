from service.models.event import Event


class ChangeName(Event):

    def apply(self, employee):
        employee.name = self.data['name']
