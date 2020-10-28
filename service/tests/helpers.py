"""Collection of helpers for use in tests."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from service.models.schema.event import EventSchema


def get_in_memory_database():
    """Create an in-memory sqlalchemy session for use in tests.

    Ideally we would use the same database type as our main database store in
    production rather than SQLite so for full integration tests or specific db
    tests you may need to consider this.

    Returns:
        sqlalchemy session object.
    """
    engine = create_engine('sqlite://')

    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    session._model_changes = {}

    EventSchema.metadata.create_all(engine)

    return session
