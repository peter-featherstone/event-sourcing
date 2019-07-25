class BaseRepository:

    _entity = None

    def __init__(self, db):
        self._db = db

    def get(self, _id):
        return self._query().first()

    def all(self, filters=None):
        return self._query(filters=filters).all()

    def _query(self, filters=None):
        query = self._db.query(self._entity)

        for query_filter in filters or []:
            query = query.filter(query_filter)

        return query

    def delete(self, entity):
        # TODO: Commit a delete event.
        pass

    def commit(self):
        # TODO: Commit all events.
        pass
