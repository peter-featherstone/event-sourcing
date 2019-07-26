import importlib
from service.models.schema.event import EventSchema


class BaseRepository:

    _entity = None

    def __init__(self, db):
        self._db = db

    def get(self, _id):
        events = self.all(
            filters=[
                EventSchema.aggregate_id == _id,
                EventSchema.aggregate_type == self._entity.__name__
            ]
        )

        entity_events = [self._translate_event(event) for event in events]

        return self._entity(events=entity_events)

    def all(self, filters=None):
        return self._query(filters=filters).all()

    def _query(self, filters=None):
        query = self._db.query(EventSchema)

        for query_filter in filters or []:
            query = query.filter(query_filter)

        query = query.order_by(EventSchema.event_id)

        return query

    def delete(self, entity):
        # TODO: Commit a delete event.
        pass

    def commit(self):
        # TODO: Commit all events.
        pass

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
            aggregate_type=event.aggregate_type,
            user_id=event.user_id,
        )
