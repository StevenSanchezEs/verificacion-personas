from sqlmodel import SQLModel

class UserRequest(SQLModel):
    nombre_completo: str
