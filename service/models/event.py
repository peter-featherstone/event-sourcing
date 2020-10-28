"""Internal pure python model representation of an internal event."""
from datetime import datetime
from uuid import UUID


class Event:
    """Definition of a base event for all other events to extend from."""

    def __init__(
        self,
        created: datetime,
        data: dict,
        event_type: str,
        aggregate_id: UUID,
        aggregate_type: str
    ) -> None:
        """Instantiates an Event object with all required data.

        Args:
            created: The time that the event was created.
            data: Any data contained in the event payload.
            event_type: The internal name of the event.
            aggregate_id: A uuid4 identifier globally unique to all aggregates.
            aggregate_type: The internal model of the aggregate to be mutates.
        """
        self.created = created
        self.data = data
        self.event_type = event_type
        self.aggregate_id = aggregate_id
        self.aggregate_type = aggregate_type

    def apply(self, model: 'Model') -> None:
        """Applies the event to a given model instance.

        All events extending from this base must implement this method to
        determine how to apply the changes to the given model.

        Args:
            model: The model to apply the changes to.
        """
        raise NotImplementedError('All events must implement an apply method.')
