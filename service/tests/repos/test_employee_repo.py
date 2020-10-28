"""Collection of tests for the Employee repository."""
from datetime import datetime
from uuid import UUID

import pytest

from service.models.employee.employee import Employee
from service.models.schema.event import EventSchema
from service.repos import EmployeeRepository, get_employee_repo
from service.tests.helpers import get_in_memory_database

TEST_DATA = [
    {
        'created': datetime(2020, 6, 6, 13, 23, 12),
        'event_id': 1,
        'event_type': 'ChangeJob',
        'model_id': UUID('c1736b8d-2064-47ac-861c-93b4fc2fcbd2'),
        'model_type': 'Employee',
        'data': {'job': 'Retail Assistant'}
    },
    {
        'event_id': 2,
        'created': datetime(2020, 6, 6, 13, 23, 13),
        'event_type': 'ChangeName',
        'model_id': UUID('c1736b8d-2064-47ac-861c-93b4fc2fcbd2'),
        'model_type': 'Employee',
        'data': {'name': 'Alice'}
    },
    {
        'event_id': 3,
        'created': datetime(2020, 6, 6, 13, 23, 14),
        'event_type': 'ChangeSalary',
        'model_id': UUID('c1736b8d-2064-47ac-861c-93b4fc2fcbd2'),
        'model_type': 'Employee',
        'data': {'salary': 19000}
    },
    {
        'event_id': 4,
        'created': datetime(2020, 6, 6, 13, 23, 15),
        'event_type': 'CreateEmployee',
        'model_id': UUID('ec316473-a32d-4a0d-b5e7-79d253ae4a96'),
        'model_type': 'Employee',
        'data': {'name': 'Alice', 'job': 'Manager', 'salary': 43500}
    },
    {
        'event_id': 5,
        'created': datetime(2020, 6, 6, 13, 23, 16),
        'event_type': 'ChangeName',
        'model_id': UUID('c1736b8d-2064-47ac-861c-93b4fc2fcbd2'),
        'model_type': 'Employee',
        'data': {'name': 'Bob'}
    }
]


@pytest.fixture()
def repo() -> EmployeeRepository:
    """Instantiates a repo for testing."""
    db = get_in_memory_database()
    db.bulk_insert_mappings(EventSchema, TEST_DATA)

    return get_employee_repo(db=db)


def test_can_be_instantiated_from_factory(repo):
    """Tests that the repo can be instantiated from a factory."""
    assert isinstance(repo, EmployeeRepository)


def test_get_returns_fully_hydrated_model(repo):
    """Tests that the repo gets and hydrates a full model by id from events."""
    employee = repo.get(id_=UUID('c1736b8d-2064-47ac-861c-93b4fc2fcbd2'))

    assert isinstance(employee, Employee)
    assert employee.name == 'Bob'
    assert employee.job == 'Retail Assistant'
    assert employee.salary == 19000


def test_all_returns_fully_hydrated_models(repo):
    """Tests that the repo gets all models and fully hydrates from events."""
    employees = repo.all().models

    assert len(employees) == 2

    assert isinstance(employees[0], Employee)
    assert employees[0].name == 'Bob'
    assert employees[0].job == 'Retail Assistant'
    assert employees[0].salary == 19000

    assert isinstance(employees[1], Employee)
    assert employees[1].name == 'Alice'
    assert employees[1].job == 'Manager'
    assert employees[1].salary == 43500


def test_saving_a_model_includes_all_events(repo):
    """Tests that saving a model saves all it's events and clears unsaved."""
    assert not repo.get(UUID('cae4b42f-0c64-4204-97c2-e36086ee0fbb'))

    employee = Employee(id_=UUID('cae4b42f-0c64-4204-97c2-e36086ee0fbb'))
    employee.create(name='Charlie', job='CEO', salary=1_000_000)
    employee.change_salary(salary=2_000_000)

    assert len(employee.unsaved_events) == 2

    repo.save(model=employee)

    employee = repo.get(UUID('cae4b42f-0c64-4204-97c2-e36086ee0fbb'))

    assert isinstance(employee, Employee)
    assert employee.name == 'Charlie'
    assert employee.job == 'CEO'
    assert employee.salary == 2_000_000

    assert not employee.unsaved_events
