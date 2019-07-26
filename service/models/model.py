import random
from datetime import datetime


class Model:

    def __init__(self, _id, events=None):
        self._id = _id
        self.events = events or []
        self.unsaved_events = []

        for event in self.events:
            self._apply_event(event)

    def _apply_event(self, event):
        event.apply(self)

    def _add_event(self, event_cls, user_id, **kwargs):
        event = event_cls(
            created=datetime.now(),
            aggregate_id=self._id,
            aggregate_type=self.__class__.__name__,
            event_type=event_cls.__name__,
            user_id=user_id,
            data=kwargs
        )

        self.unsaved_events.append(event)
