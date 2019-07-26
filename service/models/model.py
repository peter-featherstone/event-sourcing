class Model:

    def __init__(self, events=None):
        self.events = events or []
        for event in self.events:
            self._apply_event(event)

