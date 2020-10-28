"""Tests for the employee endpoints."""


def test_create_form(app):
    """Test the create employee form returns expected 200 response."""
    response = app.get('/employee/create')

    assert response.status_code == 200
    assert 'Create Employee' in str(response.data)


def test_get_employees(app):
    """Test the get all employees page returns expected 200 response."""
    response = app.get('/employees')

    assert response.status_code == 200
    assert 'All Events' in str(response.data)
    assert 'Alice' in str(response.data)


def test_get_employee(app):
    """Test the get employee page returns expected 200 response."""
    response = app.get('/employee/c1736b8d-2064-47ac-861c-93b4fc2fcbd2')

    assert response.status_code == 200
    assert 'Alice' in str(response.data)
    assert 'Retail Assistant' in str(response.data)
    assert '19000' in str(response.data)


def test_create_employee(app):
    """Test creating employee returns the expected 200 response."""
    response = app.post(
        '/employee',
        data={
            'job': 'Sales Assistant',
            'name': 'Bob',
            'salary': 24000
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert 'Bob' in str(response.data)
    assert 'Sales Assistant' in str(response.data)
    assert '24000' in str(response.data)


def test_update_employee(app):
    """Test updating employee returns expected 200 response."""
    response = app.post(
        '/employee/c1736b8d-2064-47ac-861c-93b4fc2fcbd2',
        data={
            'job': 'Regional Manager',
            'name': 'Charlie',
            'salary': 45000
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert 'Charlie' in str(response.data)
    assert 'Regional Manager' in str(response.data)
    assert '45000' in str(response.data)


def test_partially_updating_employee(app):
    """Test partially updating an employee returns expected 200 response."""
    response = app.post(
        '/employee/c1736b8d-2064-47ac-861c-93b4fc2fcbd2',
        data={
            'job': '',
            'name': 'Bob',
            'salary': ''
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert 'Bob' in str(response.data)
    assert 'Retail Assistant' in str(response.data)
    assert '19000' in str(response.data)
