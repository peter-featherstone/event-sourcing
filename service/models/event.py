class Event:

    def __init__(self, created, data, event_type, aggregate_type, user_id):
        self.created = created
        self.event_type = event_type
        self.aggregate_type = aggregate_type
        self.data = data
        self.user_id = user_id
