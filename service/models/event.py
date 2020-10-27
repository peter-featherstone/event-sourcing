class Event:

    def __init__(
        self, created, data, event_type, aggregate_id, aggregate_type
    ):
        self.created = created
        self.event_type = event_type
        self.aggregate_id = aggregate_id
        self.aggregate_type = aggregate_type
        self.data = data
