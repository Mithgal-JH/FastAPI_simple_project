from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, JWTtoken
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(prefix="/login", tags=["Authentication"])


@router.post("/")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):

    invalid_credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise invalid_credentials_exception

    if not Hash.verify_password(request.password, user.password):
        raise invalid_credentials_exception

    access_token = JWTtoken.create_access_token(data={"sub": user.email})

    return schemas.Token(access_token=access_token, token_type="bearer")
