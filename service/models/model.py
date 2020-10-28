"""Internal representation of a model built up from a list of events."""
from datetime import datetime
from typing import List
from uuid import UUID


class Model:
    """Definition of a base model for all other models to extend from."""

    def __init__(self, id_: UUID, events: List['Event'] = None) -> None:
        """Instantiates a model object with all required data.

        Loops through all events provided from the event store and applies them
        one by one in order to arrive at a final state representation of the
        model.

        Args:
            id_: A uuid4 identifier globally unique to all models.
            events: Collection of events associated to the model to apply.
        """
        self.id = id_
        self.events = events or []
        self.unsaved_events = []

        for event in self.events:
            self._apply_event(event)

    def clear_unsaved_events(self) -> None:
        """Clears any unsaved events on the model."""
        self.unsaved_events = []

    def _apply_event(self, event: 'Event') -> None:
        """Applies an individual event to the model.

        Args:
            event: The event class to use to apply changes with.
        """
        event.apply(self)

    def _add_event(self, event_cls: 'Event.__class__', **kwargs) -> None:
        """Adds an event to the unsaved events list.

        This method builds up a list of changes in memory yet to be committed
        to the event store on the model.

        Args:
            event_cls: The particular class definition of an Event to add.
            kwargs: key=value pairs for the changes that have occurred.
        """
        self.unsaved_events.append(
            event_cls(
                created=datetime.now(),
                model_id=self.id,
                model_type=self.__class__.__name__,
                event_type=event_cls.__name__,
                data=kwargs
            )
        )
