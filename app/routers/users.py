from fastapi import APIRouter, Depends, HTTPException, status
from app.models.blacklist import BlackList
from app.schemas.user import UserRequest
from app.utils.auth import verify_jwt_token
from app.repositories.blacklist_repository import BlacklistRepository
from app.core.database import SessionDep
from sqlalchemy.exc import SQLAlchemyError 

router = APIRouter()


@router.post("/verificar", status_code=status.HTTP_200_OK, dependencies=[Depends(verify_jwt_token)])
def verify_user(user: UserRequest, session: SessionDep):
    try:
        # Validar que el nombre no esté vacío o sea inválido (ejemplo)
        if not user.nombre_completo or not user.nombre_completo.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El campo 'nombre_completo' es obligatorio y no puede estar vacío."
            )

        nombre_completo_normalizado = user.nombre_completo.strip().lower()

        if BlacklistRepository.is_blacklisted(session, nombre_completo_normalizado):
            return {"encontrado": True}
    
        return {"encontrado": False}

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error en la conexión a la base de datos."
        )
