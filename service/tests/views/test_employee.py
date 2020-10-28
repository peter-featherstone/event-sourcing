"""Tests for the main endpoints."""


def test_index(app):
    """Test the index endpoint returns the expected 200 response."""
    response = app.get('/')

    assert response.status_code == 200
    assert 'A playground for testing and breaking' in str(response.data)
