from sqlmodel import SQLModel, Field
from typing import Optional


class BlackList(SQLModel, table=True):
    __tablename__ = "personas_bloqueadas"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    nombre_completo: str = Field(index=True, nullable=False, unique=True)
