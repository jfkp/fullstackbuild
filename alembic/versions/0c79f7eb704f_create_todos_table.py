"""create todos table

Revision ID: 0c79f7eb704f
Revises: 
Create Date: 2024-10-30 17:56:21.410679

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c79f7eb704f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)


def downgrade() -> None:
    op.execute("drop table todos;")
