from service.models import Model


class Customer(Model):

    def _apply_event(self, event):
        self.name = event.data['name']
