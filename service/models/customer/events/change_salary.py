from service.models.event import Event


class ChangeSalary(Event):

    def apply(self, customer):
        customer.salary = int(self.data['salary'])
