from service.models.event import Event


class ChangeJob(Event):

    def apply(self, customer):
        customer.job = self.data['job']
