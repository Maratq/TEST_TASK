"""Create Database

Revision ID: df9d2c5fb1bd
Revises: 
Create Date: 2023-07-03 15:20:57.976416

"""
import uuid

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'df9d2c5fb1bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    sa.Column('uuid', sa.UUID, primary_key=True, default=uuid.uuid4)
    sa.Column('text', sa.String,nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###