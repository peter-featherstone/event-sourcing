"""Collection of events for the base event model."""
from datetime import datetime
from uuid import UUID, uuid4

import pytest

from service.models.event import Event
from service.models.model import Model


def test_apply_method_must_be_implemented():
    """Tests that the apply method raises an error if not implemented."""
    event = Event(
        created=datetime(2020, 6, 6, 13, 23, 14),
        event_type='ChangeSalary',
        model_id=UUID('c1736b8d-2064-47ac-861c-93b4fc2fcbd2'),
        model_type='Employee',
        data={'salary': 19000}
    )

    with pytest.raises(NotImplementedError) as error:
        event.apply(model=Model(id_=uuid4()))

    assert str(error.value) == 'All events must implement an apply method.'



