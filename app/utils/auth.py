from fastapi import Header, HTTPException, status
from decouple import config

HARDCODED_JWT = config("HARDCODED_JWT")


def verify_jwt_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o faltante")
    
    token = authorization.split(" ")[1]
    if token != HARDCODED_JWT:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    
    return True
