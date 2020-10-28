"""Collection of test data just used for view testing."""
from datetime import datetime
from uuid import UUID

from service.models.schema.event import EventSchema

VIEW_DATASET = {
    EventSchema: [
        {
            'created': datetime(2020, 6, 6, 13, 23, 12),
            'event_id': 1,
            'event_type': 'ChangeJob',
            'aggregate_id': UUID('c1736b8d-2064-47ac-861c-93b4fc2fcbd2'),
            'aggregate_type': 'Employee',
            'data': {'job': 'Retail Assistant'}
        },
        {
            'event_id': 2,
            'created': datetime(2020, 6, 6, 13, 23, 13),
            'event_type': 'ChangeName',
            'aggregate_id': UUID('c1736b8d-2064-47ac-861c-93b4fc2fcbd2'),
            'aggregate_type': 'Employee',
            'data': {'name': 'Alice'}
        },
        {
            'event_id': 3,
            'created': datetime(2020, 6, 6, 13, 23, 14),
            'event_type': 'ChangeSalary',
            'aggregate_id': UUID('c1736b8d-2064-47ac-861c-93b4fc2fcbd2'),
            'aggregate_type': 'Employee',
            'data': {'salary': 19000}
        }
    ]
}
