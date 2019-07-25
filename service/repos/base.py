class BaseRepository:

    _model = None

    def __init__(self, db):
        """Instantiate the repository with a db session."""
        self._db = db

    def get(self, _id, **kwargs):
        # TODO: Get model from it's events.
        pass

    def all(self, **kwargs):
        """Return all _models.

        Returns:
            obj: An EntityList object.
        """
        return self._build_list(self._query(**kwargs))

    def _query(self, **kwargs):
        query = self._db.query(self._model)

        if kwargs.get('filters'):
            for query_filter in kwargs.get('filters'):
                query = query.filter(query_filter)

        return query

    def _build_list(self, query):

        return query.all()

    def delete(self, entity):
        # TODO: Commit a delete event.
        pass

    def commit(self):
        # TODO: Commit all events.
        pass
