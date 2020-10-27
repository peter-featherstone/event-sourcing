from service.models.event import Event


class ChangeSalary(Event):

    def apply(self, employee):
        employee.salary = int(self.data['salary'])
