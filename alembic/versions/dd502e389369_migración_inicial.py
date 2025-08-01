"""Migración inicial

Revision ID: dd502e389369
Revises: 
Create Date: 2025-07-31 17:56:36.890369

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'dd502e389369'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personas_bloqueadas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_completo', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_personas_bloqueadas_id'), 'personas_bloqueadas', ['id'], unique=False)
    op.create_index(op.f('ix_personas_bloqueadas_nombre_completo'), 'personas_bloqueadas', ['nombre_completo'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_personas_bloqueadas_nombre_completo'), table_name='personas_bloqueadas')
    op.drop_index(op.f('ix_personas_bloqueadas_id'), table_name='personas_bloqueadas')
    op.drop_table('personas_bloqueadas')
    # ### end Alembic commands ###
