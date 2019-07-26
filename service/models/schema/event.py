from service.repos.database import db


class EventSchema(db.Model):

    __tablename__ = 'events'

    created = db.Column(db.DateTime)
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_type = db.Column(db.String)
    aggregate_id = db.Column(db.Integer)
    aggregate_type = db.Column(db.String)
    data = db.Column(db.JSON)
    user_id = db.Column(db.Integer)
