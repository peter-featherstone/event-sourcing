"""Collection of base repository code."""
import importlib
from collections import defaultdict
from typing import List, Optional
from uuid import UUID

from service.models.event import Event
from service.models.model import Model
from service.models.schema.event import EventSchema


class ModelList:
    """Definition of a ModelList for representing data from event store."""

    def __init__(self, models: List[Model], events: List[Event]) -> None:
        """Instantiates the model list with all models and events.

        Provides the instantiated models themselves but also a list of all
        events in order across all models.

        Args:
            models: A list of all instantiated model with events applied.
            events: A list of all events in order across all models.
        """
        self.models = models
        self.events = events


class BaseRepository:
    """Definition of a base repository to be extended for specific models.

    _model needs to be overwritten in each extending class with a reference
    to the specific model it wants to query. One repository per model.
    """

    _model: Model.__class__ = None

    def __init__(self, db) -> None:
        """Initialise the repository with a live db session.

        Args:
            db: An instantiated db session ready for use.
        """
        self._db = db

    def get(self, id_: UUID) -> Optional[Model]:
        """Queries for a particular model by it's unique id.

        Handles the querying of all events for a specific model and applying
        them before returning the upto date model.

        Args:
            id_: The globally unique identifier for the model.

        Returns:
            An instantiated model with all it's events applied.
        """
        events = [
            self._translate_event(event) for event in self._query(
                filters=[
                    EventSchema.model_id == id_,
                    EventSchema.model_type == self._model.__name__
                ]
            ).all()
        ]

        return self._model(id_=id_, events=events) if events else None

    def all(self) -> ModelList:
        """Queries for all models of a particular type in the system.

        Handles the querying of all events for the models and applying
        them before returning the upto date models.

        Returns:
            An list of instantiated models with all their events applied.
        """
        events = self._query(
            filters=[EventSchema.model_type == self._model.__name__]
        ).all()

        model_events = defaultdict(list)
        for event in events:
            model_events[event.model_id].append(
                self._translate_event(event)
            )

        return ModelList(
            models=[
                self._model(id_=model_id, events=events)
                for model_id, events in model_events.items()
            ],
            events=[self._translate_event(event) for event in events]
        )

    def save(self, model: Model) -> None:
        """Saves an updated model back to the event store.

        We take all currently unsaved events on the model, build them into
        event schema objects ready to be saved to our event store and then
        clear the unsaved list so we don't accidentally commit changes twice.

        Args:
            model: The model who's events need saving.
        """
        for model_event in model.unsaved_events:
            self._db.add(
                EventSchema(
                    created=model_event.created,
                    model_id=model_event.model_id,
                    model_type=model_event.model_type,
                    event_type=model_event.event_type,
                    data=model_event.data
                )
            )

        self._db.commit()

        model.clear_unsaved_events()

    def _query(self, filters: list = None):
        """Builds a database query and applies any custom filters.

        Because we are using event sourcing we must ensure all queries are
        always ordered by created time and therefore all queries must come
        through this method.

        Args:
            filters: A list of filters to apply to the final query.
        """
        query = self._db.query(EventSchema)

        for query_filter in filters or []:
            query = query.filter(query_filter)

        query = query.order_by(EventSchema.created)

        return query

    def _translate_event(self, event: EventSchema) -> Event:
        """Translates an event schema record to an actual Event class.

        This is all a bit hairy fairy magic that I'd love for there to be a
        better way to achieve the same thing for. I'm sure there is if we just
        look hard enough or boil a frog to the witches of clean code.

        For now this works, and there are tests so we'll know if we broke it.

        We attempt to import from the `<event.model_type>/events` folder so
        it requires event structuring to be consistent.

        Args:
            event: An EventSchema record from the database.

        Returns:
            Our pure python Event class that can apply model mutations.
        """
        import_path = self._model.__module__.split('.')
        import_path.pop()
        import_path = '.'.join(import_path)
        import_path += '.events'

        event_class = getattr(
            importlib.import_module(import_path), event.event_type
        )

        return event_class(
            created=event.created,
            data=event.data,
            event_type=event.event_type,
            model_id=event.model_id,
            model_type=event.model_type
        )
