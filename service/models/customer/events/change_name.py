from service.models.event import Event


class ChangeName(Event):

    def apply(self, customer):
        customer.name = self.data['name']
