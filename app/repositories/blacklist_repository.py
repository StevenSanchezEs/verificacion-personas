from sqlmodel import Session, select
from app.models.blacklist import BlackList


class BlacklistRepository:
    @staticmethod
    def is_blacklisted(session: Session, nombre_completo: str) -> bool:
        nombre_completo_normalizado = nombre_completo.strip().lower()
        statement = select(BlackList).where(BlackList.nombre_completo == nombre_completo_normalizado)
        result = session.exec(statement).first()
        return result is not None
