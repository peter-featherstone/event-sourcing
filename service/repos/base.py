import importlib
from collections import defaultdict

from service.models.schema.event import EventSchema


class BaseRepository:

    _entity = None

    def __init__(self, db):
        self._db = db

    def get(self, _id):
        events = self._query(
            filters=[
                EventSchema.aggregate_id == _id,
                EventSchema.aggregate_type == self._entity.__name__
            ]
        ).all()

        entity_events = [self._translate_event(event) for event in events]

        return self._entity(_id=_id, events=entity_events)

    def all(self):
        events = self._query(
            filters=[
                EventSchema.aggregate_type == self._entity.__name__
            ]
        ).all()

        entity_events = defaultdict(list)
        for event in events:
            entity_events[event.aggregate_id].append(
                self._translate_event(event)
            )

        return EntityList(
            entities=[
                self._entity(_id=aggregate_id, events=events)
                for aggregate_id, events in entity_events.items()
            ],
            events=[self._translate_event(event) for event in events]
        )

    def _query(self, filters=None):
        query = self._db.query(EventSchema)

        for query_filter in filters or []:
            query = query.filter(query_filter)

        query = query.order_by(EventSchema.event_id)

        return query

    def save(self, entity):
        for entity_event in entity.unsaved_events:
            event = EventSchema(
                created=entity_event.created,
                aggregate_id=entity_event.aggregate_id,
                aggregate_type=entity_event.aggregate_type,
                event_type=entity_event.event_type,
                data=entity_event.data
            )

            self._db.add(event)

        self._db.commit()

    def _translate_event(self, event):
        import_path = self._entity.__module__.split('.')
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
            aggregate_id=event.aggregate_id,
            aggregate_type=event.aggregate_type
        )


class EntityList:

    def __init__(self, entities, events):
        self.entities = entities
        self.events = events
