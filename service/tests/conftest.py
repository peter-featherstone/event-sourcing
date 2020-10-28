"""Collection of fixtures accessible globally to all test methods."""
import pytest
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.compiler import compiles

from service import app as application
from service.repos.database import db
from .test_data import VIEW_DATASET


@pytest.fixture()
def app():
    """Provide a testing Flask application for view testing.

    This fixture provides an in-memory sqlite database with seeded data.

    To get the original application, for example it's config variables you can
    call `app.application` on the fixture. i.e `app.application.config`.

    Example Usage:
        def test_foo_endpoint_returns_expected_list(app):
            response = app.get('/foo')

            assert response.status_code == 200
            assert json.loads(response.data) == ['foo', 'bar']
    """
    application.config['TESTING'] = True

    with application.app_context():
        db.drop_all()
        db.create_all()

        for model, records in VIEW_DATASET.items():
            db.session.bulk_insert_mappings(model, records)

        db.session.commit()

    with application.test_client() as context:
        yield context


@compiles(UUID, 'sqlite')
def compile_uuid_sqlite(element, compiler, **kw) -> None:
    """Compile UUID types for sqlite.

    SQLite does not support a UUID type but is used by our tests.

    The compiles decorator registers itself with the model so that it is
    invoked when the object is compiled to a UUID type in a sqlite engine,
    and instead returns a String type.
    """
    return "String"
