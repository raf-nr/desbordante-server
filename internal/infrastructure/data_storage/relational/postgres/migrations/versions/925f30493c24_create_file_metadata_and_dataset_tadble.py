"""create_file_metadata_and_dataset_tadble

Revision ID: 925f30493c24
Revises: a6df7c9124be
Create Date: 2024-09-18 22:50:48.547252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '925f30493c24'
down_revision: Union[str, None] = 'a6df7c9124be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_metadata',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('mime_type', sa.String(), nullable=False),
    sa.Column('file_name', sa.Uuid(), nullable=False),
    sa.Column('original_file_name', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dataset',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('is_built_in', sa.Boolean(), nullable=False),
    sa.Column('header', sa.ARRAY(sa.Integer()), nullable=False),
    sa.Column('separator', sa.String(), nullable=False),
    sa.Column('file_id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['file_id'], ['file_metadata.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dataset')
    op.drop_table('file_metadata')
    # ### end Alembic commands ###
