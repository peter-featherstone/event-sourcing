"""Definition of the structure for our event schema object in persistence."""
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID

from service.repos.database import db


class EventSchema(db.Model):
    """Class definition of our event schema model."""

    __tablename__ = 'events'

    created = db.Column(db.DateTime, default=datetime.now())
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_type = db.Column(db.String)
    aggregate_id = db.Column(UUID(as_uuid=True))
    aggregate_type = db.Column(db.String)
    data = db.Column(db.JSON)
