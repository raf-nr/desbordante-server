"""create file and dataset tables

Revision ID: 6a59d47fe978
Revises: 03c0f0f4b98e
Create Date: 2024-04-02 01:54:21.955372

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "6a59d47fe978"
down_revision: Union[str, None] = "03c0f0f4b98e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "file",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("mime_type", sa.String(), nullable=False),
        sa.Column("file_name", sa.Uuid(), nullable=False),
        sa.Column("original_file_name", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "dataset",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("is_built_in", sa.Boolean(), nullable=False),
        sa.Column("header", postgresql.ARRAY(sa.Integer()), nullable=False),
        sa.Column("separator", sa.String(), nullable=False),
        sa.Column("file_id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.ForeignKeyConstraint(
            ["file_id"],
            ["file.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("dataset")
    op.drop_table("file")
    # ### end Alembic commands ###