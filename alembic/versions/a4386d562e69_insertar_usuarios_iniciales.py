"""Insertar usuarios iniciales

Revision ID: a4386d562e69
Revises: dd502e389369
Create Date: 2025-07-31 18:04:54.676121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'a4386d562e69'
down_revision: Union[str, Sequence[str], None] = 'dd502e389369'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
        INSERT INTO personas_bloqueadas (nombre_completo) VALUES
        ('juan pérez'),
        ('maría lópez'),
        ('carlos hernández'),
        ('ana gonzález'),
        ('pedro ramírez'),
        ('lucía martínez'),
        ('josé fernández'),
        ('elena castro'),
        ('miguel torres'),
        ('sofía díaz');
    """)


def downgrade():
    op.execute("""
        DELETE FROM personas_bloqueadas
        WHERE nombre_completo IN (
            'juan pérez','maría lópez','carlos hernández',
            'ana gonzález','pedro ramírez','lucía martínez',
            'josé fernández','elena castro','miguel torres','sofía díaz'
        );
    """)
