"""Collection of tests for the Employee model."""
from service.models.employee.employee import Employee
from service.models.employee.events import (
    ChangeJob, ChangeName, ChangeSalary, CreateEmployee
)
from freezegun import freeze_time
from datetime import datetime

def test_instantiating_normally():
    """Tests the model can be instantiated with normal data."""
    employee = Employee(id_=123, name='Alice', job='Manager', salary=5000)

    assert employee.id == 123
    assert employee.name == 'Alice'
    assert employee.job == 'Manager'
    assert employee.salary == 5000


@freeze_time(datetime(day=6, month=6, year=2020, hour=6))
def test_change_name_adds_event_and_updates_internal_data():
    """Tests changing name adds correct event and updates data."""
    employee = Employee(id_=123, name='Alice', job='Manager', salary=5000)
    employee.change_name(name='Bob')

    assert employee.id == 123
    assert employee.name == 'Bob'
    assert employee.job == 'Manager'
    assert employee.salary == 5000

    events = employee.unsaved_events
    assert events[0].created == datetime(day=6, month=6, year=2020, hour=6)
    assert events[0].model_id == 123
    assert events[0].model_type == 'Employee'
    assert events[0].event_type == 'ChangeName'
    assert events[0].data == {'name': 'Bob'}


@freeze_time(datetime(day=6, month=6, year=2020, hour=6))
def test_change_job_adds_event_and_updates_internal_data():
    """Tests changing job adds correct event and updates data."""
    employee = Employee(id_=123, name='Alice', job='Manager', salary=5000)
    employee.change_job(job='CEO')

    assert employee.id == 123
    assert employee.name == 'Alice'
    assert employee.job == 'CEO'
    assert employee.salary == 5000

    events = employee.unsaved_events
    assert events[0].created == datetime(day=6, month=6, year=2020, hour=6)
    assert events[0].model_id == 123
    assert events[0].model_type == 'Employee'
    assert events[0].event_type == 'ChangeJob'
    assert events[0].data == {'job': 'CEO'}


@freeze_time(datetime(day=6, month=6, year=2020, hour=6))
def test_change_salary_adds_event_and_updates_internal_data():
    """Tests changing salary adds correct event and updates data."""
    employee = Employee(id_=123, name='Alice', job='Manager', salary=5000)
    employee.change_salary(salary=65000)

    assert employee.id == 123
    assert employee.name == 'Alice'
    assert employee.job == 'Manager'
    assert employee.salary == 65000

    events = employee.unsaved_events
    assert events[0].created == datetime(day=6, month=6, year=2020, hour=6)
    assert events[0].model_id == 123
    assert events[0].model_type == 'Employee'
    assert events[0].event_type == 'ChangeSalary'
    assert events[0].data == {'salary': 65000}


@freeze_time(datetime(day=6, month=6, year=2020, hour=6))
def test_create_adds_event_and_updates_internal_data():
    """Tests creating adds correct event and updates data."""
    employee = Employee(id_=123)
    employee.create(name='Bob', job='Manager', salary=23000)

    assert employee.id == 123
    assert employee.name == 'Bob'
    assert employee.job == 'Manager'
    assert employee.salary == 23000

    events = employee.unsaved_events
    assert events[0].created == datetime(day=6, month=6, year=2020, hour=6)
    assert events[0].model_id == 123
    assert events[0].model_type == 'Employee'
    assert events[0].event_type == 'CreateEmployee'
    assert events[0].data == {'name': 'Bob', 'job': 'Manager', 'salary': 23000}
