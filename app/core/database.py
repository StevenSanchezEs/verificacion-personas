from typing import Annotated
from sqlmodel import create_engine, Session
from decouple import config
from fastapi import Depends

DATABASE_URL = config("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
