"""Initial setup.

Revision ID: 49239e06e506
Revises: 
Create Date: 2019-07-25 15:43:57.831288

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '49239e06e506'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'events',
        sa.Column('created', sa.DateTime, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('event_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('event_type', sa.String, nullable=False),
        sa.Column('model_id', UUID(as_uuid=True), nullable=False),
        sa.Column('model_type', sa.String, nullable=False),
        sa.Column('data', sa.JSON, nullable=False)
    )

    op.create_index(
        'ix_model', 'events',
        ['model_id', 'model_type']
    )


def downgrade():
    op.drop_table('events')
